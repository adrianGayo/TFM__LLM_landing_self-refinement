import torch 
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import random
from collections import namedtuple, deque

BUFFER_SIZE = int(1e5)  # replay buffer size
BATCH_SIZE = 64         # minibatch size
GAMMA = 0.99            # discount factor
TAU = 1e-3              # for soft update of target parameters
LR = 5e-4               # learning rate 
UPDATE_EVERY = 4        # how often to update the network
LR_ACTOR = 0.001
LR_CRITIC= 0.001

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


class DuelingQNetwork(nn.Module):
    """Dueling DQN (Deep Q-Network). Variante de la arquitectura DQN"""

    def __init__(self, num_observaciones, num_acciones, seed, fc1_size = 64, fc2_size = 64):
        """Constructor de la red.
        Params
        ======
            num_observaciones (int): Dimensión del vector de observaciones.
            num_acciones (int): Dimensión del vector de acciones.
            seed (int): Semilla para la inicialización de pesos
        """
        
        super(DuelingQNetwork, self).__init__()
        self.num_actions = num_acciones
        fc3_1_size = fc3_2_size = 32
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(num_observaciones, fc1_size)
        self.fc2 = nn.Linear(fc1_size, fc2_size)
        ## Here we separate into two streams
        # The one that calculate V(s)
        self.fc3_1 = nn.Linear(fc2_size, fc3_1_size)
        self.fc4_1 = nn.Linear(fc3_1_size, 1)
        # The one that calculate A(s,a)
        self.fc3_2 = nn.Linear(fc2_size, fc3_2_size)
        self.fc4_2 = nn.Linear(fc3_2_size, num_acciones)



    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))

        val = F.relu(self.fc3_1(x))
        val = self.fc4_1(val)
        
        adv = F.relu(self.fc3_2(x))
        adv = self.fc4_2(adv)
        # Q(s,a) = V(s) + (A(s,a) - 1/|A| * sum A(s,a'))
        action = val + adv - adv.mean(1).unsqueeze(1).expand(state.size(0), self.num_actions)
        return action


class Agent():
    """Interactúa y aprende del entorno."""

    def __init__(self, num_observaciones, num_acciones, red_modelo, seed=None):
        """Inicializa un objeto Agente.
            
        Parámetros
        =========
            num_observaciones (int): Dimensión del vector de observaciones.
            num_acciones (int): Dimensión del vector de acciones.
            seed (int): semilla aleatoria
        """
        self.num_observaciones = num_observaciones
        self.num_acciones = num_acciones
        self.seed = random.seed(seed)

        # Intanciamos las redes
        self.dqn_principal = red_modelo(num_observaciones, num_acciones, seed).to(device)
        self.dqn_target = red_modelo(num_observaciones, num_acciones, seed).to(device)
        self.optimizer = optim.Adam(self.dqn_principal.parameters(), lr=LR) #Hiperparámetro.

        # Replay memory
        self.memory = ReplayBuffer(num_acciones, BUFFER_SIZE, BATCH_SIZE, seed)
        # Initialize time step (for updating every UPDATE_EVERY steps)
        self.t_step = 0

    def step(self, state, action, reward, next_state, done):
        # Save experience in replay memory
        self.memory.add(state, action, reward, next_state, done)

        # Learn every UPDATE_EVERY time steps.
        self.t_step = (self.t_step + 1) % UPDATE_EVERY
        if self.t_step == 0:
            # If enough samples are available in memory, get random subset and learn
            if len(self.memory) > BATCH_SIZE:
                experiences = self.memory.sample()
                self.learn(experiences, GAMMA)

    def act(self, estado, eps=0.):
        """Devuelve la acción que debe tomar el agente en función del estado.
        
        Params
        ======
            estado (array_like): estado actual.
            eps (float): epsilon, for epsilon-greedy action selection
        """
        #print(f"estado:{estado}")
        estado = torch.from_numpy(estado).float().unsqueeze(0).to(device)
        self.dqn_principal.eval()
        with torch.no_grad():
            action_values = self.dqn_principal(estado)
        self.dqn_principal.train()

        # Epsilon-greedy action selection
        if random.random() > eps:
            return np.argmax(action_values.cpu().data.numpy())
        else:
            return random.choice(np.arange(self.num_acciones))

    def learn(self, experiences, gamma):
        """Actualiza los parámetros de valor utilizando el lote de tuplas de experiencia dado.

        Parámetros
        =========
            experiences (Tuple[torch.Variable]): tupla de tuplas (s, a, r, s', done)
            gamma (float): factor de descuento
        """
        # Obtiene las tuplas de experiencia descopuestas.
        states, actions, rewards, next_states, dones = experiences

        ## Compute and minimize the loss
        ### Extrae el valor máximo de las acciones futuras del modelo objetivo.
        q_targets_next = self.dqn_principal(next_states).detach().max(1)[0].unsqueeze(1)
        ### Calculate target value from bellman equation
        q_targets = rewards + gamma * q_targets_next * (1 - dones)
        ### Calculate expected value from local network
        q_expected = self.dqn_principal(states).gather(1, actions)

        ### Loss calculation (we used Mean squared error)
        loss = F.mse_loss(q_expected, q_targets)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # ------------------- update target network ------------------- #
        self.soft_update(self.dqn_principal, self.dqn_target, TAU)

    def soft_update(self, local_model, target_model, tau):
        """Soft update model parameters.
        θ_target = τ*θ_local + (1 - τ)*θ_target

        Params
        ======
            local_model (PyTorch model): weights will be copied from
            target_model (PyTorch model): weights will be copied to
            tau (float): interpolation parameter
        """
        for target_param, local_param in zip(target_model.parameters(), local_model.parameters()):
            target_param.data.copy_(tau*local_param.data + (1.0-tau)*target_param.data)


    def load_weights(self, filepath):
        """
        Carga los pesos de la red desde un archivo.

        Parámetros
        ==========
            filepath (str): Ruta al archivo que contiene los pesos.
        """
        self.dqn_principal.load_state_dict(torch.load(filepath))
        self.dqn_target.load_state_dict(torch.load(filepath))
        
        
class ReplayBuffer:
    """Fixed-size buffer to store experience tuples."""
    
    def __init__(self, num_acciones, buffer_size, batch_size, seed=None):
        """Initialize a ReplayBuffer object.
        Params
        ======
            num_acciones (int): Dimensión del vector de acciones.
            buffer_size (int): Tamaño máximo del buffer.
            batch_size (int): Tamaño del lote.
            seed (int): random seed
        """
        self.num_acciones = num_acciones
        self.memory = deque(maxlen=buffer_size)  
        self.batch_size = batch_size
        self.experience = namedtuple("Experience", field_names=["state", "action", "reward", "next_state", "done"])
        if seed is not None:
            self.seed = random.seed(seed)
    
    def add(self, state, action, reward, next_state, done):
        """Añade una nueva experienccia en memoria."""
        e = self.experience(state, action, reward, next_state, done)
        self.memory.append(e)
    
    def sample(self):
        """Randomly sample a batch of experiences from memory."""
        experiences = random.sample(self.memory, k=self.batch_size)

        states = torch.from_numpy(np.vstack([e.state for e in experiences if e is not None])).float().to(device)
        actions = torch.from_numpy(np.vstack([e.action for e in experiences if e is not None])).long().to(device)
        rewards = torch.from_numpy(np.vstack([e.reward for e in experiences if e is not None])).float().to(device)
        next_states = torch.from_numpy(np.vstack([e.next_state for e in experiences if e is not None])).float().to(device)
        dones = torch.from_numpy(np.vstack([e.done for e in experiences if e is not None]).astype(np.uint8)).float().to(device)
  
        return (states, actions, rewards, next_states, dones)

    def __len__(self):
        """Return the current size of internal memory."""
        return len(self.memory)
    

def test(agente, env, max_t=1000, video_recorder=None):
    """Ejecuta un episodio de prueba utilizando el agente entrenado.
    
    Parámetros
    =========
        agente: Instancia del agente entrenado
        max_t (int): número máximo de pasos por episodio
    """
    state = env.reset()
    state = state[0] # Corregimos bug que nos devolvía una tupla.
    score = 0
    if video_recorder:
        video_recorder.start_video_recorder()
        
    for t in range(max_t):
        action = agente.act(state, eps=0)  # Elegir la acción de forma codiciosa
        if video_recorder:
            next_state, reward, done, _, _ = video_recorder.step(action)
        else:
            next_state, reward, done, _, _ = env.step(action)
            
        state = next_state
        score += reward
        if done:
            break 
        
    print("\nTest score:", score)
    return score
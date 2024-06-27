from openai import OpenAI


class AssistantOpenAI:
    """ Clase para interactuar con la API de OpenAI.
    """
    
    def __init__(self, api_key):
        """ Constructor de la clase.

        Args:
            api_key (string): openai api key.
        """
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)
        self.assistants = []
        self.threads = []
        self.messages = []
        self.runs = []
          
    def create_assistant(self, name="Default assistant", model="gpt-3.5-turbo", description="", instructions="", tools={}):
        """ Crea un asistente en OpenAI.
    
        Args:
            name (str, optional): El nombre del asistente. Por defecto es "Default assistant".
            model (str, optional): El modelo de IA a utilizar. Por defecto es "gpt-4".
            description (str, optional): Una descripción del asistente. Por defecto es "".
            instructions (str, optional): Instrucciones para el asistente. Por defecto es "".
            tools (list, optional): Una lista de herramientas para el asistente. Por defecto es None.
            **kwargs: Argumentos adicionales.
            
        Returns:
            dict: Información del asistente.
        """
        response = self.client.beta.assistants.create(
            model=model,
            name=name,
            description=description,
            instructions=instructions,
            tools=tools)
        self.assistants.append(response.id)
        return response
    
    def get_assistant(self, assistant_id, **kwargs):
        """ 
        Obtiene la información de un asistente.
        
        Args:
        
            assistant_id (str): El id del asistente.
            **kwargs: Argumentos adicionales.
            
        Returns:
            dict: Información del asistente.
                
        """
        response = self.client.beta.assistants.retrieve(assistant_id, **kwargs)
        return response
    
    def delete_assistant(self, assistant_id, **kwargs):
        """ Elimina un asistente.
        
        Args:
        
            assistant_id (str): El id del asistente.
            **kwargs: Argumentos adicionales.
            
        Returns:
            dict: Información de la eliminación.
        """
        response = self.client.beta.assistants.delete(assistant_id, **kwargs)
        return response
    
    def create_thread(self, **kwargs):
        """ Crea un hilo de conversación.
        
        Args:
            **kwargs: Argumentos adicionales.
            
        Returns:
            dict: Información del hilo.
        """
        response = self.client.beta.threads.create(**kwargs)
        self.threads.append(response.id)
        return response
    
    def get_thread(self, thread_id, **kwargs):
        """ Obtiene la información de un hilo.
        
        Args:
            thread_id (str): El id del hilo.
            **kwargs: Argumentos adicionales.
            
        Returns:
            dict: Información del hilo.
        """
        
        response = self.client.beta.threads.retrieve(thread_id, **kwargs)
        return response
    
    def delete_thread(self, thread_id, **kwargs):
        """ Elimina un hilo.
        
        Args:
            thread_id (str): El id del hilo.
            **kwargs: Argumentos adicionales.
        
        Returns:
            dict: Información de la eliminación.
        """
        response = self.client.beta.threads.delete(thread_id, **kwargs)
        return response
    
    def add_message(self, thread_id, role, content, **kwargs):
        """ Añade un mensaje a un hilo.
        
        Args:
            thread_id (str): El id del hilo.
            role (str): El rol del mensaje.
            content (str): El contenido del mensaje.
            **kwargs: Argumentos adicionales.
        
        Returns:
            dict: Información del mensaje.
        """
        response = self.client.beta.threads.messages.create(thread_id=thread_id, content=content, role=role, **kwargs)
        self.messages.append(response.id)
        return response
    
    def run(self, thread_id, assistant_id, tool_choice='auto', **kwargs):
        """ Ejecuta un hilo.
        
        Args:
            thread_id (str): El id del hilo.
            assistant_id (str): El id del asistente.
            **kwargs: Argumentos adicionales.
        
        Returns:
            dict: Información de la ejecución.
        """
        response = self.client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id, tool_choice=tool_choice, **kwargs)
        self.runs.append(response.id)
        return response
    
    def get_run(self, run_id, thread_id, **kwargs):
        """ Obtiene la información de una ejecución.
        
        Args:
            run_id (str): El id de la ejecución.
            thread_id (str): El id del hilo.
            **kwargs: Argumentos adicionales.
            
        Returns:
            dict: Información de la ejecución.
        """
        response = self.client.beta.threads.runs.retrieve(run_id, thread_id=thread_id, **kwargs)
        return response
    
    def devolver_respuesta(self, run_id, thread_id, tool_outputs, **kwargs):
        """ Devuelve una respuesta en caso de que el agente haya requerido una acción.
        
        Args:
            run_id (str): El id de la ejecución.
            thread_id (str): El id del hilo.
            tool_outputs (dict): Las salidas de las herramientas.
            **kwargs: Argumentos adicionales.
            
        Returns:
            dict: Información de la respuesta.
        """
        response = self.client.beta.threads.runs.submit_tool_outputs(run_id, thread_id=thread_id, tool_outputs=tool_outputs, **kwargs)
        return response
    
    
    def mostrar_mensajes(self, thread_id):
        """ Muestra los mensajes de un hilo.
        
        Args:
            thread_id (str): El id del hilo.
        
        Returns:
            list: Lista de mensajes.
        """
        response = self.client.beta.threads.messages.list(thread_id)
        for message in response.data:
            print(f"{message.role}: {message.content}")
        return response
    
    
    
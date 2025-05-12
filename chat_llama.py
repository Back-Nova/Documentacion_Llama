# chat_llama.py
from llama_cpp import Llama

class ChatLlama:
    def __init__(self, modelo_llama_path):
        # Inicializamos el modelo de Llama
        self.modelo_llama = Llama(modelo_llama_path)
        self.nombre_usuario = ""
        self.configurar_conversacion_basica()

    def configurar_conversacion_basica(self):
        # Definimos patrones de NLP simples para saludos y preguntas comunes
        self.respuestas_npl = {
            "hola": "¡Hola! ¿Cómo estás?",
            "¿cómo estás?": "Estoy bien, gracias por preguntar. ¿Y tú?",
            "¿cuál es tu nombre?": "Me llamo Llama, soy tu asistente virtual.",
            "adiós": "¡Hasta luego! Espero que hablemos pronto.",
        }

    def manejar_npl(self, mensaje):
        """Manejo de respuestas básicas antes de pasar a Llama."""
        mensaje = mensaje.lower()  # Convertimos todo a minúsculas para comparación
        if mensaje in self.respuestas_npl:
            return self.respuestas_npl[mensaje]
        return None

    def generar_respuesta_llama(self, mensaje):
        """Usamos el modelo Llama para generar respuestas más avanzadas."""
        # Aquí interactuamos con el modelo Llama
        respuesta = self.modelo_llama(
            prompt=f"Usuario: {mensaje}\nAsistente:", max_tokens=100, stop=["Usuario:", "Asistente:"]
        )
        return respuesta["choices"][0]["text"].strip()

    def preguntar_nombre(self):
        return "¡Hola! ¿Cómo te llamas?"

    def guardar_nombre(self, nombre):
        self.nombre_usuario = nombre
        return f"Mucho gusto, {self.nombre_usuario}. ¿En qué puedo ayudarte hoy?"

    def generar_respuesta(self, mensaje):
        """Manejo de la conversación: introducción, respuestas básicas y Llama."""
        # Si el nombre no ha sido registrado aún, lo pedimos
        if not self.nombre_usuario:
            return self.guardar_nombre(mensaje)

        # Intentamos primero manejar el mensaje con NLP básico
        respuesta_npl = self.manejar_npl(mensaje)
        if respuesta_npl:
            return respuesta_npl

        # Si no es un saludo o una pregunta básica, generamos una respuesta con Llama
        return self.generar_respuesta_llama(mensaje)


if __name__ == "__main__":
    # Ruta del modelo Llama que debes tener cargado previamente en tu entorno
    modelo_path = "./modelo_llama.bin"  # Reemplaza con la ruta a tu modelo
    chatbot = ChatLlama(modelo_path)

    # Iniciar la conversación con el usuario
    print(chatbot.preguntar_nombre())
    nombre = input("> ")  # Obtenemos el nombre del usuario
    print(chatbot.generar_respuesta(nombre))

    while True:
        mensaje = input(f"{chatbot.nombre_usuario}> ")
        respuesta = chatbot.generar_respuesta(mensaje)
        print(respuesta)
        if mensaje.lower() == "adiós":
            break

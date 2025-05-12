# main.py
from patrones_class.chat import Chat

if __name__ == "__main__":
    chat = Chat()

    chat.agregar_usuario("Santi")
    chat.enviar_mensaje("Santi", "¡Hola, Llama!")
    chat.enviar_mensaje("Santi", "¿Qué puedes hacer?")
    chat.ver_historial("Santi")

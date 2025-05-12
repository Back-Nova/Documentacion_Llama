# chat.py
from patrones_class.usuario import Usuario
from patrones_class.mensaje import Mensaje
from patrones_class.llama_ia import LlamaIA

class Chat:
    def __init__(self):
        self.usuarios = {}
        self.ia = LlamaIA()

    def agregar_usuario(self, nombre):
        if nombre not in self.usuarios:
            self.usuarios[nombre] = Usuario(nombre)
        else:
            print(f"El usuario {nombre} ya está registrado.")

    def enviar_mensaje(self, nombre, contenido):
        if nombre in self.usuarios:
            usuario = self.usuarios[nombre]
            mensaje = Mensaje(contenido, nombre, "Llama")
            usuario.agregar_mensaje(mensaje)
            respuesta = self.ia.generar_respuesta(contenido)
            respuesta_mensaje = Mensaje(respuesta, "Llama", nombre)
            usuario.agregar_mensaje(respuesta_mensaje)
            print(mensaje.mostrar_mensaje())
            print(respuesta_mensaje.mostrar_mensaje())
        else:
            print(f"El usuario {nombre} no está registrado.")

    def ver_historial(self, nombre):
        if nombre in self.usuarios:
            usuario = self.usuarios[nombre]
            for mensaje in usuario.obtener_historial():
                print(mensaje.mostrar_mensaje())
        else:
            print(f"El usuario {nombre} no está registrado.")

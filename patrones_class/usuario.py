# usuario.py
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

    def agregar_mensaje(self, mensaje):
        self.historial.append(mensaje)

    def obtener_historial(self):
        return self.historial

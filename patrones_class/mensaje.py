# mensaje.py
class Mensaje:
    def __init__(self, contenido, remitente, receptor):
        self.contenido = contenido
        self.remitente = remitente
        self.receptor = receptor

    def mostrar_mensaje(self):
        return f"{self.remitente}: {self.contenido}"

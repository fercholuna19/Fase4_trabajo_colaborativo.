# Importamos las herramientas para crear clases abstractas
from abc import ABC, abstractmethod


# Clase abstracta que representa las entidades generales
class Entidad(ABC):

    def __init__(self, identificador):
        # Validamos que el identificador no esté vacío
        if not identificador or not identificador.strip():
            raise ValueError("El identificador no puede estar vacío")

        self._identificador = identificador.strip()

    # Método para consultar el identificador
    @property
    def identificador(self):
        return self._identificador

    # Método abstracto que deberán implementar las clases hijas
    @abstractmethod
    def mostrar_informacion(self):
        pass
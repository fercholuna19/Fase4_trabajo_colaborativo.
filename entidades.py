
# Importamos las herramientas para crear clases abstractas
from abc import ABC, abstractmethod


# Clase abstracta que representa las entidades generales
class Entidad(ABC):

    def __init__(self, identificador):

        # Validamos que el identificador sea un texto
        if not isinstance(identificador, str):
            raise TypeError("El identificador debe ser un texto")

        # Validamos que el identificador no esté vacío
        if not identificador.strip():
            raise ValueError("El identificador no puede estar vacío")

        # Guardamos el identificador de forma encapsulada
        self._identificador = identificador.strip()

    # Método para consultar el identificador
    @property
    def identificador(self):
        return self._identificador

    # Método abstracto que deben implementar las clases hijas
    @abstractmethod
    def mostrar_informacion(self):
        pass


# Importamos las herramientas para crear clases abstractas
from abc import ABC, abstractmethod

from excepciones import ErrorServicio

# Clase abstracta que representa los servicios generales
class Servicio(ABC):

    def __init__(self, nombre, tarifa_base):

        # Validamos el nombre del servicio
        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorServicio("El nombre del servicio no puede estar vacío")

        # Validamos la tarifa base
        if isinstance(tarifa_base, bool) or not isinstance(tarifa_base, (int, float)):
            raise TypeError("La tarifa debe ser un valor numérico")

        if tarifa_base <= 0:
            raise ErrorServicio("La tarifa debe ser mayor que cero")

        # Guardamos los datos de forma encapsulada
        self._nombre = nombre.strip()
        self._tarifa_base = tarifa_base

    # Método para consultar el nombre del servicio
    @property
    def nombre(self):
        return self._nombre

    # Método abstracto para calcular el costo
    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    # Método abstracto para describir el servicio
    @abstractmethod
    def describir_servicio(self):
        pass

    # Método abstracto para validar los parámetros
    @abstractmethod
    def validar_parametros(self, duracion):
        pass


# Servicio especializado para reservar salas
class ReservaSala(Servicio):

    def __init__(self, nombre, tarifa_base, capacidad_personas):
        super().__init__(nombre, tarifa_base)

        if isinstance(capacidad_personas, bool) or not isinstance(capacidad_personas, int) or capacidad_personas <= 0:
            raise ErrorServicio("La capacidad debe ser un número entero positivo")

        self.__capacidad_personas = capacidad_personas

    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorServicio("La duración de la reserva debe ser positiva")

        return True

    def calcular_costo(self, duracion):
        self.validar_parametros(duracion)
        return self._tarifa_base * duracion

    def describir_servicio(self):
        return f"Reserva de sala: {self.nombre}. Capacidad: {self.__capacidad_personas} personas."


# Servicio especializado para alquiler de equipos
class AlquilerEquipo(Servicio):

    def __init__(self, nombre, tarifa_base, tipo_equipo):
        super().__init__(nombre, tarifa_base)

        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise ErrorServicio("Debe indicar el tipo de equipo")

        self.__tipo_equipo = tipo_equipo.strip()

    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorServicio("La duración del alquiler debe ser positiva")

        return True

    def calcular_costo(self, duracion):
        self.validar_parametros(duracion)
        return self._tarifa_base * duracion

    def describir_servicio(self):
        return f"Alquiler de equipo: {self.nombre}. Tipo: {self.__tipo_equipo}."


# Servicio especializado para asesorías
class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, tarifa_base, especialidad):
        super().__init__(nombre, tarifa_base)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ErrorServicio("Debe indicar la especialidad de la asesoría")

        self.__especialidad = especialidad.strip()

    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorServicio("La duración de la asesoría debe ser positiva")

        return True

    def calcular_costo(self, duracion):
        self.validar_parametros(duracion)
        return self._tarifa_base * duracion

    def describir_servicio(self):
        return f"Asesoría especializada: {self.nombre}. Especialidad: {self.__especialidad}."

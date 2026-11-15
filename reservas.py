# Importamos las clases necesarias
from clientes import Cliente
from servicios import Servicio


# Clase que representa una reserva
class Reserva:

    def __init__(self, identificador, cliente, servicio, duracion):

        # Validamos el identificador
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador de la reserva no es válido")

        # Validamos que el cliente sea un objeto Cliente
        if not isinstance(cliente, Cliente):
            raise TypeError("La reserva debe estar asociada a un cliente válido")

        # Validamos que el servicio sea un objeto Servicio
        if not isinstance(servicio, Servicio):
            raise TypeError("La reserva debe tener un servicio válido")

        # Validamos la duración
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise TypeError("La duración debe ser un valor numérico")

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero")

        # Guardamos los datos de la reserva
        self.__identificador = identificador.strip()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion

        # Toda reserva comienza pendiente
        self.__estado = "PENDIENTE"

     # Método para consultar el estado de la reserva
    @property
    def estado(self):
        return self.__estado

    # Método para confirmar una reserva
    def confirmar(self):
        if self.__estado != "PENDIENTE":
            raise ValueError("Solo se pueden confirmar reservas pendientes")

        self.__estado = "CONFIRMADA"
        return "Reserva confirmada correctamente"

    # Método para cancelar una reserva
    def cancelar(self):
        if self.__estado != "PENDIENTE":
            raise ValueError("Solo se pueden cancelar reservas pendientes")

        self.__estado = "CANCELADA"
        return "Reserva cancelada correctamente"

    # Método para procesar una reserva
    def procesar(self):

        # Verificamos que la reserva esté confirmada
        if self.__estado != "CONFIRMADA":
            raise ValueError("Solo se pueden procesar reservas confirmadas")

        try:
            # Calculamos el costo según el servicio seleccionado
            costo = self.__servicio.calcular_costo(self.__duracion)

        except (ValueError, TypeError) as error:
            raise RuntimeError("No fue posible procesar la reserva") from error

        else:
            # Si no ocurre ningún error, actualizamos el estado
            self.__estado = "PROCESADA"
            return costo

        finally:
            # Este mensaje se ejecuta haya ocurrido un error o no
            print("Finalizó el intento de procesamiento de la reserva")
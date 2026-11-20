# Importamos las clases necesarias
from clientes import Cliente
from servicios import Servicio
from excepciones import ErrorReserva
from registro_errores import registrar_error


# Clase que representa una reserva
class Reserva:

    def __init__(self, identificador, cliente, servicio, duracion):

        # Validamos el identificador
        if not isinstance(identificador, str) or not identificador.strip():
            raise ErrorReserva("El identificador de la reserva no es válido")

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
            raise ErrorReserva("La duración debe ser mayor que cero")

        # Guardamos los datos de la reserva
        self.__identificador = identificador.strip()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion

        # Toda reserva comienza pendiente
        self.__estado = "PENDIENTE"

    # Método para consultar el estado de la reserva
    @property
    def identificador(self):
        return self.__identificador

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    # Método para confirmar una reserva
    def confirmar(self):
        if self.__estado != "PENDIENTE":
            mensaje = "Solo se pueden confirmar reservas pendientes"
            registrar_error(mensaje)
            raise ErrorReserva(mensaje)

        self.__estado = "CONFIRMADA"
        return "Reserva confirmada correctamente"

    # Método para cancelar una reserva
    def cancelar(self):
        if self.__estado != "PENDIENTE":
            mensaje = "Solo se pueden cancelar reservas pendientes"
            registrar_error(mensaje)
            raise ErrorReserva(mensaje)

        self.__estado = "CANCELADA"
        return "Reserva cancelada correctamente"

    # Método para procesar una reserva
    def procesar(self):

        # Verificamos que la reserva esté confirmada
        if self.__estado != "CONFIRMADA":
            mensaje = "Solo se pueden procesar reservas confirmadas"
            registrar_error(mensaje)
            raise ErrorReserva(mensaje)

        try:
            # Calculamos el costo según el servicio seleccionado
            costo = self.__servicio.calcular_costo(self.__duracion)

        except (ValueError, TypeError) as error:
            registrar_error(f"Error al procesar la reserva: {error}")
            raise ErrorReserva("No fue posible procesar la reserva") from error

        else:
            # Si no ocurre ningún error, actualizamos el estado
            self.__estado = "PROCESADA"
            return costo

        finally:
            # Este mensaje se ejecuta haya ocurrido un error o no
            print("Finalizó el intento de procesamiento de la reserva")
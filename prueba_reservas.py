# Importamos las clases necesarias
from clientes import Cliente
from servicios import ReservaSala
from reservas import Reserva
from excepciones import ErrorReserva


# Creamos un cliente
cliente = Cliente(
    "C003",
    "Juan Pérez",
    "juan@gmail.com",
    "3101234567"
)

# Creamos un servicio
servicio = ReservaSala("Sala principal", 50000, 20)

# Creamos una reserva
reserva = Reserva("R001", cliente, servicio, 2)

try:
    print("Estado inicial:", reserva.estado)

    print(reserva.confirmar())
    print("Estado actual:", reserva.estado)

    costo = reserva.procesar()
    print("Costo de la reserva:", costo)
    print("Estado final:", reserva.estado)

except (ValueError, TypeError, RuntimeError) as error:
    print("Error durante la reserva:", error)

# Probamos una reserva que no ha sido confirmada
print("\n--- PRUEBA DE RESERVA PENDIENTE ---")

try:
    reserva2 = Reserva("R002", cliente, servicio, 3)

    print("Estado inicial:", reserva2.estado)

    # Intentamos procesar sin confirmar
    reserva2.procesar()

except ErrorReserva as error:
    print("Se detectó el error correctamente:", error)


# Probamos la cancelación de la reserva
print("\n--- PRUEBA DE CANCELACIÓN ---")

try:
    print(reserva2.cancelar())
    print("Estado final:", reserva2.estado)

except ErrorReserva as error:
    print("Error al cancelar:", error)

# Intentamos confirmar una reserva cancelada
print("\n--- PRUEBA DE RESERVA CANCELADA ---")

try:
    reserva2.confirmar()

except ErrorReserva as error:
    print("No se permite confirmar:", error)


# Intentamos procesar una reserva cancelada
try:
    reserva2.procesar()

except ErrorReserva as error:
    print("No se permite procesar:", error)

    
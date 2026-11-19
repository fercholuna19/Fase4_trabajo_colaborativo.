# SISTEMA INTEGRAL SOFTWARE FJ

from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from registro_errores import registrar_error


clientes = []
servicios = [
    ReservaSala("Sala de reuniones", 50000, 20),
    AlquilerEquipo("Proyector", 30000, "Equipo audiovisual"),
    AsesoriaEspecializada("Asesoría técnica", 80000, "Sistemas"),
]
reservas = []


def pedir_numero(mensaje):
    """Solicita un número y muestra un error claro si la entrada no es válida."""
    try:
        return float(input(mensaje))
    except ValueError as error:
        registrar_error(f"Entrada numérica inválida: {error}")
        raise ValueError("Debes ingresar un número válido.") from error


def mostrar_menu():
    print("\n====================================")
    print("       SISTEMA SOFTWARE FJ")
    print("====================================")
    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Mostrar servicios")
    print("4. Crear reserva")
    print("5. Mostrar reservas")
    print("6. Salir")
    print("====================================")


def registrar_cliente():
    try:
        identificador = input("Identificador: ")
        nombre = input("Nombre: ")
        correo = input("Correo electrónico: ")
        telefono = input("Teléfono: ")

        cliente = Cliente(identificador, nombre, correo, telefono)
        clientes.append(cliente)
        print("Cliente registrado correctamente.")

    except (ValueError, TypeError) as error:
        registrar_error(f"Error al registrar cliente: {error}")
        print(f"No se pudo registrar el cliente: {error}")


def mostrar_clientes():
    if not clientes:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print("\n" + cliente.mostrar_informacion())


def mostrar_servicios():
    for indice, servicio in enumerate(servicios, start=1):
        print(f"\n{indice}. {servicio.describir_servicio()}")


def crear_reserva():
    if not clientes:
        print("Primero debes registrar un cliente.")
        return

    try:
        mostrar_clientes()
        numero_cliente = int(input("Número de cliente (empezando por 1): "))
        if numero_cliente < 1 or numero_cliente > len(clientes):
            raise ValueError("El número de cliente no existe.")

        mostrar_servicios()
        numero_servicio = int(input("Número de servicio (empezando por 1): "))
        if numero_servicio < 1 or numero_servicio > len(servicios):
            raise ValueError("El número de servicio no existe.")

        duracion = pedir_numero("Duración en horas: ")
        identificador = input("Identificador de la reserva: ")

        reserva = Reserva(
            identificador,
            clientes[numero_cliente - 1],
            servicios[numero_servicio - 1],
            duracion,
        )
        reservas.append(reserva)

        print(reserva.confirmar())
        costo = reserva.procesar()
        print(f"Reserva procesada. Costo: ${costo:,.2f}")

    except (ValueError, TypeError, RuntimeError) as error:
        registrar_error(f"Error al crear reserva: {error}")
        print(f"No se pudo crear la reserva: {error}")


def mostrar_reservas():
    if not reservas:
        print("No hay reservas registradas.")
        return

    for reserva in reservas:
        print(f"Estado: {reserva.estado}")


def main():
    print("Bienvenido al Sistema Software FJ")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            mostrar_servicios()
        elif opcion == "4":
            crear_reserva()
        elif opcion == "5":
            mostrar_reservas()
        elif opcion == "6":
            print("Gracias por utilizar Software FJ.")
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")


if __name__ == "__main__":
    main()
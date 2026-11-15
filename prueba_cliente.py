
# Importamos la clase Cliente
from clientes import Cliente

# Creamos un cliente con datos válidos
try:
    cliente1 = Cliente(
        "C001",
        "Carlos Pérez",
        "carlos@gmail.com",
        "3124567890"
    )

    print("CLIENTE REGISTRADO CORRECTAMENTE")
    print(cliente1.mostrar_informacion())

except (ValueError, TypeError) as error:
    print("Error al registrar el cliente:", error)


# Probamos un registro con datos incorrectos
try:
    cliente2 = Cliente(
        "C002",
        "",
        "correo_invalido",
        "3124567890"
    )

except (ValueError, TypeError) as error:
    print("Se detectó un registro incorrecto:", error)

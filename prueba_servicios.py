
# Importamos las clases de servicios
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada

from excepciones import ErrorServicio

# Creamos una lista con diferentes servicios
servicios = [
    ReservaSala("Sala de reuniones", 50000, 20),
    AlquilerEquipo("Proyector", 30000, "Equipo audiovisual"),
    AsesoriaEspecializada("Asesoría técnica", 80000, "Sistemas")
]

# Recorremos los servicios y mostramos su información
for servicio in servicios:
    try:
        print(servicio.describir_servicio())
        print("Costo por 2 horas:", servicio.calcular_costo(2))
        print("-----------------------------------")

    except (ValueError, TypeError) as error:
        print("Error al procesar el servicio:", error)


# Probamos un servicio con datos incorrectos
print("\n--- PRUEBA DE ERROR PERSONALIZADO ---")

try:
    servicio_error = ReservaSala("Sala de prueba", 50000, 0)

except ErrorServicio as error:
    print("Se detectó el error personalizado:", error)
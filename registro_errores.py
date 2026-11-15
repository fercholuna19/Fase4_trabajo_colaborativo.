# Importamos la herramienta para registrar errores
import logging


# Configuramos el registro de errores
logging.basicConfig(
    filename="registro.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Función para guardar los errores del sistema
def registrar_error(mensaje):
    logging.error(mensaje)


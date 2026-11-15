
# Importamos la clase abstracta Entidad
from entidades import Entidad


# Clase Cliente que hereda de Entidad
class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo, telefono):

        # Inicializamos los datos de la clase padre
        super().__init__(identificador)

        # Validamos el nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del cliente no puede estar vacío")

        # Validamos el correo electrónico
        if not isinstance(correo, str) or "@" not in correo or "." not in correo:
            raise ValueError("El correo electrónico no es válido")

        # Validamos el teléfono
        if not isinstance(telefono, str) or not telefono.strip():
            raise ValueError("El teléfono no puede estar vacío")

        # Guardamos los datos personales de forma encapsulada
        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = telefono.strip()

    # Método para mostrar la información del cliente
    def mostrar_informacion(self):
        return (
            f"Identificador: {self.identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )

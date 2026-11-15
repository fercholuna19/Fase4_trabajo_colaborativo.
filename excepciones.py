# Clase base para los errores del sistema
class ErrorSistema(Exception):
    pass


# Error cuando los datos del cliente no son válidos
class ErrorCliente(ErrorSistema, ValueError):
    pass


# Error cuando los datos del servicio no son válidos
class ErrorServicio(ErrorSistema, ValueError):
    pass


# Error cuando ocurre un problema con una reserva
class ErrorReserva(ErrorSistema, ValueError):
    pass
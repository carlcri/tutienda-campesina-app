# # Importar las instancias 'router' de los módulos individuales
# # Esto hace que 'root_router', 'students_router', y 'clients_router'
# # sean directamente accesibles cuando se importa 'api.v1.endpoints'.
# from .root import router as root_router
# from .students import router as students_router


# # Definir __all__ para especificar qué se exporta cuando se usa 'from ... import *'
# # Esto también ayuda a las herramientas de análisis estático como Pylance a entender
# # qué símbolos están disponibles en este paquete.
# __all__ = ["root_router", "students_router"]
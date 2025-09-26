"""
Models Package - Modelo de datos y lógica de negocio
Contiene las entidades, servicios y consultas de la aplicación CRUD
"""

# Importaciones principales del modelo
from .Empleado import Empleado
from .Consulta import Consulta
from .Servicio import Servicio
from .Mensaje import Mensaje

# Exponer las clases principales
__all__ = [
    'Empleado',
    'Consulta', 
    'Servicio',
    'Mensaje'
]

# Información del paquete
__version__ = '2.0'
__author__ = 'Tu Nombre'
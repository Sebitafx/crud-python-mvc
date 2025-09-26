"""
Configuración de la aplicación CRUD
Constantes y configuraciones centralizadas
"""

# Información de la aplicación
APP_NAME = "CRUD Python - Gestión de Empleados"
APP_VERSION = "2.0"
APP_AUTHOR = "Tu Nombre"

# Configuración de la ventana principal
WINDOW_TITLE = "APLICACION CRUD CON BASE DE DATOS"
WINDOW_SIZE = "600x350"
WINDOW_BG_COLOR = "lightblue"

# Configuración de la base de datos
DB_NAME = "base"

# Rutas de recursos
ASSETS_PATH = "assets"
IMAGES_PATH = "assets/imagenes"

# Configuración de la tabla
TABLE_HEADERS = ["ID", "Nombre del Empleado", "Cargo", "Salario"]
TABLE_HEIGHT = 10

# Colores de botones
BUTTON_COLORS = {
    'buscar': 'orange',
    'crear': 'green',
    'actualizar': 'orange',
    'mostrar': 'orange',
    'eliminar': 'red'
}
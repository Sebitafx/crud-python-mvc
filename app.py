
"""CRUD Python - Aplicación de Gestión de Empleados
Aplicación CRUD desarrollada en Python siguiendo el patrón MVC"""

import sys
import os

# Agregar el directorio actual al path para imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from views import MainWindow

def main():
    """Función principal de la aplicación"""
    try:
        print("🚀 Iniciando aplicación CRUD...")
        app = MainWindow()
        app.run()
        print("✅ Aplicación cerrada correctamente")
    except Exception as e:
        print(f"❌ Error al ejecutar la aplicación: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
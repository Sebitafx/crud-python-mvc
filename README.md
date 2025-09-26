# 🚀 CRUD Python - Sistema de Gestión de Empleados

Una aplicación CRUD (Create, Read, Update, Delete) desarrollada en Python siguiendo el patrón arquitectónico **MVC (Modelo-Vista-Controlador)** con interfaz gráfica usando Tkinter.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite-green.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)
![MVC](https://img.shields.io/badge/Pattern-MVC-purple.svg)

## 🏗️ Arquitectura del Proyecto

```
CRUD Python/
├── app.py                  # 🚀 Punto de entrada principal
├── assets/                 # 📁 Recursos estáticos
│   └── imagenes/          
│       ├── actualizar.png
│       ├── buscar.png
│       ├── crear.png
│       ├── eliminar.png
│       └── mostrar.png
├── models/                 # 📊 Modelo (Datos y lógica de negocio)
│   ├── __init__.py
│   ├── Empleado.py        # Entidad Empleado
│   ├── Consulta.py        # Consultas SQL
│   ├── Servicio.py        # Capa de acceso a datos
│   └── Mensaje.py         # Mensajes del sistema
├── views/                  # 🖥️ Vista (Interfaz de usuario)
│   ├── __init__.py
│   └── main_window.py     # Ventana principal
├── controllers/            # 🎮 Controlador (Lógica de control)
│   ├── __init__.py
│   └── Gestor.py          # Gestor principal
└── base                   # 🗄️ Base de datos SQLite
```

## 🚀 Cómo ejecutar

```bash
python app.py
```

## ✨ Funcionalidades

- ✅ **Crear** empleados
- ✅ **Leer/Consultar** empleados
- ✅ **Actualizar** información de empleados
- ✅ **Eliminar** empleados
- ✅ **Buscar** empleados por nombre
- ✅ **Gestión de base de datos** SQLite
- ✅ **Interfaz gráfica** intuitiva con iconos

## 🛠️ Tecnologías

- **Python 3.x**
- **Tkinter** (Interfaz gráfica)
- **SQLite** (Base de datos)
- **Patrón MVC** (Arquitectura)

## 📋 Estructura de la Base de Datos

```sql
CREATE TABLE empleado (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE VARCHAR(50) NOT NULL,
    CARGO VARCHAR(50) NOT NULL,
    SALARIO INT NOT NULL
)
```

## � Instalación y Ejecución

### Prerrequisitos
- Python 3.8 o superior
- No se requieren dependencias externas

### Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/crud-python-mvc.git
cd crud-python-mvc
```

### Ejecutar la aplicación
```bash
python app.py
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## �👤 Autor

Desarrollado siguiendo las mejores prácticas de programación orientada a objetos y patrones de diseño.

---
⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub!
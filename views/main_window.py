"""
MainWindow - Ventana principal de la aplicación CRUD
Contiene la interfaz gráfica principal y la lógica de eventos
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tkinter import *
from tkinter import ttk, messagebox
from models import Mensaje
from controllers import Gestor


class MainWindow:
    """Clase principal de la ventana de la aplicación CRUD"""
    
    def __init__(self):
        """Inicializar la ventana principal"""
        self.root = None
        self.tree = None
        
        # Variables de los campos
        self.miId = None
        self.miNombre = None
        self.miCargo = None
        self.miSalario = None
        
        # Variables para imágenes
        self.imagenes = {}
        
        self._setup_window()
        self._setup_variables()
        self._load_images()
        self._create_widgets()
        
    def _setup_window(self):
        """Configurar la ventana principal"""
        self.root = Tk()
        self.root.title("APLICACION CRUD CON BASE DE DATOS")
        self.root.configure(background='lightblue')
        self.root.geometry("600x350")
        
    def _setup_variables(self):
        """Configurar las variables de los campos"""
        self.miId = StringVar()
        self.miNombre = StringVar()
        self.miCargo = StringVar()
        self.miSalario = StringVar()
        
    def _load_images(self):
        """Cargar las imágenes de los iconos"""
        try:
            self.imagenes = {
                'buscar': PhotoImage(file="assets/imagenes/buscar.png"),
                'crear': PhotoImage(file="assets/imagenes/crear.png"),
                'mostrar': PhotoImage(file="assets/imagenes/mostrar.png"),
                'actualizar': PhotoImage(file="assets/imagenes/actualizar.png"),
                'eliminar': PhotoImage(file="assets/imagenes/eliminar.png")
            }
        except Exception as e:
            print(f"Error cargando imágenes: {e}")
            # Crear diccionario vacío si no se pueden cargar las imágenes
            self.imagenes = {key: None for key in ['buscar', 'crear', 'mostrar', 'actualizar', 'eliminar']}
    
    def _create_widgets(self):
        """Crear todos los widgets de la interfaz"""
        self._create_menu()
        self._create_form()
        self._create_table()
        self._create_buttons()
        
        # Mostrar datos iniciales
        self.mostrar()
        
    def _create_menu(self):
        """Crear la barra de menú"""
        menubar = Menu(self.root)
        
        # Menú Base de Datos
        menubasedat = Menu(menubar, tearoff=0)
        menubasedat.add_command(label="Crear/Conectar Base de Datos", command=self.conexionBBDD)
        menubasedat.add_command(label="Eliminar Base de Datos", command=self.eliminarBBDD)
        menubasedat.add_command(label="Salir", command=self.salirAplicacion)
        menubar.add_cascade(label="Inicio", menu=menubasedat)
        
        # Menú Ayuda
        ayudamenu = Menu(menubar, tearoff=0)
        ayudamenu.add_command(label="Resetear Campos", command=self.limpiarCampos)
        ayudamenu.add_command(label="Acerca", command=Gestor.mensaje)
        menubar.add_cascade(label="Ayuda", menu=ayudamenu)
        
        self.root.config(menu=menubar)
        
    def _create_form(self):
        """Crear el formulario de entrada de datos"""
        # Campo oculto ID
        self.e1 = Entry(self.root, textvariable=self.miId)
        
        # Nombre
        Label(self.root, text="Nombre", background='lightblue').place(x=50, y=10)
        Entry(self.root, textvariable=self.miNombre, width=50).place(x=100, y=10)
        
        # Cargo
        Label(self.root, text="Cargo", background='lightblue').place(x=50, y=40)
        Entry(self.root, textvariable=self.miCargo).place(x=100, y=40)
        
        # Salario
        Label(self.root, text="Salario", background='lightblue').place(x=280, y=40)
        Entry(self.root, textvariable=self.miSalario, width=10).place(x=320, y=40)
        Label(self.root, text="USD", background='lightblue').place(x=380, y=40)
        
    def _create_table(self):
        """Crear la tabla de empleados"""
        cabecera = ["ID", "Nombre del Empleado", "Cargo", "Salario"]
        
        self.tree = ttk.Treeview(height=10, columns=('#0', '#1', '#2'))
        self.tree.place(x=0, y=130)
        self.tree.column('#0', width=100)
        self.tree.heading('#0', text=cabecera[0], anchor=CENTER)
        self.tree.heading('#1', text=cabecera[1], anchor=CENTER)
        self.tree.heading('#2', text=cabecera[2], anchor=CENTER)
        self.tree.column('#3', width=100)
        self.tree.heading('#3', text=cabecera[3], anchor=CENTER)
        self.tree.bind("<Button-1>", self.seleccionarUsandoClick)
        
    def _create_buttons(self):
        """Crear los botones de la interfaz"""
        Button(self.root, text="Buscar Registro", 
               image=self.imagenes['buscar'], bg="orange", 
               command=self.buscar).place(x=450, y=10)
               
        Button(self.root, text="Crear Registro", 
               image=self.imagenes['crear'], bg="green", 
               command=self.crear).place(x=50, y=85)
               
        Button(self.root, text="Actualizar Registro", 
               image=self.imagenes['actualizar'], bg="orange", 
               command=self.actualizar).place(x=180, y=85)
               
        Button(self.root, text="Mostrar Lista", 
               image=self.imagenes['mostrar'], bg="orange", 
               command=self.mostrar).place(x=320, y=85)
               
        Button(self.root, text="Eliminar Registro", 
               image=self.imagenes['eliminar'], bg="red", 
               command=self.borrar).place(x=450, y=85)
    
    # ==================== MÉTODOS DE GESTIÓN BD ====================
    
    def conexionBBDD(self):
        """Conectar/crear base de datos"""
        Gestor.conexionBBDD()

    def eliminarBBDD(self):
        """Eliminar base de datos"""
        Gestor.eliminarBBDD()
        self.limpiarMostrar()

    def limpiarMostrar(self):
        """Limpiar campos y mostrar datos"""
        self.limpiarCampos()
        self.mostrar()

    def limpiarCampos(self):
        """Limpiar todos los campos del formulario"""
        self.miId.set("")
        self.miNombre.set("")
        self.miCargo.set("")
        self.miSalario.set("")

    def mostrar(self):
        """Mostrar todos los empleados en la tabla"""
        Gestor.mostrar(self.tree)

    def salirAplicacion(self):
        """Salir de la aplicación"""
        valor = messagebox.askquestion("Salir", Mensaje.SALIR)
        if valor == "yes":
            self.root.destroy()
    
    # ==================== MÉTODOS CRUD ====================
    
    def crear(self):
        """Crear nuevo empleado"""
        Gestor.crear(self.miNombre.get(), self.miCargo.get(), self.miSalario.get())
        self.limpiarMostrar()

    def actualizar(self):
        """Actualizar empleado existente"""
        Gestor.actualizar(self.miNombre.get(), self.miCargo.get(), 
                         self.miSalario.get(), self.miId.get())
        self.limpiarMostrar()

    def borrar(self):
        """Eliminar empleado"""
        Gestor.borrar(self.miId.get())
        self.limpiarMostrar()

    def buscar(self):
        """Buscar empleados por nombre"""
        Gestor.buscar(self.tree, self.miNombre.get())

    def seleccionarUsandoClick(self, event):
        """Seleccionar empleado haciendo clic en la tabla"""
        item = self.tree.identify('item', event.x, event.y)
        if item:
            self.miId.set(self.tree.item(item, "text"))
            values = self.tree.item(item, "values")
            if len(values) >= 3:
                self.miNombre.set(values[0])
                self.miCargo.set(values[1])
                self.miSalario.set(values[2])
    
    # ==================== MÉTODO PRINCIPAL ====================
    
    def run(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()
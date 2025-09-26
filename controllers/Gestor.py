import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tkinter import messagebox
from models import Servicio, Mensaje

class Gestor:

	def conexionBBDD():
		try:
			Servicio.conexionBBDD()
			messagebox.showinfo("CONEXION",Mensaje.EXITO_BD)
		except:
			messagebox.showinfo("CONEXION", Mensaje.ERROR_BD)

	def eliminarBBDD():
		if messagebox.askyesno(message=Mensaje.CONFIRMAR_BD, title="ADVERTENCIA"):
			Servicio.eliminarBBDD()
		else:
			messagebox.showinfo("CONEXION", Mensaje.ERROR_ELIMINAR_BD)


	def mostrar(tree):
		registros=tree.get_children()
		[tree.delete(elemento) for elemento in registros]
		try:
			empleados = Servicio.consultar()
			[tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3])) for row in empleados]
		except:
			messagebox.showwarning("ADVERTENCIA",Mensaje.ERROR_MOSTRAR)

	def buscar(tree, criterio):
		registros=tree.get_children()
		[tree.delete(elemento) for elemento in registros]
		try:
			if(criterio!=""):
				empleados = Servicio.buscar(criterio)
				[tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3])) for row in empleados]
			else:
				messagebox.showwarning("ADVERTENCIA",Mensaje.NOMBRE_FALTANTE)
		except:
			messagebox.showwarning("ADVERTENCIA",Mensaje.ERROR_BUSCAR)

	def crear(nombre,cargo,salario):
		try:
			if(nombre!="" and cargo!="" and salario!=""):
				Servicio.crear(nombre,cargo,salario)
			else:
				messagebox.showwarning("ADVERTENCIA",Mensaje.CAMPOS_FALTANTES)
		except:
			messagebox.showwarning("ADVERTENCIA",Mensaje.ERROR_CREAR)

	def actualizar(nombre,cargo,salario,ide):
		try:
			if(nombre!="" and cargo!="" and salario!=""):
				Servicio.actualizar(nombre,cargo,salario,ide)
			else:
				messagebox.showwarning("ADVERTENCIA",Mensaje.CAMPOS_FALTANTES)
		except:
			messagebox.showwarning("ADVERTENCIA",Mensaje.ERROR_ACTUALIZAR)

	def borrar(ide):
		try:
			if messagebox.askyesno(message=Mensaje.CONFIRMAR, title="ADVERTENCIA"):
				Servicio.borrar(ide)
		except:
			messagebox.showwarning("ADVERTENCIA",Mensaje.ERROR_ELIMINAR)


	def mensaje():
		messagebox.showinfo(title="INFORMACION", message=Mensaje.ACERCA)

import sqlite3
from .Consulta import *
from .Empleado import *

class Servicio:

	def conectar():
		miConexion=sqlite3.connect("base")
		miCursor=miConexion.cursor()
		return miConexion,miCursor

	def conexionBBDD():
		miConexion,miCursor=Servicio.conectar()
		miCursor.execute(Consulta.CREATE)

	def eliminarBBDD():
		miConexion,miCursor=Servicio.conectar()
		miCursor.execute(Consulta.DELETE_TABLE)

	def consultar():
		miConexion,miCursor=Servicio.conectar()
		miCursor.execute(Consulta.SELECT)
		return miCursor.fetchall()

	def crear(nombre,cargo,salario):
		miConexion,miCursor=Servicio.conectar()
		empleado=Empleado(nombre,cargo,salario)
		miCursor.execute(Consulta.INSERT, (empleado.info()))
		miConexion.commit()

	def actualizar(nombre,cargo,salario,ide):
		miConexion,miCursor=Servicio.conectar()
		empleado=Empleado(nombre,cargo,salario)
		miCursor.execute(Consulta.UPDATE+ide, (empleado.info()))
		miConexion.commit()

	def borrar(ide):
		miConexion,miCursor=Servicio.conectar()
		miCursor.execute(Consulta.DELETE+ide)
		miConexion.commit()

	def buscar(nombre):
		miConexion,miCursor=Servicio.conectar()
		miCursor.execute(Consulta.BUSCAR, (nombre,))
		return miCursor.fetchall()



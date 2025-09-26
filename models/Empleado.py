class Empleado:

	#constructor
	def __init__(self,nombre,cargo,salario):
		self.__nombre=nombre
		self.__cargo=cargo
		self.__salario=salario

	def info(self):
		return self.__nombre,self.__cargo,self.__salario


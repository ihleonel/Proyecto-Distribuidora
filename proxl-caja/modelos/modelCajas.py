# -*- coding: utf-8 -*-
from db_conn import DBConn

class ModeloCajas:
	def __init__(self):
		self.ccam_anio = 0
		self.ccam_num  = 0
		self.caj_numero = 0
		self.caj_fecha = ""
		self.caj_estado = 0 # 1: Abierta 2: Cerrada
		self.caj_inicial = 0.0
		self.db = DBConn()

	def create(self):
		query = "Call agregarCaja(%s, %s, %s, %s, %s)"
		values = (self.ccam_anio, self.ccam_num, self.caj_numero, self.caj_fecha, self.caj_inicial)
		return self.db.ejecutar(query, values)
		
	def update(self):
		pass

	def delete(self):
		pass

	def close(self):
		query = "CALL cerrarCaja(%s, %s, %s)"
		values = (self.ccam_anio, self.ccam_num, self.caj_numero)
		return self.db.ejecutar(query, values)

	def get_box_active(self):
		query = "SELECT * FROM cajas WHERE caj_estado = 1;"
		tabla = self.db.ejecutar(query)
		resultado = {}
		if tabla != ():
			resultado['campAnio'] = tabla[0][0]
			resultado['campNum'] = tabla[0][1]
			resultado['numero'] = tabla[0][2]
			resultado['fecha'] = tabla[0][3]
			resultado['estado'] = tabla[0][4]
			resultado['monto'] = tabla[0][5]
		return resultado

	def read(self):
		query = "SELECT * FROM cajas WHERE ccam_anio = %s AND ccam_num = %s AND caj_numero = %s;"
		values = (self.ccam_anio, self.ccam_num, self.caj_numero)
		tabla = self.db.ejecutar(query, values)
		resultado = {}
		if tabla != ():
			resultado['campAnio'] = tabla[0][0]
			resultado['campNum'] = tabla[0][1]
			resultado['numero'] = tabla[0][2]
			resultado['fecha'] = tabla[0][3]
			resultado['estado'] = tabla[0][4]
			resultado['monto'] = tabla[0][5]
		return resultado

	def count_boxes(self):
		query = "SELECT cantidadCajas(%s, %s);"
		values = (self.ccam_anio, self.ccam_num)
		return self.db.ejecutar(query, values)[0][0]

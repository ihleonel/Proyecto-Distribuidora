# -*- coding: utf-8 -*-
from db_conn import DBConn

class ModeloGastosVarios:

	def __init__(self):
		self.icam_anio = 0
		self.icam_num = 0
		self.i_numero = 0
		self.i_fecha = ""
		self.i_monto = 0.0
		self.i_concepto = ""
		self.db = DBConn()

	def create(self):
		query = "Call agregarImprevisto(%s, %s, %s, %s, %s, %s)"
		values = (self.icam_anio, self.icam_num, self.i_numero, self.i_fecha, self.i_monto, self.i_concepto)
		return self.db.ejecutar(query, values)

	def update(self):
		query = "Call modificarImprevisto(%s, %s, %s, %s, %s, %s)"
		values = (self.icam_anio, self.icam_num, self.i_numero, self.i_fecha, self.i_monto, self.i_concepto)
		return self.db.ejecutar(query, values)

	def delete(self):
		query = "Call eliminarImprevisto(%s, %s, %s)"
		values = (self.icam_anio, self.icam_num, self.i_numero)
		return self.db.ejecutar(query, values)

	def read_all(self):
		query = "SELECT * FROM imprevistos WHERE icam_anio = %s AND icam_num = %s;"
		values = (self.icam_anio, self.icam_num)
		return self.db.ejecutar(query, values)

	def last_spending(self):
		query = "SELECT ultimoImprevisto(%s, %s)"
		values = (self.icam_anio, self.icam_num)
		return self.db.ejecutar(query, values)[0][0]
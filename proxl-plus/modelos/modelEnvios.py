# -*- coding: utf-8 -*-
from db_conn import DBConn

class ModeloEnvios:

	def __init__(self):
		self.ecam_anio = 0
		self.ecam_num = 0
		self.env_num = 0
		self.env_fecha = "0000-00-00"
		self.env_monto = 0.0
		self.db = DBConn()

	def create(self):
		query = "CALL agregarEnvio(%s, %s, %s, %s, %s)"
		values = (self.ecam_anio, self.ecam_num, self.env_num, self.env_fecha, self.env_monto)
		return self.db.ejecutar(query, values)

	def update(self):
		query = "CALL modificarEnvio(%s, %s, %s, %s, %s)"
		values = (self.ecam_anio, self.ecam_num, self.env_num, self.env_fecha, self.env_monto)
		return self.db.ejecutar(query, values)

	def delete(self):
		query = "CALL eliminarEnvio(%s, %s, %s)"
		values = (self.ecam_anio, self.ecam_num, self.env_num)
		return self.db.ejecutar(query, values)

	def read_all(self):
		query = "SELECT * FROM envios WHERE ecam_anio = %s AND ecam_num = %s"
		values = (self.ecam_anio, self.ecam_num)
		return self.db.ejecutar(query, values)

	def last_deposit(self):
		query = "SELECT ultimoDeposito(%s, %s);"
		values = (self.ecam_anio, self.ecam_num)
		return self.db.ejecutar(query, values)[0][0]
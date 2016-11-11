# -*- coding : utf-8 -*-
from db_conn import DBConn
class ModeloTiposUsuario:
	def __init__(self):
		self.tipo = ""
		self.descripcion = ""
		self.estado = 1
		self.db = DBConn()

	def read(self):
		query = "SELECT * FROM tipos_usuario WHERE tusu_tipo = %s AND tusu_estado = 1"
		value = (self.tipo)
		dato = self.db.ejecutar(query, value)
		resp = {'tipo': dato[0][0], 
				'descripcion': dato[0][1], 
				'estado': dato[0][2]}
		return resp

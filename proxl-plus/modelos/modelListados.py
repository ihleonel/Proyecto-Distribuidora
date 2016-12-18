# -*- coding: utf-8 -*-
from db_conn import DBConn

class ModeloListados:

	def __init__(self):
		self.cam_anio = 0 # 4 digitos
		self.cam_num = 0 # 4 digitos
		self.numero = 0 # 4 digitos
		self.fecha = ''
		self.comentario = ''
		self.db = DBConn()

	def create(self):
		query = "CALL agregarListado(%s, %s, %s, %s, %s)"
		values = (self.cam_anio, self.cam_num, self.numero, self.fecha, self.comentario)
		return self.db.ejecutar(query, values)

	def update(self):
		query = "CALL actualizarListado(%s, %s, %s, %s)"
		values = (self.cam_anio, self.cam_num, self.numero, self.comentario)
		return self.db.ejecutar(query, values)

	def delete(self):
		query = "CALL eliminarListado(%s, %s, %s)"
		values = (self.cam_anio, self.cam_num, self.numero)
		return self.db.ejecutar(query, values)

	def read(self):
		query = "SELECT * FROM listados WHERE lcam_anio = %s AND lcam_num = %s AND lis_numero = %s"
		values = (self.cam_anio, self.cam_num, self.numero)
		tabla = self.db.ejecutar(query, values)
		if tabla:
			listado = {'numero': tabla[0][2], 
					'fecha': self.date_format(tabla[0][3]), 
					'comentario': tabla[0][4]}
		else:
			listado = None
		return listado

	def read_all(self):
		query = "SELECT * FROM listados WHERE lcam_anio = %s AND lcam_num = %s"
		values = (self.cam_anio, self.cam_num)
		return self.db.ejecutar(query, values)

	def count_list(self):
		query = 'SELECT cantidadListados(%s, %s)'
		values = (self.cam_anio, self.cam_num)
		cant = self.db.ejecutar(query, values)
		return cant[0][0]

	def date_format(self, s):
		s = str(s)
		l = s.split("-")
		l[0], l[2] = l[2], l[0]
		return "-".join(l)
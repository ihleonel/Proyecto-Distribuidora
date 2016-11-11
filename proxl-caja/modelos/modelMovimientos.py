# -*- coding: utf-8 -*-
from db_conn import DBConn

class ModeloMovimientos:
	def __init__(self):
		self.mcam_anio = 0
		self.mcam_num = 0
		self.mcaj_numero = 0
		self.mov_numero = 0
		self.mov_monto = 0.0
		self.mov_tipo = 0 #1:ingresos varios; 2:egresos varios
		self.mov_comentario = ""
		self.db = DBConn()


	def create(self):
		query = "CALL agregarMovimiento(%s, %s, %s, %s, %s, %s, %s);"
		values = (self.mcam_anio, self.mcam_num, self.mcaj_numero, self.mov_numero, self.mov_monto, self.mov_tipo, self.mov_comentario)
		return self.db.ejecutar(query, values)

	def read_all(self):
		query = "SELECT * FROM movimientos WHERE mcam_anio = %s AND mcam_num = %s AND mcaj_numero = %s;"
		values = (self.mcam_anio, self.mcam_num, self.mcaj_numero)
		tabla = self.db.ejecutar(query, values)
		resultados = []
		for fila in tabla:
			resultado = {}
			resultado['monto']= str(fila[4])
			if fila[5] == 1:
				resultado['tipo']= 'Igresos Varios'
			elif fila[5] == 2:
				resultado['tipo']= 'Egresos Varios'
			else:
				resultado['tipo']= 'Ups!'
			resultado['comentario']=str(fila[6])

			resultados.append(resultado)

		return resultados

	def get_income(self):
		query = "SELECT mov_comentario, mov_monto FROM movimientos\
				WHERE mcam_anio = %s AND mcam_num = %s AND mcaj_numero = %s AND mov_tipo = 1;"
		values = (self.mcam_anio, self.mcam_num, self.mcaj_numero)
		return self.db.ejecutar(query, values)

	def get_expenses(self):
		query = "SELECT mov_comentario, mov_monto FROM movimientos\
				WHERE mcam_anio = %s AND mcam_num = %s AND mcaj_numero = %s AND mov_tipo = 2;"
		values = (self.mcam_anio, self.mcam_num, self.mcaj_numero)
		return self.db.ejecutar(query, values)

	def count_movs(self):
		query = "SELECT cantidadMovimientos(%s, %s, %s);"
		values = (self.mcam_anio, self.mcam_num, self.mcaj_numero)
		return self.db.ejecutar(query, values)[0][0]

	def totalIngresos(self):
		query = "SELECT totalIngresos(%s, %s, %s)"
		values = (self.mcam_anio, self.mcam_num, self.mcaj_numero)
		return self.db.ejecutar(query, values)[0][0]

	def totalEgresos(self):
		query = "SELECT totalEgresos(%s, %s, %s)"
		values = (self.mcam_anio, self.mcam_num, self.mcaj_numero)
		return self.db.ejecutar(query, values)[0][0]

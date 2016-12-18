# -*- coding: utf-8 -*-
from db_conn import DBConn

class ModeloRutas:

	def __init__(self):
		self.rut_id = 0
		self.rut_nombre = ''
		self.rut_orden = 0
		self.db = DBConn()

	def create(self):
		query = 'CALL crearRuta(%s, %s);'
		values = (self.rut_nombre, self.rut_orden)
		return self.db.ejecutar(query, values)

	def update(self):
		query = 'CALL modificarRuta(%s, %s, %s);'
		values = (self.rut_id, self.rut_nombre, self.rut_orden)
		return self.db.ejecutar(query, values)

	def delete(self):
		query = 'CALL eliminarRuta(%s);'
		values = (self.rut_id)
		return self.db.ejecutar(query, values)

	def read_all(self):
		query = 'SELECT * FROM rutas WHERE rut_id <> 1;'
		return self.db.ejecutar(query)

	def read(self):
		query = 'SELECT * FROM rutas WHERE rut_id = %s;'
		values = (self.rut_id)
		return self.db.ejecutar(query, values)

	def read_name(self):
		query = 'SELECT * FROM rutas WHERE rut_nombre = %s;'
		values = (self.rut_nombre)
		return self.db.ejecutar(query, values)

	def exist(self):
		query = "SELECT existeRuta(%s);"
		values = (self.rut_nombre)
		return self.db.ejecutar(query, values)[0][0] > 0

	def get_id(self):
		query = 'SELECT rut_id FROM rutas WHERE rut_nombre = %s'
		values = (self.rut_nombre)
		return self.db.ejecutar(query, values)[0][0]

	def customers_in_router(self, anio, num):
		query = "SELECT cli_orden, cli_codigo, cli_seccion, cli_apenom, \
				(SELECT art_deuda FROM articulos WHERE acam_anio = %s and acam_num = %s and acli_codigo = cli_codigo) as deuda,\
				cli_localidad, cli_domicilio, \
				cli_telefono, cli_barrio, cli_referencia, rut_id, \
				(SELECT alis_numero FROM articulos WHERE acam_anio = %s and acam_num = %s and acli_codigo = cli_codigo) as listado,\
				rut_nombre\
				FROM clientes\
				INNER JOIN rutas ON crut_id = rut_id \
				WHERE rut_orden = %s;"
		values = (anio, num, anio, num, self.rut_orden)
		return self.db.ejecutar(query, values)

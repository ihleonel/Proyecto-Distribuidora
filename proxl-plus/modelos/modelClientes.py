# -*- coding: utf-8 -*-
from db_conn import DBConn

class ModeloClientes:

	def __init__(self):
		self.codigo = ""
		self.apenom = ""
		self.zona = ""
		self.domicilio = ""
		self.telefonos = ""
		self.barrio = ""
		self.localidad = ""
		self.seccion = ""
		self.descripcion = ""
		self.referencia = 0 # 0: Sale a reparto; 1: R/D; 2: N/S 
		self.crut_id = 0
		self.orden = 0
		self.estado = 0
		self.alta = ""
		self.baja = ""
		
		self.db = DBConn()

	def __str__(self):
		return str((self.codigo, self.apenom, self.domicilio, self.barrio, self.localidad, self.crut_id, self.orden))

	def initialize(self):
		self.codigo = ""
		self.apenom = ""
		self.zona = ""
		self.domicilio = ""
		self.barrio = ""
		self.localidad = ""
		self.seccion = ""
		self.descripcion = ""
		self.telefonos = ""

	def create(self):
		query = "CALL insertarCliente(%s, %s, %s, %s, %s, %s, %s, %s, %s);"
		values = (self.codigo, self.apenom, self.domicilio, self.telefonos, self.barrio, self.localidad, self.seccion, self.zona, self.descripcion)
		return self.db.ejecutar(query, values)

	def create_short(self):
		query = "CALL insertarCliente2(%s)"
		values = (self.codigo)
		return self.db.ejecutar(query, values)

	def delete(self):
		query = "CALL eliminarCliente(%s)"
		values = (self.codigo)
		return self.db.ejecutar(query, values)

	def update(self):
		query = "CALL actualizarCliente(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		values = (self.codigo, self.apenom, self.domicilio, self.telefonos, self.barrio, self.localidad, self.seccion, self.zona, self.descripcion, self.referencia, self.crut_id, self.orden)
		return self.db.ejecutar(query, values)

	def new_update(self):
		if self.apenom:
			query = "UPDATE clientes SET cli_apenom=%s WHERE cli_codigo=%s;" % (self.apenom, self.codigo)
			self.db.ejecutar(query)

		if self.domicilio:
			query = "UPDATE clientes SET cli_domicilio=%s WHERE cli_codigo=%s;" % (self.domicilio, self.codigo)
			self.db.ejecutar(query)

		if self.telefonos:
			query = "UPDATE clientes SET cli_telefono=%s WHERE cli_codigo=%s;" % (self.telefonos, self.codigo)
			self.db.ejecutar(query)

		if self.barrio:
			query = "UPDATE clientes SET cli_barrio=%s WHERE cli_codigo=%s;" % (self.barrio, self.codigo)
			self.db.ejecutar(query)

		if self.localidad:
			query = "UPDATE clientes SET cli_localidad=%s WHERE cli_codigo=%s;" 
			values = (self.localidad, self.codigo)
			self.db.ejecutar(query, values)

		if self.seccion:
			query = "UPDATE clientes SET cli_seccion=%s WHERE cli_codigo=%s;" % (self.seccion, self.codigo)
			self.db.ejecutar(query)

		if self.zona:
			query = "UPDATE clientes SET cli_zona=%s WHERE cli_codigo=%s;" % (self.zona, self.codigo)
			self.db.ejecutar(query)

		if self.descripcion:
			query = "UPDATE clientes SET cli_descripcion=%s WHERE cli_codigo=%s;" % (self.descripcion, self.codigo)
			self.db.ejecutar(query)

		if self.referencia:
			query = "UPDATE clientes SET cli_referencia=%s WHERE cli_codigo=%s;" % (self.referencia, self.codigo)
			self.db.ejecutar(query)


	def read_all_for_code(self):
		query = "SELECT cli_codigo, cli_apenom, cli_domicilio FROM clientes WHERE cli_estado = 1 AND cli_codigo LIKE %s"
		value = (self.codigo+"%")
		return self.db.ejecutar(query, value)

	def read_all_for_name(self):
		query = "SELECT cli_codigo, cli_apenom, cli_domicilio FROM clientes WHERE cli_estado = 1 AND (SELECT locate(%s, cli_apenom))<>0"
		value = (self.apenom)
		return self.db.ejecutar(query, value)

	def read(self):
		query = "SELECT cli_codigo, cli_apenom, cli_zona, cli_domicilio, cli_telefono, cli_barrio, cli_localidad, cli_seccion, cli_descripcion, cli_referencia, crut_id, cli_orden, cli_estado, cli_alta, cli_baja\
				FROM clientes\
				WHERE cli_codigo = %s"
		values = (self.codigo)
		tabla = self.db.ejecutar(query, values)
		resultado = {'codigo': tabla[0][0],
					'nombre': tabla[0][1], 
					'zona': tabla[0][2], 
					'domicilio': tabla[0][3],
					'telefonos': tabla[0][4], 
					'barrio': tabla[0][5],
					'localidad': tabla[0][6],
					'seccion': tabla[0][7],
					'descripcion': tabla[0][8],
					'referencia': tabla[0][9],
					'ruta_id': tabla[0][10],
					'orden': tabla[0][11],
					'estado': tabla[0][12],
					'alta': tabla[0][13],
					'baja': tabla[0][14]}
		return resultado

	def read_with_ruta(self):
		query = "SELECT cli_codigo, cli_apenom, cli_zona, cli_domicilio, cli_telefono, cli_barrio, cli_localidad, cli_seccion, cli_descripcion, cli_referencia, crut_id, rut_nombre, cli_orden, cli_estado, cli_alta, cli_baja\
				FROM clientes INNER JOIN rutas ON crut_id = rut_id\
				WHERE cli_codigo = %s"
		values = (self.codigo)
		tabla = self.db.ejecutar(query, values)
		resultado = {'codigo': tabla[0][0],
					'nombre': tabla[0][1], 
					'zona': tabla[0][2], 
					'domicilio': tabla[0][3],
					'telefonos': tabla[0][4], 
					'barrio': tabla[0][5],
					'localidad': tabla[0][6],
					'seccion': tabla[0][7],
					'descripcion': tabla[0][8],
					'referencia': tabla[0][9],
					'ruta_id': tabla[0][10],
					'ruta_nombre': tabla[0][11],
					'orden': tabla[0][12],
					'estado': tabla[0][13],
					'alta': tabla[0][14],
					'baja': tabla[0][15]}
		return resultado


	def exist(self):
		query = "SELECT existeCliente(%s)"
		value = (self.codigo)
		return self.db.ejecutar(query, value)[0][0] == 1

	def actualizar_orden(self):
		query = 'UPDATE Clientes SET cli_orden = %s WHERE cli_codigo = %s;'
		values = (self.orden, self.codigo)
		return self.db.ejecutar(query, values)


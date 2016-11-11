# -*- coding : utf-8 -*-
from db_conn import DBConn
class ModeloUsuarios:
	def __init__(self):
		self.usuario = ''
		self.clave = ''
		self.tipo = ''
		self.estado = 1
		self.db = DBConn()

	def create(self):
		query = "CALL agregarUsuario(%s, %s, %s)"
		values = (self.usuario, self.clave, self.tipo)
		return self.db.ejecutar(query, values)

	def update(self):
		query = "CALL modificarUsuario(%s, %s, %s)"
		values = (self.usuario, self.clave, self.tipo)
		return self.db.ejecutar(query, values)

	def delete(self):
		query = "CALL deshabilitarUsuario(%s)"
		values = (self.usuario)
		return self.db.ejecutar(query, values)

	def existUser(self):
		query = "SELECT existeUsuario(%s)"
		values = (self.usuario)
		return self.db.ejecutar(query, values)[0][0]

	def existUserKey(self):
		query = "SELECT existeUsuarioClave(%s, %s)"
		values = (self.usuario, self.clave)
		return self.db.ejecutar(query, values)[0][0]

	def typeUser(self):
		query = "SELECT tipoUsuario(%s, %s)"
		values = (self.usuario, self.clave)
		return self.db.ejecutar(query, values)[0][0]

	def read_all(self):
		query = "SELECT * FROM usuarios WHERE usu_estado = 1"
		tabla = self.db.ejecutar(query)
		datos = []
		for fila in tabla:
			if fila[0] != "root":
				dato = {'usuario': fila[0], 
						'clave': fila[1], 
						'tipo': fila[2]}
				datos.append(dato)
		return datos

	def read_all_for_name(self):
		query = "SELECT * FROM usuarios WHERE usu_usuario = %s AND usu_estado = 1"
		values = (self.usuario)
		tabla = self.db.ejecutar(query, values)
		datos = []
		for fila in tabla:
			if fila[0] != "root":
				dato = {'usuario': fila[0], 
						'clave': fila[1], 
						'tipo': fila[2]}
				datos.append(dato)
		return datos
	def read(self):
		query = "SELECT * FROM usuarios WHERE usu_usuario = %s AND usu_estado = 1"
		values = (self.usuario)
		tabla = self.db.ejecutar(query, values)
		dato = {'usuario': tabla[0][0], 
				'clave': tabla[0][1], 
				'tipo': tabla[0][2]}
		return dato
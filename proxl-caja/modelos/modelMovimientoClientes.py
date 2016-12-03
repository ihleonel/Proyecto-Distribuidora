# -*- coding: utf-8 -*-
from db_conn import DBConn

class ModeloMovimientoClientes:

	def __init__(self):
		self.mcam_anio = 0
		self.mcam_num = 0
		self.mcaj_numero = 0
		self.mcli_codigo = ""
		self.movcli_monto = 0.0
		self.movcli_entregado = 0
		self.movcli_forma_pago = 0
		self.movcli_diferencia = 0.0

		self.db = DBConn()

	def create(self):
		query = "CALL agregarMovimientoCliente(%s, %s, %s, %s, %s, %s, %s, %s);"
		values = (self.mcam_anio, self.mcam_num, self.mcaj_numero, self.mcli_codigo, self.movcli_monto, self.movcli_entregado, self.movcli_forma_pago, self.movcli_diferencia)
		return self.db.ejecutar(query, values)

	def get_delivered_box(self):
		query = "SELECT cli_codigo, cli_apenom, movcli_monto, movcli_entregado, movcli_forma_pago, movcli_diferencia\
				FROM movimiento_clientes INNER JOIN clientes ON cli_codigo = mcli_codigo\
				WHERE mcam_anio = %s AND mcam_num = %s AND mcaj_numero = %s"
		values = (self.mcam_anio, self.mcam_num, self.mcaj_numero)
		return self.db.ejecutar(query, values)

	def read(self):
		query = "SELECT cli_codigo, cli_apenom, movcli_monto, movcli_entregado, movcli_forma_pago, movcli_diferencia\
				FROM movimiento_clientes INNER JOIN clientes ON cli_codigo = mcli_codigo\
				WHERE mcam_anio = %s AND mcam_num = %s AND mcaj_numero = %s AND mcli_codigo = %s"
		values = (self.mcam_anio, self.mcam_num, self.mcaj_numero, self.mcli_codigo)
		return self.db.ejecutar(query, values)[0]

	def read_all(self):
		query = "SELECT cli_codigo, cli_apenom, movcli_monto, movcli_entregado, movcli_forma_pago, movcli_diferencia\
				FROM movimiento_clientes INNER JOIN clientes ON cli_codigo = mcli_codigo\
				WHERE mcam_anio = %s AND mcam_num = %s AND mcaj_numero = %s"
		values = (self.mcam_anio, self.mcam_num, self.mcaj_numero)
		return self.db.ejecutar(query, values)

	def totalIngresosClientes(self):
		query = "SELECT totalIngresosMClientes(%s, %s, %s);"
		values = (self.mcam_anio, self.mcam_num, self.mcaj_numero)
		return self.db.ejecutar(query, values)[0][0]

	def existe(self):
		query = "SELECT existeMovimientoCliente(%s, %s, %s)"
		values = (self.mcam_anio, self.mcam_num, self.mcli_codigo)
		return self.db.ejecutar(query, values)[0][0]

	def update_e(self, anio, num, cnum, cod, entr, fentr):
		query = "CALL actualizarEntrega(%s, %s, %s, %s, %s, %s)"
		values = (anio, num, cnum, cod, entr, fentr)
		return self.db.ejecutar(query, values)

	def update(self):
		query = "CALL actualizarMovCli(%s, %s, %s, %s, %s, %s, %s, %s)"
		values = (self.mcam_anio, self.mcam_num, self.mcaj_numero, self.mcli_codigo, self.movcli_monto, self.movcli_entregado, self.movcli_forma_pago, self.movcli_diferencia)
		return self.db.ejecutar(query, values)

	def __str__(self):
		return str(self.mcam_anio) +'-'+ str(self.mcam_num)+'-' + str(self.mcaj_numero)+'-' + str(self.mcli_codigo)+'-' + str(self.movcli_monto)

	def superCargaMov(self, anio, num, cnum, cod, reb, mentr, monto, entr, fpago, dif, fentr):
		query = "CALL superCargaMovimiento(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
		values = (anio, num, cnum, cod, reb, mentr, monto, entr, fpago, dif, fentr)
		return self.db.ejecutar(query, values)
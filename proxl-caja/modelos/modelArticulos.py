# -*- coding: utf-8 -*-
from db_conn import DBConn

class ModeloArticulos:

	def __init__(self):
		self.cam_anio = 0
		self.cam_num = 0
		self.lis_numero = 0
		self.cli_codigo = ''
		self.cli_apenom = ''
		self.deuda = 0.0
		self.camp = ""
		self.entregado = '0000/00/00'
		self.forma_pago = 0	#0: No pagado; 1:Efectivo; 2:Boleta; 3:Oficina
		self.medio_entr = 0	#0; 1:Caja; 2:Envio
		self.rebote = "#$NINGUNO$#"
		self.db = DBConn()

	def create(self):
		'Registra una nuevo articulo en la tabla Articulos.'
		query = "CALL agregarArticulo(%s, %s, %s, %s, %s, %s);"
		values = (self.cam_anio, self.cam_num, self.lis_numero, self.cli_codigo, self.deuda, self.camp)
		return self.db.ejecutar(query, values)

	def update(self):
		'Modifica un articulo de la tabla Articulos.'
		query = "Call actualizarArticulo(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
		values = (self.cam_anio, self.cam_num, self.lis_numero, self.cli_codigo, self.deuda, self.camp, self.entregado, self.forma_pago, self.medio_entr, self.rebote)
		return self.db.ejecutar(query, values)

	def exist(self):
		query = "SELECT COUNT(*) FROM articulos WHERE acam_anio = %s AND acam_num = %s AND acli_codigo = %s;"
		values = (self.cam_anio, self.cam_num, self.cli_codigo)
		return self.db.ejecutar(query, values)[0][0] != 0

	def read_for_name(self):
		"""Retorna un registro de articulo."""
		query = "SELECT acam_anio, acam_num, alis_numero, acli_codigo, art_deuda, art_camp, art_entregado, art_forma_pago, art_medio_entr, cli_apenom, cli_domicilio, cli_zona FROM articulos \
				INNER JOIN clientes ON acli_codigo = cli_codigo\
				WHERE acam_anio = %s AND acam_num = %s AND (SELECT locate(%s, cli_apenom))<>0 "
		values = (self.cam_anio, self.cam_num, self.cli_apenom)
		tabla =  self.db.ejecutar(query, values)
		resultados = []
		for columna in tabla:
			resultado = {}
			resultado['anio'] = columna[0]
			resultado['num'] = columna[1]
			resultado['lis'] = columna[2]
			resultado['codigo'] = columna[3]
			resultado['deuda'] = columna[4]
			resultado['campania'] = columna[5]
			resultado['entregado'] = columna[6]
			resultado['forma_pago'] = columna[7]
			resultado['medio_entr'] = columna[8]
			resultado['nombre'] = columna[9]
			resultado['domicilio'] = columna[10]
			resultado['zona'] = columna[11]
			resultados.append(resultado)

		return resultados


	def read(self):
		"""Retorna un registro de articulo."""
		query = "SELECT acam_anio, acam_num, alis_numero, acli_codigo, art_deuda, art_camp, art_entregado, art_forma_pago, art_medio_entr, art_rebote, cli_apenom, cli_zona FROM articulos \
				INNER JOIN clientes ON acli_codigo = cli_codigo\
				WHERE acam_anio = %s AND acam_num = %s AND acli_codigo = %s "
		values = (self.cam_anio, self.cam_num, self.cli_codigo)
		tabla =  self.db.ejecutar(query, values)
		resultado = {}
		if tabla != ():
			resultado['anio'] = tabla[0][0]
			resultado['num'] = tabla[0][1]
			resultado['lis'] = tabla[0][2]
			resultado['codigo'] = tabla[0][3]
			resultado['deuda'] = tabla[0][4]
			resultado['campania'] = tabla[0][5]
			resultado['entregado'] = tabla[0][6]
			resultado['forma_pago'] = tabla[0][7]
			resultado['medio_entr'] = tabla[0][8]
			resultado['rebote'] = tabla[0][9]
			resultado['nombre'] = tabla[0][10]
			resultado['zona'] = tabla[0][11]

		return resultado

	def result_campaign(self):
		values = (self.cam_anio, self.cam_num)
		resultado = {}

		query = "SELECT cantArticulosCampania(%s, %s);"
		resultado["cantArticulosCampania"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT cantArticulosNoEntregados(%s, %s);"
		resultado["cantArticulosNoEntregados"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT cantArticulosBoletas(%s, %s);"
		resultado["cantArticulosBoletas"] = self.db.ejecutar(query, values)[0][0]

		# Efectivo

		query = "SELECT cantArticulosEntregadosEfectivo(%s, %s);"
		resultado["entregadosEfectivo"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT cantArticulosNoEntregadosEfectivo(%s, %s);"
		resultado["noEntregadosEfectivo"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT cantArticulosCobradosEfectivo(%s, %s);"
		resultado["cobradosEfectivo"] = self.db.ejecutar(query, values)[0][0]

		# Boletas

		query = "SELECT cantArticulosEntregadosBoleta(%s, %s);"
		resultado["entregadosBoleta"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT cantArticulosNoEntregadosBoleta(%s, %s);"
		resultado["noEntregadosBoleta"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT cantArticulosCobradosBoleta(%s, %s);"
		resultado["cobradosBoleta"] = self.db.ejecutar(query, values)[0][0]

		# Recibo oficina

		query = "SELECT cantArticulosEntregadosOficina(%s, %s);"
		resultado["entregadosOficina"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT cantArticulosNoEntregadosOficina(%s, %s);"
		resultado["noEntregadosOficina"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT cantArticulosCobradosOficina(%s, %s);"
		resultado["cobradosOficina"] = self.db.ejecutar(query, values)[0][0]

		# No cobrados 
		query = "SELECT cantArticulosEntregadosNoCobrados(%s, %s);"
		resultado["entregadosNoCobrados"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT cantArticulosNoEntregadosNoCobrados(%s, %s);"
		resultado["noEntregadosNoCobrados"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT cantArticulosNoCobrados(%s, %s);"
		resultado["noCobrados"] = self.db.ejecutar(query, values)[0][0]

		# Valores Articulos
		query = "SELECT valArticulosCampania(%s, %s);"
		resultado["valArticulosCampania"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT valArticulosNoEntregados(%s, %s);"
		resultado["valArticulosNoEntregados"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT valArticulosBoletas(%s, %s);"
		resultado["valArticulosBoletas"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT valArticulosEntregadosNoCobrados(%s, %s);"
		resultado["valEntregadosNoCobrados"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT valArticulosNoEntregadosNoCobrados(%s, %s);"
		resultado["valNoEntregadosNoCobrados"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT valArticulosNoCobrados(%s, %s);"
		resultado["valNoCobrados"] = self.db.ejecutar(query, values)[0][0]


		# efectivo

		query = "SELECT valArticulosEntregadosEfectivo(%s, %s);"
		resultado["valEntregadosEfectivo"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT valArticulosNoEntregadosEfectivo(%s, %s);"
		resultado["valNoEntregadosEfectivo"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT valArticulosEfectivo(%s, %s);"
		resultado["valEfectivo"] = self.db.ejecutar(query, values)[0][0]

		# boleta

		query = "SELECT valArticulosEntregadosBoleta(%s, %s);"
		resultado["valEntregadosBoleta"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT valArticulosNoEntregadosBoleta(%s, %s);"
		resultado["valNoEntregadosBoleta"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT valArticulosBoleta(%s, %s);"
		resultado["valBoleta"] = self.db.ejecutar(query, values)[0][0]

		# oficina

		query = "SELECT valArticulosEntregadosOficina(%s, %s);"
		resultado["valEntregadosOficina"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT valArticulosNoEntregadosOficina(%s, %s);"
		resultado["valNoEntregadosOficina"] = self.db.ejecutar(query, values)[0][0]

		query = "SELECT valArticulosOficina(%s, %s);"
		resultado["valOficina"] = self.db.ejecutar(query, values)[0][0]

		return resultado

	def obtenerContenidoCampania(self):
		query = "SELECT cli_zona, cli_codigo, art_camp, art_deuda, art_entregado, art_forma_pago \
				FROM articulos INNER JOIN clientes ON cli_codigo = acli_codigo\
				WHERE acam_anio = %s AND acam_num = %s\
				ORDER BY 2;"
		values = (self.cam_anio, self.cam_num)

		return self.db.ejecutar(query, values)






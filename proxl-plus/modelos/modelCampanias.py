# -*- coding: utf-8 -*-
from db_conn import DBConn

class ModeloCampanias:

	def __init__(self):
		self.anio = 0 #hasta 4 digitos
		self.num = 0 #hasta 4 digitos
		self.cli_codigo = ''
		self.inicio = '' #fecha
		self.ini_reparto = '' # fecha de inicio de reparto
		self.fin_reparto = '' # fecha de fin de reparto
		self.base = 0.00 # base de distribucion
		self.parametro = 0.00 # distribucion = (pedidos a cobrar) x parametro + base
		self.diferencia = 0.00 # monto de diferencia con campania anterior
		self.fin = '' #fecha
		self.comentario = '' #hasta 700 caracteres
		self.usuario = 0
		self.db = DBConn()

	def create(self):
		query = "CALL agregarCampania(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		values = (self.anio, self.num, self.inicio, self.ini_reparto, self.diferencia, self.parametro, self.base, self.comentario, self.usuario)
		return self.db.ejecutar(query, values)

	def close(self):
		query = "UPDATE campanias SET cam_fin = %s WHERE cam_anio = %s AND cam_num = %s"
		values = (self.fin, self.anio, self.num)
		return self.db.ejecutar(query, values)

	def update(self):
		query = "Call actualizarCampania(%s, %s, %s, %s, %s, %s, %s, %s)"
		values = (self.anio, self.num, self.ini_reparto, self.fin_reparto, self.diferencia, self.parametro, self.base, self.comentario)
		return self.db.ejecutar(query, values)

	def delete(self):
		query = "Call eliminarCampania(%s, %s)"
		values = (self.anio, self.num)
		return self.db.ejecutar(query, values)

	def read_x_anio_num(self):
		query="SELECT cam_anio, cam_num, cam_inicio, cam_fin, cam_usuario \
				FROM campanias \
				WHERE cam_anio = %s AND cam_num = %s"
		values = (self.anio, self.num)
		return self.db.ejecutar(query, values)

	def read_x_anio(self):
		query="SELECT cam_anio, cam_num, cam_inicio, cam_fin, cam_usuario \
				FROM campanias \
				WHERE cam_anio = %s"
		values = (self.anio)
		return self.db.ejecutar(query, values)


	def read_all(self):
		query = "SELECT cam_anio, cam_num, cam_inicio, cam_fin, cam_usuario \
				FROM campanias"
		return self.db.ejecutar(query)

	def exist_campaign(self):
		query = "SELECT existeCampania(%s, %s);"
		values = (self.anio, self.num)
		return self.db.ejecutar(query, values)[0][0] != 0

	def read(self):
		query="SELECT cam_anio, cam_num, cam_inicio, cam_ini_reparto, cam_fin_reparto, cam_diferencia, cam_parametro, cam_base, cam_comentario, cam_fin, cam_usuario \
				FROM campanias \
				WHERE cam_anio = %s AND cam_num = %s"
		values = (self.anio, self.num)
		tabla = self.db.ejecutar(query, values)
		campania = {}
		if tabla != ():
			campania = {'anio': tabla[0][0],
						'num': tabla[0][1], 
						'inicio': self.date_format(tabla[0][2]),
						'ini_reparto': tabla[0][3],
						'fin_reparto': tabla[0][4],
						'diferencia': tabla[0][5],
						'parametro': tabla[0][6],
						'base': tabla[0][7],
						'comentario': tabla[0][8], 
						'fin': tabla[0][9], 
						'usuario': tabla[0][10]}
		return campania

	def get_active_campaign(self):
		query = "SELECT cam_anio, cam_num, cam_inicio, cam_ini_reparto, cam_fin_reparto, cam_diferencia, cam_parametro, cam_base, cam_comentario, cam_fin, cam_usuario \
				FROM campanias WHERE cam_fin = %s"
		values = ('0000-00-00')
		datos =  self.db.ejecutar(query, values)
		resultado = {}
		if datos != ():
			resultado['anio'] = datos[0][0]
			resultado['numero'] = datos[0][1]
			resultado['inicio'] = self.date_format(datos[0][2])
			resultado['ini_reparto'] = datos[0][3]
			resultado['fin_reparto'] = datos[0][4]
			resultado['diferencia'] = datos[0][5]
			resultado['parametro'] = datos[0][6]
			resultado['base'] = datos[0][7]
			resultado['comentarios'] = datos[0][8]
			resultado['fin'] = datos[0][9]
			resultado['usuario'] = datos[0][10]

		return resultado

	def get_next_number_campaign(self):
		'Retorna el siguinte numero de campania.'
		query = "SELECT siguienteNumeroCampania(%s);"
		values = (self.anio)
		return self.db.ejecutar(query, values)[0][0]

	def codes_campaign(self):
		query = "SELECT c.cli_codigo, c.cod_deuda, c.cod_camp, c.cod_entregado, c.cod_efectivo, c.cod_boleta\
    	FROM listados l\
    	INNER JOIN codigos c ON c.lis_id = l.lis_id\
    	WHERE l.cam_id = %s;"
		values = (self.id)
		codigos = self.db.ejecutar(query, values)
		resultado = []
		for fila in codigos:
			dato = {'codigo': fila[0], 
					'deuda': str(fila[1]), 
					'campania': str(fila[2]), 
					'entregado': fila[3], 
					'efectivo': fila[4], 
					'boleta': fila[5]}
			resultado.append(dato)
		return resultado

	def campaign_in_range(self, rng):
		query = "SELECT cam_anio, cam_num FROM campanias ORDER BY 1 DESC LIMIT %s"
		values = (rng)
		return self.db.ejecutar(query, values)
		
	def date_format(self, s):
		'Formatea una fecha dada (aaaa-mm-dd  >>  dd-mm-aaaa)'
		s = str(s)
		l = s.split("-")
		l[0], l[2] = l[2], l[0]
		return "-".join(l)
# -*- coding: utf-8 -*-
from db_conn import DBConn

class ModeloCampanias:

	def __init__(self):
		self.anio = 0 #hasta 4 digitos
		self.num = 0 #hasta 4 digitos
		self.cli_codigo = ''
		self.inicio = '' #fecha
		self.fin = '' #fecha
		self.comentario = '' #hasta 700 caracteres
		self.usuario = 0
		self.db = DBConn()

	def create(self):
		query = "CALL agregarCampania(%s, %s, %s, %s, %s)"
		values = (self.anio, self.num, self.inicio, self.comentario, self.usuario)
		return self.db.ejecutar(query, values)

	def close(self):
		query = "UPDATE campanias SET cam_fin = %s WHERE cam_anio = %s AND cam_num = %s"
		values = (self.fin, self.anio, self.num)
		return self.db.ejecutar(query, values)

	def update(self):
		query = "Call actualizarCampania(%s, %s, %s)"
		values = (self.anio, self.num, self.comentario)
		return self.db.ejecutar(query, values)

	def delete(self):
		query = "Call eliminarCampania(%s, %s)"
		values = (self.anio, self.num)
		return self.db.ejecutar(query, values)

	def read(self):
		query="SELECT cam_anio, cam_num, cam_inicio, cam_comentario, cam_fin, cam_usuario \
				FROM campanias \
				WHERE cam_anio = %s AND cam_num = %s"
		values = (self.anio, self.num)
		tabla = self.db.ejecutar(query, values)
		campania = {}
		if tabla != ():
			campania = {'anio': tabla[0][0],
						'num': tabla[0][1], 
						'inicio': self.date_format(tabla[0][2]),
						'comentario': tabla[0][3], 
						'fin': tabla[0][4], 
						'usuario': tabla[0][5]}
		return campania

	def read_all(self):
		query = "SELECT cam_anio, cam_num, cam_inicio, cam_usuario \
				FROM campanias"
		return self.db.ejecutar(query)

	def get_active_campaign(self):
		query = "SELECT cam_anio, cam_num, cam_inicio, cam_comentario, cam_fin, cam_usuario \
				FROM campanias WHERE cam_fin = %s"
		values = ('0000-00-00')
		datos =  self.db.ejecutar(query, values)
		resultado = {}
		if datos != ():
			resultado['anio'] = datos[0][0]
			resultado['numero'] = datos[0][1]
			resultado['inicio'] = self.date_format(datos[0][2])
			resultado['comentarios'] = datos[0][3]
			resultado['fin'] = datos[0][4]
			resultado['usuario'] = datos[0][5]

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

	def date_format(self, s):
		'Formatea una fecha dada (aaaa-mm-dd  >>  dd-mm-aaaa)'
		s = str(s)
		l = s.split("-")
		l[0], l[2] = l[2], l[0]
		return "-".join(l)
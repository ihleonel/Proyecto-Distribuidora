# -*- coding : utf-8 -*-
from db_conn import DBConn
class ModeloHistoriales:
	def __init__(self):
		self.db = DBConn()

	def get_history_costumer_c(self, codigo, anio_ini, num_ini, anio_fin, num_fin):
		'Retorna una tabla con el historial de un clientes en un periodo dado.'
		query = "SELECT cam_anio, cam_num, art_deuda, art_entregado, art_efectivo, art_boleta\
				FROM campanias\
				INNER JOIN articulos ON acam_anio = cam_anio AND acam_num = cam_num\
				INNER JOIN clientes ON acli_codigo = cli_codigo\
				WHERE cli_codigo = %s AND cam_anio BETWEEN %s AND %s \
				AND cam_num BETWEEN %s AND %s;"
		values = (codigo, anio_ini, anio_fin, num_ini, num_fin)
		return self.db.ejecutar(query, values)



# -*- coding: utf-8 -*-
'''
Nombre: modelo.py
Autor: Ibarra Hector Leonel
'''

import xlwt, locale
from datetime import datetime
from modelos.modelMovimientos import ModeloMovimientos 
from modelos.modelMovimientoClientes import ModeloMovimientoClientes 
class ModeloReportes:

	mdlMov = ModeloMovimientos()
	mdlMovCli = ModeloMovimientoClientes()

	def __init__(self, caja):
		self.dir = dir
		self.caja = caja 
		locale.setlocale(locale.LC_ALL, 'spanish_spain') # Para que la fecha este es catelano.

	def generar_libro(self):
		"""Crear libro y hoja xls"""
		wb = xlwt.Workbook(encoding='latin-1')
		ws = wb.add_sheet("Hoja1")

		#Cargar encabezado
		ws.write(0, 2, "PLANILLA DE CAJA DE DEPOSITO")
		ws.write(1, 2, datetime.today().strftime("%A, %d de %B de %Y"))
		ws.write(2, 0, "CODIGO")
		ws.write(2, 1, "APELLIDO")
		ws.write(2, 2, "INGRESOS")
		ws.write(2, 3, "ENTREGADO")
		ws.write(2, 4, "EGRESOS")
		ws.write(2, 5, "OFICINA")
		ws.write(2, 6, "BOLETA")

		#Cargando cuerpo de listado de caja
		indice = 3
		self.mdlMovCli.mcam_anio = self.caja['campAnio']
		self.mdlMovCli.mcam_num = self.caja['campNum']
		self.mdlMovCli.mcaj_numero = self.caja['numero']

		listado = self.mdlMovCli.get_delivered_box()
		if len(listado) != 0:
			for fila in listado:
				ws.write(indice, 0, fila[0])
				ws.write(indice, 1, fila[1])
				ws.write(indice, 2, fila[2])
				if fila[3] == 1:
					ws.write(indice, 3, 'Si')
				else:
					ws.write(indice, 3, 'No')

				if fila[4] == 3:
					ws.write(indice, 5, fila[5])
				elif fila[4] == 2:
					ws.write(indice, 6, fila[5])
				indice += 1
		#Cargando ingresos varios
		self.mdlMov.mcam_anio = self.caja['campAnio']
		self.mdlMov.mcam_num = self.caja['campNum']
		self.mdlMov.mcaj_numero = self.caja['numero']

		indice += 3
		ws.write(indice, 0, 'FONDO DE CAJA')
		ws.write(indice, 2, float(self.caja['monto']))
		indice += 1
		listado = self.mdlMov.get_income()
		if len(listado) != 0:
			for fila in listado:
				ws.write(indice, 0, fila[0])
				ws.write(indice, 2, fila[1])
				indice += 1
		# Cargando egresos varios
		indice += 3
		listado = self.mdlMov.get_expenses()
		if len(listado) != 0:
			for fila in listado:
				ws.write(indice, 0, fila[0])
				ws.write(indice, 4, fila[1])
				indice += 1

		#Cargando pie de listado
		indice += 1
		ws.write(indice, 0, 'TOTALES')
		exp = 'SUM(C3:C%s)' % (indice)
		ws.write(indice, 2, xlwt.Formula(exp))
		exp = 'SUM(E3:E%s)' % (indice)
		ws.write(indice, 4, xlwt.Formula(exp))
		exp = 'SUM(F3:F%s)' % (indice)
		ws.write(indice, 5, xlwt.Formula(exp))
		exp = 'SUM(G3:G%s)' % (indice)
		ws.write(indice, 6, xlwt.Formula(exp))

		wb.save(self.dir)

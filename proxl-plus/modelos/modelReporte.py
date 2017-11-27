# -*- coding: utf-8 -*-
'''
Nombre: modelReporte.py
Autor: Ibarra Hector Leonel
'''
import wx
import xlwt, locale
from modelos.modelArticulos import ModeloArticulos 
from modelos.modelClientes import ModeloClientes
from modelos.modelCampanias import ModeloCampanias
from modelos.modelListados import ModeloListados
from modelos.modelEnvios import ModeloEnvios
from modelos.modelGastos import ModeloGastosVarios


class ModeloReporte:
	"""Esta clase contiene los modulos para la creacion de archivos de extencion .xls
		para la generacion de reporte de campañas."""
	mdlCli = ModeloClientes()
	mdlArt = ModeloArticulos()
	mdlCamp = ModeloCampanias()
	mdlEnv = ModeloEnvios()
	mdlGvar = ModeloGastosVarios()

	def __init__(self, dir, camp):
		self.dir = dir
		self.mdlCamp.anio = camp['anio']
		self.mdlCamp.num = camp['numero']
		self.camp = self.mdlCamp.read()
		locale.setlocale(locale.LC_ALL, 'spanish_spain') # Para que la fecha este es catelano.


	def generar_libro(self):
		"""Crear libro y hoja xls"""
		wb = xlwt.Workbook(encoding='latin-1')
		ws = wb.add_sheet("Hoja1")

		#Cargando encabezado
		ws.write(0, 0, "ZONA")
		ws.write(0, 1, u"CÓDIGO")
		ws.write(0, 2, "LOCALIDAD")
		ws.write(0, 3, "CAMP")
		ws.write(0, 4, "DEUDA")
		ws.write(0, 5, "NO ENTR")
		ws.write(0, 6, "BOLETA")

		#Cargando cuerpo de listado
		self.mdlArt.cam_anio =  self.camp['anio']
		self.mdlArt.cam_num = self.camp['num']
		tabla = self.mdlArt.obtenerContenidoCampania()

		for i, fila in enumerate(tabla):
			ws.write(i+1, 0, int(fila[0])) # Zona
			ws.write(i+1, 1, str(fila[1])) # Codigo
			ws.write(i+1, 2, str(fila[2])) # Localidad
			ws.write(i+1, 3, int(fila[3])) # Camp
			ws.write(i+1, 4, float(fila[4])) # Deuda

			if str(fila[5]) == "None":	# No Entr
				ws.write(i+1, 5, "x")
			else:
				ws.write(i+1, 5, "")

			if fila[6] == 2:			# Boleta
				ws.write(i+1, 6, "x")
			else:
				ws.write(i+1, 6, "")

		# Cargando pie de reporte (formulas)
		cantFilas = len(tabla)

		ws.write(cantFilas+5, 1, "Total en $")

		valArticulosCampania = 'SUM(E1:E%s)' % (cantFilas+1)
		ws.write(cantFilas+5, 3, xlwt.Formula(valArticulosCampania))

		valArticulosNoEntregados = 'SUMIF(F1:F%s;"x";E1:E%s)' % (cantFilas+1, cantFilas+1)
		ws.write(cantFilas+5, 4, xlwt.Formula(valArticulosNoEntregados))

		valArticulosBoletas = 'SUMIF(G1:G%s;"x";E1:E%s)' % (cantFilas+1, cantFilas+1)
		ws.write(cantFilas+5, 5, xlwt.Formula(valArticulosBoletas))

		ws.write(cantFilas+7, 1, u"Total en códigos")

		cantArticulosCampania = 'COUNT(E1:E%s)' % (cantFilas+1)
		ws.write(cantFilas+7, 3, xlwt.Formula(cantArticulosCampania))

		cantArticulosNoEntregados = 'COUNTIF(F1:F%s;"x")' % (cantFilas+1)
		ws.write(cantFilas+7, 4, xlwt.Formula(cantArticulosNoEntregados))

		cantArticulosBoletas = 'COUNTIF(G1:G%s;"x")' % (cantFilas+1)
		ws.write(cantFilas+7, 5, xlwt.Formula(cantArticulosBoletas))

		ws.write(cantFilas+9, 0, "FECHA DE INICIO DE REPARTO")
		ws.write(cantFilas+9, 3, self.camp['ini_reparto'])
		ws.write(cantFilas+10, 0, "FECHA DE FIN DE REPARTO")
		ws.write(cantFilas+10, 3, self.camp['fin_reparto'])

		ws.write(cantFilas+12, 0, "A RENDIR")
		exp1 = "D%s" % (cantFilas+6)
		ws.write(cantFilas+12, 3, xlwt.Formula(exp1))

		ws.write(cantFilas+14, 0, "NO ENTREGADOS")
		exp1 = "E%s" % (cantFilas+6)
		ws.write(cantFilas+14, 3, xlwt.Formula(exp1))

		ws.write(cantFilas+15, 0, "BOLETAS INDIVIDUALES")
		exp1 = "F%s" % (cantFilas+6)
		ws.write(cantFilas+15, 3, xlwt.Formula(exp1))

		#Listado de depositos bancarios

		self.mdlEnv.ecam_anio = self.camp['anio']
		self.mdlEnv.ecam_num = self.camp['num']
		listadoEnv = self.mdlEnv.read_all()
		cantFilas2 = cantFilas + 16
		for i, dato in enumerate(listadoEnv):
			label = "%s° ENVIO" % (i+1)
			ws.write(cantFilas2, 0, label)
			ws.write(cantFilas2, 3, dato[4])
			ws.write(cantFilas2, 4, dato[3])
			cantFilas2 += 1

		ws.write(cantFilas2+1, 0, u"DISTRIBUCIÓN")
		ws.write(cantFilas2+2, 0, "OTROS")

		# Cargando Otros Gastos
		self.mdlGvar.icam_anio = self.camp['anio']
		self.mdlGvar.icam_num = self.camp['num']
		listadoGvar = self.mdlGvar.read_all()
		cantFilas3 = cantFilas2 + 3
		for dato in listadoGvar:
			ws.write(cantFilas3, 0, dato[5])
			ws.write(cantFilas3, 3, dato[4])
			cantFilas3 += 1

	
		ws.write(cantFilas3+3, 0, "DIFERENCIA ANTERIOR")
		ws.write(cantFilas3+3, 3, self.camp['diferencia'])

		ws.write(cantFilas3+5, 0, "SALDO")

		ws.write(cantFilas3+10, 0, "GASTOS DE DISTRIBUCION")
		ws.write(cantFilas3+11, 0, "A entregar")
		exp1 = "D%s" % (cantFilas+8)
		ws.write(cantFilas3+11, 3, xlwt.Formula(exp1))

		ws.write(cantFilas3+12, 0, "No entregados")
		exp1 = "E%s" % (cantFilas+8)
		ws.write(cantFilas3+12, 3, xlwt.Formula(exp1))

		ws.write(cantFilas3+13, 0, "Pedidos a cobrar")
		exp1 = "D%s - D%s" % (cantFilas3+12, cantFilas3+13)
		ws.write(cantFilas3+13, 3, xlwt.Formula(exp1))


		#DISTRIBUCION
		exp1 = "D%s * %s+ %s" % (cantFilas3+14, self.camp['parametro'], self.camp['base'])
		ws.write(cantFilas2+1, 3, xlwt.Formula(exp1))

		#SALDO
		exp1 = 'SUM(D%s: D%s)- D%s' % (cantFilas+15, cantFilas3+5, cantFilas+13)
		ws.write(cantFilas3+5, 3, xlwt.Formula(exp1))

		wb.save(self.dir)

class ModeloReporteDetalleCampania:

	def __init__(self, contenido, dir):
		self.contenido = contenido
		self.dir = dir
		locale.setlocale(locale.LC_ALL, 'spanish_spain') # Para que la fecha este es catelano.

	def generar_reporte(self):
		"""Crear libro y hoja xls"""
		wb = xlwt.Workbook(encoding='latin-1')
		ws = wb.add_sheet("Hoja1")

		ws.write(0, 0, u"Código")
		ws.write(0, 1, u"Apellido y nombre")
		ws.write(0, 2, u"Sección")
		ws.write(0, 3, u"Teléfono")
		ws.write(0, 4, u"Campaña")
		ws.write(0, 5, u"Deuda")
		ws.write(0, 6, u"Barrio")
		ws.write(0, 7, u"Localidad")

		
		for fila, dato in enumerate(self.contenido):
			ws.write(fila+1, 0, dato[0])
			ws.write(fila+1, 1, dato[1])
			try:
				ws.write(fila+1, 2, int(dato[2]))
			except:
				ws.write(fila+1, 2, dato[2])
			try:
				ws.write(fila+1, 3, int(dato[3]))
			except:
				ws.write(fila+1, 3, dato[3])
				
			ws.write(fila+1, 4, int(dato[4]))
			ws.write(fila+1, 5, dato[5])
			ws.write(fila+1, 6, dato[6])
			ws.write(fila+1, 7, dato[7])

		wb.save(self.dir)

class ModeloReporteDesmanteladoCampania:

	def __init__(self, contenido, dir):
		self.contenido = contenido
		self.dir = dir
		locale.setlocale(locale.LC_ALL, 'spanish_spain') # Para que la fecha este es catelano.

	def generar_reporte(self):
		"""Crear libro y hoja xls"""
		wb = xlwt.Workbook(encoding='latin-1')
		ws = wb.add_sheet("Hoja1")

		ws.write(0, 0, u"Código")
		ws.write(0, 1, u"Cant.")
		ws.write(0, 2, u"Apellido y nombre")
		ws.write(0, 3, u"Sección")
		ws.write(0, 4, u"Teléfono")
		ws.write(0, 5, u"Campaña")
		ws.write(0, 6, u"Deuda")
		ws.write(0, 7, u"Barrio")
		ws.write(0, 8, u"Localidad")

		
		for fila, dato in enumerate(self.contenido):
			ws.write(fila+1, 0, dato[0])
			ws.write(fila+1, 1, dato[1])
			ws.write(fila+1, 2, dato[2])
			try:
				ws.write(fila+1, 3, int(dato[3]))
			except:
				ws.write(fila+1, 3, dato[3])
			try:
				ws.write(fila+1, 4, int(dato[4]))
			except:
				ws.write(fila+1, 4, dato[4])
				
			ws.write(fila+1, 5, int(dato[5]))
			ws.write(fila+1, 6, dato[6])
			ws.write(fila+1, 7, dato[7])
			ws.write(fila+1, 8, dato[8])

		wb.save(self.dir)

class ModeloReporteRepartos:
	def __init__(self, dia, camp, contenido, dir):
		"""La variable contenido es de tipo dict {nombre ruta: [filas...]}"""
		self.dia = dia
		self.camp = camp
		self.contenido = contenido
		self.dir = dir
		locale.setlocale(locale.LC_ALL, 'spanish_spain') # Para que la fecha este es catelano.

	def generar_reporte(self):
		"""Crear libro y hoja xls"""
		wb = xlwt.Workbook(encoding='latin-1')
		mdlArt = ModeloArticulos()
		mdlCamp = ModeloCampanias()
		mdlLis = ModeloListados()
		
		mdlArt.cam_anio = self.camp['anio']
		mdlArt.cam_num = self.camp['numero']

		progresoMax = len(self.contenido)
		dialog = wx.ProgressDialog("Progreso", 
									"Generando ruta...", progresoMax, 
									style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
		band = True
		incremento = 0
		for nombre in self.contenido:
			ws = wb.add_sheet(nombre)

			estilo = xlwt.easyxf('font: bold on; align: vert centre, horiz left')

			ws.write(0, 0, u"REPARTO DIA: %s" % self.dia, estilo)

			ws.write(2, 0, u"ord", estilo)
			ws.col(0).width = len('ord__') * 256
			
			ws.write(2, 1, u"codigo", estilo)
			ws.write(2, 2, u"sec", estilo)
			ws.write(2, 3, u"apellido y nombre", estilo)
			ws.col(3).width = len('__apellido y nombre__') * 256

			ws.write(2, 4, u"deuda", estilo)
			ws.write(2, 5, u"localidad", estilo)
			ws.write(2, 6, u"domicilio", estilo)
			ws.write(2, 7, u"telefono", estilo)
			ws.write(2, 8, u"barrio", estilo)
			ws.write(2, 9, u"rec", estilo)
			ws.write(2, 10, u"estado", estilo)

			
			for fila, dato in enumerate(self.contenido[nombre]):
				ws.write(fila+3, 0, dato[0])
				ws.write(fila+3, 1, dato[1])
				if dato[2].strip().isdigit():
					ws.write(fila+3, 2, int(dato[2]))
				else:
					ws.write(fila+3, 2, dato[2])
				ws.write(fila+3, 3, dato[3])
				ws.write(fila+3, 4, dato[4])
				ws.write(fila+3, 5, dato[5])
				ws.write(fila+3, 6, dato[6])

				if dato[7].strip().isdigit():
					ws.write(fila+3, 7, int(dato[7]))
				else:
					ws.write(fila+3, 7, dato[7])

				ws.write(fila+3, 8, dato[8])

				mdlArt.cli_codigo = dato[1]
				
				hist = mdlArt.historial(12).split(',')[1:]
				cont = hist.count('A') + hist.count('S/B')
				ws.write(fila+3, 9, cont)

				if mdlArt.exist():
					if mdlArt.articulo_pagado() != 0:
						if str(mdlArt.articulo_entregado()) == "None":
							ws.write(fila+3, 10, u"Pagado")
						else:
							ws.write(fila+3, 10, u"E")
					elif dato[9] == 0:
						ws.write(fila+3, 10, u"")
					elif dato[9] == 1:
						ws.write(fila+3, 10, u"R/D")
					elif dato[9] == 2:
						ws.write(fila+3, 10, u"N/S")
					elif dato[9] == 3:
						ws.write(fila+3, 10, u"Lider")

					mdlLis.cam_anio = self.camp['anio']
					mdlLis.cam_num = self.camp['numero']
					mdlLis.numero = dato[11]
					lis = mdlLis.read()
					if lis:
						ws.write(fila+3, 11, lis['comentario'])
				else:
					ws.write(fila+3, 10, u"x")

			if band and incremento < progresoMax:
				incremento += 1
				band = dialog.Update(incremento)
		dialog.Destroy()
		wb.save(self.dir)

# -*- coding: utf-8 -*-
import time
import wx
from xlrd import Book, open_workbook
from modelRutas import ModeloRutas
from modelClientes import ModeloClientes
class ModeloXLRutas(Book):
	def __init__(self):
		self._dir = None
		self.mdlCli = ModeloClientes()

	def abrir_archivo_xls(self, dir=None):
		"""Realiza a apertura del archivo."""
		try: 
			self._wb = open_workbook(dir, formatting_info=True)
		except:
			return False
		else:
			self._dir = dir
			self._path = "/".join(dir.split("\\")[:-1])
			return True

	def nhojas(self):
		"""Retorna el numero de hojas en el archivo"""
		return self._wb.nsheets

	def hojas_nombres(self):
		"""Retorna una lista con los nombres de las hojas en el archivo."""
		return self._wb.sheet_names()

	def hojas(self):
		"""Retorna una lista con todas las hojas del archivo."""
		return self._wb.sheets()

	def hoja_por_nombre(self, nombre):
		"""Retorna una hoja cuyo nombre es pasado por parametro."""
		return self._wb.sheet_by_name(nombre)


	def formato_es_valido(self):
		"""
		Verifica si el formato de las hojas es correcto.
		Cada hoja debe contenes las columnas: """
		labels = ["ord", "codigo", "sec", "apellido y nombre", "deuda", "localidad", "domicilio", "telefono", "barrio", "rec", "estado"]
		valido = True
		for name in self._wb.sheet_names():
			ws = self._wb.sheet_by_name(name)
			for xcol, label in enumerate(labels):
				if ws.cell(2, xcol).value.lower() != label:
					valido = False
		return valido

	def migrar_a_base_de_datos(self):
		"""Se migraran los datos de los archivos XLS a la base de datos"""
	
		self.mdlRutas = ModeloRutas()
		progresoMax = self._wb.nsheets
		dialog = wx.ProgressDialog("Progreso de Carga", 
									"Migrando datos...", progresoMax, 
									style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
		band = True
		cont = 0
		for ruta_nombre in self._wb.sheet_names():
			ws = self._wb.sheet_by_name(ruta_nombre)

			ruta_orden = int(ws.cell(0, 0).value.split(":")[-1])

			# Verificamos si existe el titulo de ruta
			self.mdlRutas.rut_nombre = ruta_nombre.strip().upper()
			if not self.mdlRutas.exist():
				self.mdlRutas.rut_orden = ruta_orden
				self.mdlRutas.create()

			rut_id = self.mdlRutas.get_id()

			# Asociamos a los clientes a sus respectivas rutas.
			for rowx in range(3, ws.nrows):
				orden = ws.cell(rowx, 0)
				codigo =  ws.cell(rowx, 1)
				seccion = ws.cell(rowx, 2)
				apenom = ws.cell(rowx, 3)
				localidad =  ws.cell(rowx, 5)
				domicilio =  ws.cell(rowx, 6)
				telefono = ws.cell(rowx, 7)
				barrio =  ws.cell(rowx, 8)
				estado = ws.cell(rowx, 10)

				if codigo.value.strip() != "":
					self.mdlCli.codigo = codigo.value.strip()
					if self.mdlCli.exist():
						datos_cliente = self.mdlCli.read_with_ruta()

						self.mdlCli.codigo = datos_cliente['codigo']
						if apenom.value != "":
							self.mdlCli.apenom = apenom.value.upper()
						else:
							self.mdlCli.apenom = datos_cliente['nombre']
						
						try:
							self.mdlCli.seccion = str(int(seccion.value))
						except:
							self.mdlCli.seccion = datos_cliente['seccion']

						if domicilio.value != "":
							self.mdlCli.domicilio = domicilio.value.strip()
						else:
							self.mdlCli.domicilio = datos_cliente['domicilio']
						
						if barrio.value != "":
							self.mdlCli.barrio = barrio.value.strip()
						else:
							self.mdlCli.barrio = datos_cliente['barrio']
						
						if localidad.value != "":
							self.mdlCli.localidad = localidad.value.strip().upper()
						else:
							self.mdlCli.localidad = datos_cliente['localidad']

						if estado.value == "":
							self.mdlCli.referencia = 0
						elif estado.value.strip().upper() == "R/D":
							self.mdlCli.referencia = 1
						elif estado.value.strip().upper() == "N/S":
							self.mdlCli.referencia = 2
						elif estado.value.strip().upper() == "LIDER":
							self.mdlCli.referencia = 3			
						else:
							self.mdlCli.referencia = datos_cliente['referencia']

						self.mdlCli.descripcion = datos_cliente['descripcion']

						if type(telefono.value) in [ str, unicode ]:
							self.mdlCli.telefonos = telefono.value
						elif type(telefono.value) == float:
							self.mdlCli.telefonos = str(int(telefono.value))
						else:
							self.mdlCli.telefonos = datos_cliente['telefonos']
						
						
						# Asignacion de ruta y orden
						self.mdlCli.crut_id = rut_id
						if str(orden.value) != "":
							self.mdlCli.orden = int(orden.value)
						else:
							self.mdlCli.orden = datos_cliente['orden']

						self.mdlCli.zona = datos_cliente['zona']
						self.mdlCli.update()

			if band and cont < progresoMax:
				cont += 1
				band = dialog.Update(cont)
		dialog.Destroy()
		wx.MessageBox("Datos de ruta migrados con exito!", "Enhorabuena!")



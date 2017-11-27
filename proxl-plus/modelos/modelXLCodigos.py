# -*- coding: utf-8 -*-
'''
Nombre: modelXLCodigos.py
Autor: Ibarra Hector Leonel
'''
import re
from xlrd import open_workbook
import xlwt

class ModeloXLCodigos:
	def __init__(self):
		self.dir = ""
		self.patronCodigo = re.compile('^(\d\d\d/\d\d)$')

	def traerLibro(self):
		try:
			self.Libro = open_workbook(self.dir, formatting_info=True)
			self.Hoja = self.Libro.sheet_by_index(0)
		except:
			return False
		else:
			return True

	def obtenerCodigos(self):
		"""Carga los datos en una matriz virtual."""
		listado = []
		columnaCodigos = self.Hoja.col(1)
		for i, c in enumerate(columnaCodigos):
			if self.patronCodigo.match(c.value.strip()) != None:
				contenido = {}
				fila = self.Hoja.row(i)
				contenido["codigo"] = fila[1].value.strip()
				contenido["localidad"] = fila[2].value.strip()
				contenido["campania"] = str(int(fila[3].value))
				contenido["deuda"] = fila[4].value

				listado.append(contenido)
		return listado





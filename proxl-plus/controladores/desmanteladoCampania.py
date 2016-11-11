# -*- coding: utf-8 -*-
import wx
from vistas.frame_desmantelado_campania import FrameDesmanteladoCampania 

from modelos.modelArticulos import ModeloArticulos
from modelos.modelReporte import ModeloReporteDesmanteladoCampania

class ControladorDesmanteladoCampania:
	mdlArt = ModeloArticulos()

	def __init__(self, parent, camp):
		self.parent = parent
		self.camp = camp

	def run(self):
		self.frame = FrameDesmanteladoCampania(self.parent)
		self.capturarEventos()
		self.cargarDatos()
		self.frame.ShowModal()

	def capturarEventos(self):
		self.frame.grilla.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.ModificarCant)
		self.frame.btn_generar.Bind(wx.EVT_BUTTON, self.GenerarReporte)

	def cargarDatos(self):
		self.mdlArt.cam_anio = self.camp['anio']
		self.mdlArt.cam_num = self.camp['numero']
		self.lista = self.mdlArt.listarNoCobradosNoEntregados()
		self.cargarGrilla(self.lista)

	def cargarGrilla(self, listado):
		tam = len(listado)
		self.frame.grilla.AppendRows(tam)
		self.configurarGrilla(tam)
		for i in range(tam):
			self.frame.grilla.SetRowSize(i, 25)
			self.frame.grilla.SetCellValue(i, 0, str(listado[i][0]))
			self.frame.grilla.SetCellValue(i, 1, str(listado[i][1]))
			self.frame.grilla.SetCellValue(i, 2, str(listado[i][2]))
			self.frame.grilla.SetCellValue(i, 3, str(listado[i][3]))
			self.frame.grilla.SetCellValue(i, 4, str(listado[i][4]))
			self.frame.grilla.SetCellValue(i, 5, str(listado[i][5]))
			self.frame.grilla.SetCellValue(i, 6, str(listado[i][6]))
			self.frame.grilla.SetCellValue(i, 7, str(listado[i][7]))
			self.frame.grilla.SetCellValue(i, 8, str(listado[i][8]))

	def configurarGrilla(self, filas):
		"""Este modulo se encarga de deshabilitar las celdas que no
			deben ser editables."""
		columnas = self.frame.grilla.GetNumberCols()
		for j in range(columnas):
			if j != 1:
				for i in range(filas):
					self.frame.grilla.SetReadOnly(i, j, True)

	def ModificarCant(self, event):
		self.mdlArt.cli_codigo = self.frame.grilla.GetCellValue(event.GetRow(), 0)
		if self.frame.grilla.GetCellValue(event.GetRow(), 1).isdigit() and len(self.frame.grilla.GetCellValue(event.GetRow(), 1)) <= 2:
			self.mdlArt.cant = int(self.frame.grilla.GetCellValue(event.GetRow(), 1))
		else:
			self.mdlArt.cant = 0
		self.mdlArt.updateStock()

	def GenerarReporte(self, event):
		nombreArchivo = "/Desmantelado.xls"
		dialog = wx.DirDialog(self.frame, "SELECCIONAR CARPETA DE DESTINO:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
		rta = dialog.ShowModal()
		if rta == wx.ID_OK:
			dir = dialog.GetPath()
			
			dir = dir + nombreArchivo
			mdlMRDC = ModeloReporteDesmanteladoCampania(self.lista, dir)
			try:
				mdlMRDC.generar_reporte()
			except:
				wx.MessageBox("Ha ocurrido un error al generar reporte.", "Ups!")
			else:
				wx.MessageBox("El reporte ha sido generado con exito.", "Enhorabuena!")

		dialog.Destroy()
# -*- coding: utf-8 -*-
import wx
from vistas.frame_detalle_campania import FrameDetalleCampania 

from modelos.modelArticulos import ModeloArticulos
from modelos.modelReporte import ModeloReporteDetalleCampania

class ControladorCobradosEfectivoCampania:

	mdlArt = ModeloArticulos()

	def __init__(self, parent, camp):
		self.parent = parent
		self.camp = camp

	def run(self):
		self.frame = FrameDetalleCampania(self.parent)
		self.capturarEventos()
		self.cargarDatos()
		self.frame.ShowModal()

	def capturarEventos(self):
		self.frame.btn_generar.Bind(wx.EVT_BUTTON, self.GenerarReporte)

	def cargarDatos(self):
		self.mdlArt.cam_anio = self.camp['anio']
		self.mdlArt.cam_num = self.camp['numero']
		#Efectivo
		self.titulo = u"Cobrados en efectivo"
		self.frame.st_titulo.SetLabel(self.titulo)
		self.lista = self.mdlArt.listarCobradosEfectivo()
		self.cargarGrilla(self.lista)
		

	def cargarGrilla(self, listado):
		tam = len(listado)
		self.frame.grilla.AppendRows(tam)
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

	def GenerarReporte(self, event):
		nombreArchivo = "/%s.xls" % (self.titulo)
		dialog = wx.DirDialog(self.frame, "SELECCIONAR CARPETA DE DESTINO:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
		rta = dialog.ShowModal()
		if rta == wx.ID_OK:
			dir = dialog.GetPath()
			
			dir = dir + nombreArchivo
			mdlMRDC = ModeloReporteDetalleCampania(self.lista, dir)
			try:
				mdlMRDC.generar_reporte()
			except:
				wx.MessageBox("Ha ocurrido un error al generar reporte.", "Ups!")
			else:
				wx.MessageBox("El reporte ha sido generado con exito.", "Enhorabuena!")

		dialog.Destroy()



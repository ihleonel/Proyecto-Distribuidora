# -*- coding: utf-8 -*-
import wx
import time
from vistas.frame_resultado_campania import FrameResultadoCampania
from modelos.modelArticulos import ModeloArticulos
from modelos.modelCampanias import ModeloCampanias
from modelos.modelReporte import ModeloReporte

from controladores.desmanteladoCampania import ControladorDesmanteladoCampania
from controladores.cobradosEfectivoCampania import ControladorCobradosEfectivoCampania
from controladores.cobradosBoletaCampania import ControladorCobradosBoletaCampania
from controladores.cobradosReciboCampania import ControladorCobradosReciboCampania
from controladores.cobradosEfectivoNoEntregadosCampania import ControladorCobradosEfectivoNoEntregadosCampania
from controladores.noCobradosEntregadosCampania import ControladorNoCobradosEntregadosCampania

class ControladorResultadoCampania:
	mdlArt = ModeloArticulos()
	mdlCamp = ModeloCampanias()
	def __init__(self, parent, camp):
		self.parent = parent
		self.camp = camp

	def run(self):
		self.frame = FrameResultadoCampania(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		self.frame.btn_volver.SetFocus()
		self.configurarGrilla()
		self.cargarGrilla()
		self.cargarDatos()
		self.capturarEventos()
		self.frame.Show()

	def capturarEventos(self):
		self.frame.btn_volver.Bind(wx.EVT_BUTTON, self.Volver)
		self.frame.btn_generar.Bind(wx.EVT_BUTTON, self.Generar)

		self.frame.grilla.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.Detalle)

	def configurarGrilla(self):
		self.frame.grilla.SetCellSize(0, 0, 3, 1)
		self.frame.grilla.SetCellSize(0, 1, 1, 6)
		self.frame.grilla.SetCellSize(1, 1, 1, 2)
		self.frame.grilla.SetCellSize(1, 3, 1, 2)
		self.frame.grilla.SetCellSize(1, 5, 1, 2)
		self.frame.grilla.SetCellSize(0, 7, 2, 2)

		self.frame.grilla.SetCellBackgroundColour(1, 1, '#81de1e')
		self.frame.grilla.SetCellBackgroundColour(1, 3, '#81de1e')
		self.frame.grilla.SetCellBackgroundColour(1, 5, '#81de1e')
		self.frame.grilla.SetCellBackgroundColour(3, 7, '#81de1e')
		self.frame.grilla.SetCellBackgroundColour(4, 1, '#81de1e')
		self.frame.grilla.SetCellBackgroundColour(4, 7, '#81de1e')

	def configurarGrilla2(self):
		pass

	def cargarGrilla(self):
		self.frame.grilla.SetCellValue(3, 0, "ENTREGADOS")
		self.frame.grilla.SetCellValue(4, 0, "NO ENTREGADOS")
		self.frame.grilla.SetCellValue(5, 0, "SUBTOTALES")

		self.frame.grilla.SetCellValue(0, 1, "COBRADOS")
		self.frame.grilla.SetCellValue(1, 1, "EFECTIVO")
		self.frame.grilla.SetCellValue(1, 3, "BOLETAS")
		self.frame.grilla.SetCellValue(1, 5, "RECIBO OFICINA")
		self.frame.grilla.SetCellValue(0, 7, "NO COBRADOS")

		self.frame.grilla.SetCellValue(2, 1, u"códigos")
		self.frame.grilla.SetCellValue(2, 2, "$")
		self.frame.grilla.SetCellValue(2, 3, u"códigos")
		self.frame.grilla.SetCellValue(2, 4, "$")
		self.frame.grilla.SetCellValue(2, 5, u"códigos")
		self.frame.grilla.SetCellValue(2, 6, "$")
		self.frame.grilla.SetCellValue(2, 7, u"códigos")
		self.frame.grilla.SetCellValue(2, 8, "$")

		self.mdlArt.cam_anio = self.camp['anio']
		self.mdlArt.cam_num = self.camp['numero']

		resultados = self.mdlArt.result_campaign()

		# cantidades Articulos
		self.frame.grilla.SetCellValue(3, 1, str(resultados['entregadosEfectivo']))
		self.frame.grilla.SetCellValue(4, 1, str(resultados['noEntregadosEfectivo']))
		self.frame.grilla.SetCellValue(5, 1, str(resultados['cobradosEfectivo']))

		self.frame.grilla.SetCellValue(3, 3, str(resultados['entregadosBoleta']))
		self.frame.grilla.SetCellValue(4, 3, str(resultados['noEntregadosBoleta']))
		self.frame.grilla.SetCellValue(5, 3, str(resultados['cobradosBoleta']))

		self.frame.grilla.SetCellValue(3, 5, str(resultados['entregadosOficina']))
		self.frame.grilla.SetCellValue(4, 5, str(resultados['noEntregadosOficina']))
		self.frame.grilla.SetCellValue(5, 5, str(resultados['cobradosOficina']))

		self.frame.grilla.SetCellValue(3, 7, str(resultados['entregadosNoCobrados']))
		self.frame.grilla.SetCellValue(4, 7, str(resultados['noEntregadosNoCobrados']))
		self.frame.grilla.SetCellValue(5, 7, str(resultados['noCobrados']))

		# valores Articulos

		self.frame.grilla.SetCellValue(3, 2, str(resultados['valEntregadosEfectivo']))
		self.frame.grilla.SetCellValue(4, 2, str(resultados['valNoEntregadosEfectivo']))
		self.frame.grilla.SetCellValue(5, 2, str(resultados['valEfectivo']))

		self.frame.grilla.SetCellValue(3, 4, str(resultados['valEntregadosBoleta']))
		self.frame.grilla.SetCellValue(4, 4, str(resultados['valNoEntregadosBoleta']))
		self.frame.grilla.SetCellValue(5, 4, str(resultados['valBoleta']))

		self.frame.grilla.SetCellValue(3, 6, str(resultados['valEntregadosOficina']))
		self.frame.grilla.SetCellValue(4, 6, str(resultados['valNoEntregadosOficina']))
		self.frame.grilla.SetCellValue(5, 6, str(resultados['valOficina']))

		self.frame.grilla.SetCellValue(3, 8, str(resultados['valEntregadosNoCobrados']))
		self.frame.grilla.SetCellValue(4, 8, str(resultados['valNoEntregadosNoCobrados']))
		self.frame.grilla.SetCellValue(5, 8, str(resultados['valNoCobrados']))

		# cargando grilla 2
		self.frame.grilla2.SetCellValue(1, 0, u"Total en $")
		self.frame.grilla2.SetCellValue(2, 0, u"Total en códigos")
		self.frame.grilla2.SetCellValue(0, 1, "DEUDA")
		self.frame.grilla2.SetCellValue(0, 2, "NO ENTR")
		self.frame.grilla2.SetCellValue(0, 3, "BOLETA")

		self.frame.grilla2.SetCellValue(1, 1, str(resultados['valArticulosCampania']))
		self.frame.grilla2.SetCellValue(1, 2, str(resultados['valArticulosNoEntregados']))
		self.frame.grilla2.SetCellValue(1, 3, str(resultados['valArticulosBoletas']))
		
		self.frame.grilla2.SetCellValue(2, 1, str(resultados['cantArticulosCampania']))
		self.frame.grilla2.SetCellValue(2, 2, str(resultados['cantArticulosNoEntregados']))
		self.frame.grilla2.SetCellValue(2, 3, str(resultados['cantArticulosBoletas']))


	def cargarDatos(self):
		self.mdlCamp.anio = self.camp['anio']
		self.mdlCamp.num = self.camp['numero']
		self.dCamp = self.mdlCamp.read()
		self.titulo = str(self.camp['numero']) + "-"+str(self.camp['anio'])
		self.frame.tc_campania.SetValue(self.titulo)
		self.frame.tc_inicio.SetValue(self.dCamp['inicio'])

	"Evento de ventana"
	def Volver(self, event):
		self.frame.Destroy()

	def Generar(self, event):
		nombreArchivo = "/Camp %s__%s .xls" % (self.titulo, time.strftime("%d-%m-%Y"))
		dialog = wx.DirDialog(self.frame, "SELECCIONAR CARPETA DE DESTINO:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
		rta = dialog.ShowModal()
		if rta == wx.ID_OK:
			dir = dialog.GetPath()
			
			dir = dir + nombreArchivo
			mdlRep = ModeloReporte(dir, self.camp)
			try:
				mdlRep.generar_libro()
			except:
				wx.MessageBox("Ha ocurrido un error al generar reporte.", "Ups!")
			else:
				wx.MessageBox("El reporte ha sido generado con exito.", "Enhorabuena!")

		dialog.Destroy()

	def Detalle(self, event):
		celda = (event.GetRow(), event.GetCol())
		if celda == (1, 1):# Cobradas en efectivo
			cobEfCamp = ControladorCobradosEfectivoCampania(self.frame, self.camp)
			cobEfCamp.run()
		elif celda == (1, 3):# Cobradas por boleta unica
			cobBoCamp = ControladorCobradosBoletaCampania(self.frame, self.camp)
			cobBoCamp.run()
		elif celda == (1, 5):# Cobrados por recibo oficina
			cobReCamp = ControladorCobradosReciboCampania(self.frame, self.camp)
			cobReCamp.run()
		elif celda == (3, 7):# No cobrados entregados
			noCoEntr = ControladorNoCobradosEntregadosCampania(self.frame, self.camp)
			noCoEntr.run()
		elif celda == (4, 1):# Cobrados en efectivo no entregados
			cobEfNoEntrCamp = ControladorCobradosEfectivoNoEntregadosCampania(self.frame, self.camp)
			cobEfNoEntrCamp.run()
		elif celda == (4, 7):# Desmantelado
			desCamp = ControladorDesmanteladoCampania(self.frame, self.camp)
			desCamp.run()
		
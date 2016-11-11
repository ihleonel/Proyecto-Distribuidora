# -*- coding : utf-8 -*-
import wx
from vistas.frame_campanias import FrameCampanias
from modelos.modelCampanias import ModeloCampanias
from controladores.resultadosCampania import ControladorResultadoCampania

class ControladorCampanias:
	mdlCampanias = ModeloCampanias()

	def __init__(self, parent, usuario):
		self.parent = parent
		self.usuario = usuario
		self.listadoCampanias = self.mdlCampanias.read_all()
		self.Seleccionado = {}

	def run(self):
		self.frame = FrameCampanias(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))

		self.capturarEventos()
		self.configurarGrilla(len(self.listadoCampanias))
		self.cargarGrilla(self.listadoCampanias)
		self.deshabilitaBTNS()
		self.frame.Show()

	def capturarEventos(self):
		self.frame.btn_ver.Bind(wx.EVT_BUTTON, self.Ver)
		self.frame.btn_buscar.Bind(wx.EVT_BUTTON, self.Buscar)
		self.frame.btn_volver.Bind(wx.EVT_BUTTON, self.Volver)
		self.frame.grilla.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.f_seleccion_fila)

	def configurarGrilla(self, tam):
		self.frame.grilla.SetSelectionMode(wx.grid.Grid.SelectRows)
		self.frame.grilla.AppendRows(tam)
		presentador = wx.grid.GridCellAutoWrapStringRenderer
		for i in range(tam):
			self.frame.grilla.SetRowSize(i, 25)
			self.frame.grilla.SetCellRenderer(i, 1, presentador())

	def cargarGrilla(self, listado):
		for i in range(len(listado)):
			self.frame.grilla.SetCellValue(i, 0, str(listado[i][0]))
			self.frame.grilla.SetCellValue(i, 1, str(listado[i][1]))
			self.frame.grilla.SetCellValue(i, 2, str(listado[i][2]))
			self.frame.grilla.SetCellValue(i, 3, str(listado[i][4]))

	def limpiarGrilla(self):
		for i in range(self.frame.grilla.GetNumberRows()):
			self.frame.grilla.DeleteRows(0, 1)

	def refrescar_grilla(self, listado):
		self.limpiarGrilla()
		self.configurarGrilla(len(listado))
		self.cargarGrilla(listado)


	'''Eventos de Botones'''

	def Buscar(self, event):
		if self.isint(self.frame.tc_anio.GetValue()):
			if self.isint(self.frame.tc_numero.GetValue()):
				self.mdlCampanias.anio = int(self.frame.tc_anio.GetValue())
				self.mdlCampanias.num = int(self.frame.tc_numero.GetValue())
				self.listadoCampanias = self.mdlCampanias.read_x_anio_num()
				self.refrescar_grilla(self.listadoCampanias)
			else:
				self.mdlCampanias.anio = int(self.frame.tc_anio.GetValue())
				self.listadoCampanias = self.mdlCampanias.read_x_anio()
				self.refrescar_grilla(self.listadoCampanias)



	def Volver(self, event):
		self.frame.Destroy()

	def Ver(self, event):
		verCamp = ControladorResultadoCampania(self.frame, self.Seleccionado)
		verCamp.run()

	'''Habilitar/Deshabilitar Botones'''

	def deshabilitaBTNS(self):
		self.frame.btn_ver.Enable(False)
		
	def habilitarBTNS(self):
		self.frame.btn_ver.Enable(True)

	'''Eventos de Grilla'''

	def f_seleccion_fila(self, event):
		fila = event.GetRow()
		try:
			self.Seleccionado['anio'] = int(self.frame.grilla.GetCellValue(fila, 0))
			self.Seleccionado['numero'] = int(self.frame.grilla.GetCellValue(fila, 1))
			self.habilitarBTNS()
		except:
			pass
		event.Skip()

	def isint(self, n):
		try:
			int(n)
			return True
		except:
			return False
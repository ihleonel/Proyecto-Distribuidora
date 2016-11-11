# -*- coding : utf-8 -*-
import wx
from vistas.frame_listados import FrameListados
from controladores.agregarListado import ControladorAgregarListado
from controladores.modificarListado import ControladorModificarListado
from controladores.eliminarListado import ControladorEliminarListado
from modelos.modelListados import ModeloListados

class ControladorListados:
	mdlList = ModeloListados()
	def __init__(self, parent, camp):
		self.parent = parent
		self.aCamp = camp

	def run(self):
		self.frame = FrameListados(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		self.cargarDatos()
		self.capturarEventos()
		self.frame.ShowModal()

	def capturarEventos(self):
		self.frame.btn_agregar.Bind(wx.EVT_BUTTON, self.Agregar)
		self.frame.btn_modificar.Bind(wx.EVT_BUTTON, self.Modificar)
		self.frame.btn_eliminar.Bind(wx.EVT_BUTTON, self.Eliminar)
		self.frame.grilla.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.f_seleccion_fila)

	"Eventos"

	def Agregar(self, event):
		agreLis = ControladorAgregarListado(self.frame, self.aCamp)
		agreLis.run()
		self.refrescar_grilla()
		self.DeshabilitarBTNS()

	def Modificar(self, event):
		modList = ControladorModificarListado(self.frame, self.aCamp, self.numList)
		modList.run()
		self.refrescar_grilla()
		self.DeshabilitarBTNS()

	def Eliminar(self, event):
		elimList = ControladorEliminarListado(self.frame, self.aCamp, self.numList)
		elimList.run()
		self.refrescar_grilla()
		self.DeshabilitarBTNS()


	def cargarDatos(self):
		t = str(self.aCamp['numero'])+'-'+str(self.aCamp['anio'])
		self.frame.st_campania.SetLabel(t)

		self.mdlList.cam_anio = self.aCamp['anio']
		self.mdlList.cam_num = self.aCamp['numero']
		self.Listados = self.mdlList.read_all()

		if self.Listados != ():
			self.cargarGrilla(self.Listados)

	def configurar_grilla(self, tam):
		self.frame.grilla.SetSelectionMode(wx.grid.Grid.SelectRows)
		self.frame.grilla.AppendRows(tam)
		presentador = wx.grid.GridCellAutoWrapStringRenderer
		for i in range(tam):
			self.frame.grilla.SetRowSize(i, 25)
			self.frame.grilla.SetCellRenderer(i, 2, presentador())

	def cargarGrilla(self, listado):
		self.configurar_grilla(len(listado))
		for i in range(len(listado)):
			self.frame.grilla.SetCellValue(i, 0, self.date_format(listado[i][3]))
			self.frame.grilla.SetCellValue(i, 1, str(listado[i][2]))
			self.frame.grilla.SetCellValue(i, 2, str(listado[i][4]))

	def limpiar_grilla(self):
		for i in range(self.frame.grilla.GetNumberRows()):
			self.frame.grilla.DeleteRows(0, 1)

	def refrescar_grilla(self):
		self.limpiar_grilla()
		self.Listados = self.mdlList.read_all()
		self.cargarGrilla(self.Listados)

	"habilitar/desabilitar botones"

	def habilitarBTNS(self):
		self.frame.btn_modificar.Enable(True)
		self.frame.btn_eliminar.Enable(True)	

	def DeshabilitarBTNS(self):
		self.frame.btn_modificar.Enable(False)
		self.frame.btn_eliminar.Enable(False)

	def f_seleccion_fila(self, event):
		fila = event.GetRow()
		try:
			self.numList = int(self.frame.grilla.GetCellValue(fila, 1))
			self.habilitarBTNS()
		except:
			pass
		event.Skip()

	def date_format(self, s):
		s = str(s)
		l = s.split("-")
		l[0], l[2] = l[2], l[0]
		return "-".join(l)

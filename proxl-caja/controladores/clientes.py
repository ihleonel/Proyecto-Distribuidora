# -*- coding: utf-8 -*-
import wx
from vistas.frame_caja_clientes import FrameClientes

from controladores.infoCliente import ControladorInfoCliente

from modelos.modelCampanias import ModeloCampanias
from modelos.modelArticulos import ModeloArticulos

class ControladorClientes:
	mdlCamp = ModeloCampanias()
	mdlArt = ModeloArticulos()

	def __init__(self, parent, datosCaja):
		self.parent = parent
		self.datosCaja = datosCaja

	def run(self):
		self.frame = FrameClientes(self.parent.frame)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))

		self.frame.tc_dato_busqueda.SetFocus()
		self.capturarEventos()
		self.frame.Show()

	def capturarEventos(self):
		self.frame.btn_buscar.Bind(wx.EVT_BUTTON, self.Buscar)
		self.frame.tc_dato_busqueda.Bind(wx.EVT_TEXT_ENTER, self.Buscar)
		self.frame.tc_dato_busqueda.Bind(wx.EVT_TEXT, self.AutoCompletar)
		self.frame.btn_continuar.Bind(wx.EVT_BUTTON, self.Continuar)
		self.frame.grilla.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.f_seleccion_fila)
		self.frame.grilla.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.Continuar)
		self.frame.btn_volver.Bind(wx.EVT_BUTTON, self.Volver)
		

	"Eventos"

	def Volver(self, event):
		self.frame.Destroy()
		
	def Buscar(self, event):
		# Primero verificamos que existe una campaña activa.
		campania = self.mdlCamp.get_active_campaign()
		if campania != {}:
			# Verificamos que el tipo de busqueda es por codigo.
			if self.frame.rb_codigo.GetValue() == True:
				# Tipo de busqueda por codigo.
				self.mdlArt.cam_anio = campania['anio']
				self.mdlArt.cam_num = campania['numero']
				self.mdlArt.cli_codigo = self.frame.tc_dato_busqueda.GetValue()
				self.datosCli = self.mdlArt.read()
				# Verificamos si existe un articulo para ese codigo.
				if self.datosCli != {}:
					# Si existe mostramos los datos en la proxima pantalla.
					self.Continuar()
					self.frame.tc_dato_busqueda.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
					self.frame.tc_dato_busqueda.Refresh()
				else:
					# Si no existe.
					self.frame.tc_dato_busqueda.SetBackgroundColour("pink")
					self.frame.tc_dato_busqueda.SetFocus()
					self.frame.tc_dato_busqueda.Refresh()
			else:
				# Tipo de busqueda es por apellido y nombre.
				self.mdlArt.cam_anio = campania['anio']
				self.mdlArt.cam_num = campania['numero']
				self.mdlArt.cli_apenom = self.frame.tc_dato_busqueda.GetValue()
				self.refrescar_grilla()
				self.frame.btn_continuar.Enable(False)
		else:
			wx.MessageBox(u"No se ha encontrado una campaña activa.\nPor favor compruebe que exista una campaña \nabierta.", "No existe campaña activa!")

	def AutoCompletar(self, event):
		if self.frame.rb_codigo.GetValue():
			prefijo = self.frame.tc_dato_busqueda.GetValue()
			if len(prefijo) == 4:
				sufijo = prefijo[-1]
				if sufijo != "/": 
					prefijo = prefijo[:3] + "/"
					prefijo += sufijo
					self.frame.tc_dato_busqueda.SetValue(prefijo)
			self.frame.tc_dato_busqueda.SetInsertionPoint(len(prefijo))
			event.Skip()
	
	def Continuar(self, event = None):
		campania = self.mdlCamp.get_active_campaign()
		if campania != {}:
			infoCli = ControladorInfoCliente(self.frame, self.datosCaja, self.datosCli)
			infoCli.run()
			self.frame.tc_dato_busqueda.SelectAll()
			self.parent.refrescar_grilla_uno()
			self.parent.refrescar_resultados()
			self.parent.panelUno.btn_modificar.Enable(False)
		else:
			wx.MessageBox(u"No se ha encontrado una campaña activa.\nPor favor compruebe que exista una campaña \nabierta.", "No existe campaña activa!")

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
			self.frame.grilla.SetCellValue(i, 0, str(listado[i]['codigo']))
			self.frame.grilla.SetCellValue(i, 1, str(listado[i]['nombre']))
			self.frame.grilla.SetCellValue(i, 2, str(listado[i]['domicilio']))

	def limpiar_grilla(self):
		for i in range(self.frame.grilla.GetNumberRows()):
			self.frame.grilla.DeleteRows(0, 1)

	def refrescar_grilla(self):
		self.limpiar_grilla()
		self.listadoCampanias = self.mdlArt.read_for_name()
		if self.listadoCampanias != ():
			self.frame.tc_dato_busqueda.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
			self.frame.tc_dato_busqueda.SetFocus()
			self.frame.tc_dato_busqueda.Refresh()
			self.cargarGrilla(self.listadoCampanias)
		else:
			self.frame.tc_dato_busqueda.SetBackgroundColour("pink")
			self.frame.tc_dato_busqueda.SetFocus()
			self.frame.tc_dato_busqueda.Refresh()
			self.frame.btn_conrinuar.Enable(False)

	def f_seleccion_fila(self, event):
		fila = event.GetRow()
		try:
			self.mdlArt.cli_codigo = self.frame.grilla.GetCellValue(fila, 0)
			self.datosCli = self.mdlArt.read()
			self.frame.btn_continuar.Enable(True)
		except:
			pass
		event.Skip()
	


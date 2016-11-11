# -*- coding: utf-8 -*-
import wx
from vistas.frame_principal import FramePrincipal
from vistas.panel_uno import PanelUno
from vistas.panel_dos import PanelDos

from controladores.clientes import ControladorClientes
from controladores.campanias import ControladorCampanias
from controladores.usuarios import ControladorUsuarios
from controladores.rutas import ControladorRutas
from controladores.historial import ControladorHistorial

from controladores.crearCampania import ControladorCrearCampania
from controladores.cerrarCampania import ControladorCerrarCampania
from controladores.verCampania import ControladorVerCampania
from controladores.modificarCampania import ControladorModificarCampania
from controladores.listados import ControladorListados
from controladores.repartos import ControladorRepartos
from controladores.gastosVarios import ControladorGastosVarios
from controladores.depositos import ControladorDepositos


from controladores.agregarListado import ControladorAgregarListado
from controladores.informacion import ControladorInformacion
from controladores.resultadosCampania import ControladorResultadoCampania

from modelos.modelCampanias import ModeloCampanias
from modelos.modelArticulos import ModeloArticulos

class ControladorPrincipal:
	mdlCamp = ModeloCampanias()
	mdlArt = ModeloArticulos()
	def __init__(self, usuario):
		self.usuario = usuario

	def run(self):
		self.frame = FramePrincipal(None)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		self.panelUno = PanelUno(self.frame.notebook)
		self.panelDos = PanelDos(self.frame.notebook)

		self.capturarEventos()

		self.frame.notebook.AddPage(self.panelUno, u"Campaña actual", False)
		self.frame.notebook.AddPage(self.panelDos, u"Menú", False)

		self.cargarDatos()

		self.frame.Show()

	def capturarEventos(self):
		"""Eventos de Frame"""
		self.frame.btn_salir.Bind(wx.EVT_BUTTON, self.Salir)

		"""Eventos de Panel Uno"""
		self.panelUno.btn_buscar.Bind(wx.EVT_BUTTON, self.Buscar)
		self.panelUno.btn_crear_campania.Bind(wx.EVT_BUTTON, self.CrearCampania)
		self.panelUno.btn_cerrar_campania.Bind(wx.EVT_BUTTON, self.CerrarCampania)
		self.panelUno.btn_modificar_campania.Bind(wx.EVT_BUTTON, self.ModificarCampania)
		self.panelUno.btn_listados.Bind(wx.EVT_BUTTON, self.Listados)
		self.panelUno.btn_repartos.Bind(wx.EVT_BUTTON, self.Repartos)
		self.panelUno.btn_gastos.Bind(wx.EVT_BUTTON, self.Gastos)
		self.panelUno.btn_depositos.Bind(wx.EVT_BUTTON, self.Envios)
		self.panelUno.tc_codigo.Bind(wx.EVT_TEXT_ENTER, self.Buscar)
		self.panelUno.tc_codigo.Bind(wx.EVT_TEXT, self.AutoCompletar)
		self.panelUno.btn_resultados_campania.Bind(wx.EVT_BUTTON, self.ResultCampania)

		"""Eventos de Panel Dos"""
		self.panelDos.btn_campanias.Bind(wx.EVT_BUTTON, self.Campanias)
		self.panelDos.btn_usuarios.Bind(wx.EVT_BUTTON, self.Usuarios)
		self.panelDos.btn_clientes.Bind(wx.EVT_BUTTON, self.Clientes)
		self.panelDos.btn_historial.Bind(wx.EVT_BUTTON, self.Historial)
		self.panelDos.btn_rutas.Bind(wx.EVT_BUTTON, self.Rutas)

	"""Eventos de Frame"""
	def Salir(self, event):
		self.frame.Destroy()

	"""Eventos de Panel Uno"""
	def Buscar(self, event):
		self.mdlArt.cam_anio = self.aCamp['anio']
		self.mdlArt.cam_num = self.aCamp['numero']
		cod = self.panelUno.tc_codigo.GetValue()
		self.mdlArt.cli_codigo = cod
		if self.mdlArt.exist():
			self.panelUno.tc_codigo.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
			self.panelUno.tc_codigo.SetFocus()
			self.panelUno.tc_codigo.Refresh()
			info = ControladorInformacion(self.frame, self.aCamp, cod)
			info.run()
			self.panelUno.tc_codigo.SelectAll()
		else:
			self.panelUno.tc_codigo.SetBackgroundColour("pink")
			self.panelUno.tc_codigo.SetFocus()
			self.panelUno.tc_codigo.Refresh()
		event.Skip()

	def AutoCompletar(self, event):
		prefijo = self.panelUno.tc_codigo.GetValue()
		if len(prefijo) == 4:
			sufijo = prefijo[-1]
			if sufijo != "/": 
				prefijo = prefijo[:3] + "/"
				prefijo += sufijo
				self.panelUno.tc_codigo.SetValue(prefijo)
		self.panelUno.tc_codigo.SetInsertionPoint(len(prefijo))
		event.Skip()

	def CrearCampania(self, event):
		crearCamp = ControladorCrearCampania(self.frame, self.usuario)
		crearCamp.run()
		self.cargarDatos()

	def ModificarCampania(self, event):
		modifCampania = ControladorModificarCampania(self.frame, self.aCamp)
		modifCampania.run()
		self.cargarDatos()

	def CerrarCampania(self, event):
		cerrarCamp = ControladorCerrarCampania(self.frame, self.aCamp)
		cerrarCamp.run()
		self.cargarDatos()

	def Listados(self, event):
		listados = ControladorListados(self.frame, self.aCamp)
		listados.run()

	def Repartos(self, event):
		repartos = ControladorRepartos(self.frame, self.aCamp)
		repartos.run()

	def Gastos(self, event):
		gastos = ControladorGastosVarios(self.frame, self.aCamp)
		gastos.run()

	def Envios(self, event):
		envios = ControladorDepositos(self.frame, self.aCamp)
		envios.run()

	def ResultCampania(self, event):
		resCamp = ControladorResultadoCampania(self.frame, self.aCamp)
		resCamp.run()

	def cargarDatos(self):
		if self.mdlCamp.get_active_campaign() != {}:

			self.panelUno.btn_crear_campania.Enable(False)
			self.panelUno.tc_codigo.SetFocus()

			self.aCamp = self.mdlCamp.get_active_campaign()
			texto = str(self.aCamp['numero']) +'-'+ str(self.aCamp['anio'])
			self.panelUno.st_campania.SetLabel(texto)

			self.panelUno.tc_codigo.Enable(True)
			self.panelUno.btn_listados.Enable(True)
			self.panelUno.btn_modificar_campania.Enable(True)
			self.panelUno.btn_cerrar_campania.Enable(True)
			self.panelUno.btn_buscar.Enable(True)
			self.panelUno.btn_resultados_campania.Enable(True)
			self.panelUno.btn_depositos.Enable(True)
			self.panelUno.btn_gastos.Enable(True)
			self.panelUno.btn_repartos.Enable(True)
		else:
			self.panelUno.tc_codigo.Clear()
			self.panelUno.tc_codigo.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
			self.panelUno.tc_codigo.Enable(False)
			self.panelUno.btn_crear_campania.Enable(True)
			self.panelUno.btn_crear_campania.SetFocus()
			self.panelUno.st_campania.SetLabel(u'No hay campañas abiertas')
			self.panelUno.btn_listados.Enable(False)
			self.panelUno.btn_modificar_campania.Enable(False)
			self.panelUno.btn_cerrar_campania.Enable(False)
			self.panelUno.btn_buscar.Enable(False)
			self.panelUno.btn_resultados_campania.Enable(False)
			self.panelUno.btn_depositos.Enable(False)
			self.panelUno.btn_gastos.Enable(False)
			self.panelUno.btn_repartos.Enable(False)

	
	"""Eventos de Panel Dos"""
	def Clientes(self, event):
		clientes = ControladorClientes(self.frame)
		clientes.run()

	def Campanias(self, event):
		campanias = ControladorCampanias(self.frame, self.usuario)
		campanias.run()

	def Usuarios(self, event):
		usuarios = ControladorUsuarios(self.frame)
		usuarios.run()

	def Historial(self, event):
		hist = ControladorHistorial(self.frame)
		hist.run()

	def Rutas(self, event):
		ruts = ControladorRutas(self.frame)
		ruts.run()

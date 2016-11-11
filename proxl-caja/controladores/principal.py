# -*- coding: utf-8 -*-
import wx
from vistas.frame_principal import FramePrincipal

from vistas.panel_uno import PanelUno
from vistas.panel_dos import PanelDos

from controladores.login import ControladorLogin
from controladores.iniciar import ControladorIniciarCaja
from controladores.clientes import ControladorClientes
from controladores.ingresos_varios import ControladorCajaIngresosVarios
from controladores.egresos_varios import ControladorCajaEgresosVarios
from controladores.cerrar import ControladorCerrarCaja
from controladores.modificarMovimiento import ControladorModificarMovimiento

from modelos.modelCajas import ModeloCajas
from modelos.modelMovimientos import ModeloMovimientos
from modelos.modelMovimientoClientes import ModeloMovimientoClientes
from modelos.modelCampanias import ModeloCampanias

class ControladorPrincipal:
	mdlCaj = ModeloCajas()
	mdlMov = ModeloMovimientos()
	mdlMovCli = ModeloMovimientoClientes()
	mdlCamp = ModeloCampanias()
	
	def __init__(self):
		self.parent = None
		self.selec = {}

	def run(self):
		self.frame = FramePrincipal(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		log = ControladorLogin(self.frame, False)
		self.usuario = log.run()
		if self.usuario != {}:
			self.panelUno = PanelUno(self.frame.notebook)
			self.panelDos = PanelDos(self.frame.notebook)

			self.frame.notebook.AddPage(self.panelUno, u"Clientes atendidos", False)
			self.frame.notebook.AddPage(self.panelDos, u"Ingresos/Egresos Varios", False)

			self.capturarEventos()
			self.cargarDatos()
			self.frame.Show()

	def capturarEventos(self):
		self.frame.btn_iniciar.Bind(wx.EVT_BUTTON, self.Iniciar)
		self.frame.btn_cerrar.Bind(wx.EVT_BUTTON, self.Cerrar)
		self.frame.btn_salir.Bind(wx.EVT_BUTTON, self.Salir)

		# Eventos panel uno
		self.panelUno.btn_clientes.Bind(wx.EVT_BUTTON, self.Clientes)
		self.panelUno.btn_modificar.Bind(wx.EVT_BUTTON, self.Modificar)
		self.panelUno.grilla_uno.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.f_seleccion_fila)

		# Eventos panel dos
		self.panelDos.btn_ingresos.Bind(wx.EVT_BUTTON, self.IngresosVarios)
		self.panelDos.btn_egresos.Bind(wx.EVT_BUTTON, self.EgresosVarios)

	def cargarDatos(self):
		self.datosCamp = self.mdlCamp.get_active_campaign()
		if self.datosCamp != {}:
			camp = str(self.datosCamp['numero']) + '-' + str(self.datosCamp['anio'])
			self.frame.st_campania.SetLabel(camp)
		self.datosCaja = self.mdlCaj.get_box_active()
	
		if self.datosCaja != {}:
			self.frame.btn_iniciar.Enable(False)
			camp = str(self.datosCaja['campNum']) + "-" + str(self.datosCaja['campAnio'])
			self.frame.st_campania.SetLabel(camp)
			self.frame.btn_cerrar.Enable(True)
			self.frame.tc_monto_inicial.SetValue(str(self.datosCaja['monto']))
			self.frame.tc_monto_inicial.Enable(True)

			self.mdlMovCli.mcam_anio = self.datosCaja['campAnio']
			self.mdlMovCli.mcam_num = self.datosCaja['campNum']
			self.mdlMovCli.mcaj_numero = self.datosCaja['numero']
			ListadoMovCli = self.mdlMovCli.read_all()
			self.cargar_grilla_uno(ListadoMovCli)

			self.mdlMov.mcam_anio = self.datosCaja['campAnio']
			self.mdlMov.mcam_num = self.datosCaja['campNum']
			self.mdlMov.mcaj_numero = self.datosCaja['numero']

			self.ListadoMov = self.mdlMov.read_all()
			self.cargar_grilla_dos(self.ListadoMov)

			self.panelUno.btn_clientes.Enable(True)
			self.panelDos.btn_ingresos.Enable(True)
			self.panelDos.btn_egresos.Enable(True)
			
			self.refrescar_resultados()

		else:
			self.frame.tc_monto_inicial.Clear()
			self.frame.btn_iniciar.Enable(True)
			self.frame.btn_cerrar.Enable(False)
			self.frame.tc_monto_inicial.Enable(False)
			self.panelUno.btn_clientes.Enable(False)
			self.panelDos.btn_ingresos.Enable(False)
			self.panelDos.btn_egresos.Enable(False)
			self.limpiar_grilla_uno()
			self.limpiar_grilla_dos()
			self.frame.tc_total_ing.Clear()
			self.frame.tc_total_egr.Clear()
			self.frame.tc_totales.Clear()
			
		self.panelUno.btn_modificar.Enable(False)
		


	def configurar_grilla_uno(self, tam):
		self.panelUno.grilla_uno.SetSelectionMode(wx.grid.Grid.SelectRows)
		self.panelUno.grilla_uno.AppendRows(tam)

	def cargar_grilla_uno(self, listado):
		self.configurar_grilla_uno(len(listado))
		for i in range(len(listado)):
			self.panelUno.grilla_uno.SetCellValue(i, 0, str(listado[i][0]))
			self.panelUno.grilla_uno.SetCellValue(i, 1, str(listado[i][1]))
			self.panelUno.grilla_uno.SetCellValue(i, 2, str(listado[i][2]))

			if listado[i][3] == 0:
				self.panelUno.grilla_uno.SetCellValue(i, 3, "No")
			elif listado[i][3] == 1:
				self.panelUno.grilla_uno.SetCellValue(i, 3, "Si")

			if listado[i][4] == 2:
				self.panelUno.grilla_uno.SetCellValue(i, 4, str(listado[i][5]))
			elif listado[i][4] == 3:
				self.panelUno.grilla_uno.SetCellValue(i, 5, str(listado[i][5]))

	def limpiar_grilla_uno(self):
		for i in range(self.panelUno.grilla_uno.GetNumberRows()):
			self.panelUno.grilla_uno.DeleteRows(0, 1)

	def refrescar_grilla_uno(self):
		self.limpiar_grilla_uno()
		self.ListadoMovCli = self.mdlMovCli.read_all()
		self.cargar_grilla_uno(self.ListadoMovCli)

	def configurar_grilla_dos(self, tam):
		self.panelDos.grilla_dos.SetSelectionMode(wx.grid.Grid.SelectRows)
		self.panelDos.grilla_dos.AppendRows(tam)
		presentador = wx.grid.GridCellAutoWrapStringRenderer
		for i in range(tam):
			self.panelDos.grilla_dos.SetRowSize(i, 25)
			self.panelDos.grilla_dos.SetCellRenderer(i, 2, presentador())

	def cargar_grilla_dos(self, listado):
		self.configurar_grilla_dos(len(listado))
		for i in range(len(listado)):
			self.panelDos.grilla_dos.SetCellValue(i, 0, listado[i]['tipo'])
			self.panelDos.grilla_dos.SetCellValue(i, 1, listado[i]['monto'])
			self.panelDos.grilla_dos.SetCellValue(i, 2, listado[i]['comentario'])

	def limpiar_grilla_dos(self):
		for i in range(self.panelDos.grilla_dos.GetNumberRows()):
			self.panelDos.grilla_dos.DeleteRows(0, 1)

	def refrescar_grilla_dos(self):
		self.limpiar_grilla_dos()
		self.cargar_grilla_dos(self.ListadoMov)

	def refrescar_resultados(self):
		ingr = self.mdlMov.totalIngresos() + self.mdlMovCli.totalIngresosClientes()
		egre = self.mdlMov.totalEgresos()
		ttal = ingr - egre
		self.frame.tc_total_ing.SetValue(str(ingr))
		self.frame.tc_total_egr.SetValue(str(egre))
		self.frame.tc_totales.SetValue(str(ttal))


	def Iniciar(self, event):
		if self.datosCamp != {}:
			iniCaja = ControladorIniciarCaja(self.frame, self.datosCamp)
			iniCaja.run()
			self.cargarDatos()
		else:
			wx.MessageBox(u"Para iniciar la caja primero debe existir una campaña activa.", u"No hay campaña activa!")


	def Cerrar(self, event):
		cerCaja = ControladorCerrarCaja(self.frame, self.datosCaja)
		cerCaja.run()
		self.cargarDatos()

	def Clientes(self, event):
		cli = ControladorClientes(self, self.datosCaja)
		cli.run()
		self.panelUno.btn_modificar.Enable(False)

	def Modificar(self, event):
		log = ControladorLogin(self.frame, True)
		usu = log.run()
		if usu != {}:
			modMov = ControladorModificarMovimiento(self.frame, self.selec)
			modMov.run()
			self.panelUno.btn_modificar.Enable(False)
			self.selec = {}
			self.refrescar_resultados()
			self.refrescar_grilla_uno()
			self.panelUno.btn_modificar.Enable(False)
		

	def f_seleccion_fila(self, event):
		fila = event.GetRow()
		try:
			self.selec['anio'] = self.datosCaja['campAnio']
			self.selec['num'] = self.datosCaja['campNum']
			self.selec['cnum'] = self.datosCaja['numero']
			self.selec['codigo'] = self.panelUno.grilla_uno.GetCellValue(fila, 0)
			self.panelUno.btn_modificar.Enable(True) 
		except:
			pass
		event.Skip()

	def IngresosVarios(self, event):
		ingVar = ControladorCajaIngresosVarios(self.frame, self.datosCaja)
		ingVar.run()
		self.ListadoMov = self.mdlMov.read_all()
		self.refrescar_grilla_dos()
		self.refrescar_resultados()

	def EgresosVarios(self, event):
		egrVar = ControladorCajaEgresosVarios(self.frame, self.datosCaja)
		egrVar.run()
		self.ListadoMov = self.mdlMov.read_all()
		self.refrescar_grilla_dos()
		self.refrescar_resultados()

	def Salir(self, event):
		self.frame.Destroy()



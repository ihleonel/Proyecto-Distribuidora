# -*- coding: utf-8 -*-
import time
import wx
from modelos.modelListados import ModeloListados
from modelos.modelXLCodigos import ModeloXLCodigos
from modelos.modelArticulos import ModeloArticulos
from modelos.modelClientes import ModeloClientes
from modelos.modelCampanias import ModeloCampanias
from vistas.frame_agregar_listado import FrameAgregarListado
from validadores.validarListado import ValidarList

class ControladorAgregarListado:
	mdlXLCod = ModeloXLCodigos()
	mdlList = ModeloListados()
	mdlArt = ModeloArticulos()
	mdlCli = ModeloClientes()
	mdlCam = ModeloCampanias()
	def __init__(self, parent, aCamp):
		self.parent = parent
		self.aCamp = aCamp

	def run(self):
		self.frame = FrameAgregarListado(self.parent)
		self.cargarDatos()
		self.capturarEventos()
		self.cargarValidadores()
		resp = self.frame.ShowModal()
		if resp == wx.ID_OK:
			self.Agregar()
			#wx.MessageBox("El listado a sido cargado con exito", "Enhorabuena")
		self.frame.Destroy()

	def capturarEventos(self):
		self.frame.btn_buscar.Bind(wx.EVT_BUTTON, self.Buscar)

	def cargarDatos(self):
		t = str(self.aCamp['anio'])+'-'+str(self.aCamp['numero'])
		self.frame.tc_campania.SetValue(t)
		self.frame.tc_fecha.SetValue(time.strftime("%d-%m-%Y"))
		self.mdlList.cam_anio = self.aCamp['anio']
		self.mdlList.cam_num = self.aCamp['numero']
		self.frame.tc_num_listado.SetValue(str(self.mdlList.count_list()+1))

	def cargarValidadores(self):
		self.frame.tc_archivo.SetValidator(ValidarList())

	def Buscar(self, event):
		wildcard = 	"Archivos de Excel (*.xls)|*.xls"
					
		dialog = wx.FileDialog(self.frame, "Elegir archivo", "C:\Users\leonel\desktop",
				"", wildcard, wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			self.mdlXLCod.dir = dialog.GetPath()
			self.frame.tc_archivo.SetValue(dialog.GetFilename())
		
			if self.mdlXLCod.traerLibro():
				self.listadoCodigos = self.mdlXLCod.obtenerCodigos()
				self.frame.tc_archivo.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
				self.frame.tc_archivo.Refresh()
			else:
				wx.MessageBox("Se produgo un error al intentar leer el archivo Excel!", "Ups!")
				self.frame.tc_archivo.SetBackgroundColour("pink")
				self.frame.tc_archivo.SetFocus()

	def Agregar(self):

		self.mdlList.fecha = time.strftime("%Y-%m-%d")
		self.mdlList.numero = self.frame.tc_num_listado.GetValue()
		self.mdlList.comentario = self.frame.tc_comentarios.GetValue()
		self.mdlList.create() # Agregar un nuevo listado.

		
		progresoMax = len(self.listadoCodigos)
		dialog = wx.ProgressDialog("Progreso de Carga", 
									"Cargando listado", progresoMax, 
									style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
		band = True
		cont = 0
		nuevosCodigos = 0
		self.mdlArt.cam_anio = self.aCamp['anio']
		self.mdlArt.cam_num = self.aCamp['numero']
		self.mdlArt.lis_numero = self.mdlList.numero

		for datos in self.listadoCodigos:
			self.mdlArt.cli_codigo = datos['codigo']
			if not self.mdlArt.exist(): # el codigo existe en la campania?
				self.mdlCli.codigo = datos['codigo']
				if not self.mdlCli.exist(): # el codigo de cliente existe?
					nuevosCodigos += 1
					self.mdlCli.create_short()
					
				# Actualizamos la localidad del cliente
				self.mdlCli.localidad = datos['localidad']
				self.mdlCli.new_update()

				self.mdlArt.cli_codigo = datos['codigo']
				self.mdlArt.deuda = float(datos['deuda'])
				self.mdlArt.camp = datos['campania']
				self.mdlArt.create() # agregamos un articulo nuevo
			if band and cont < progresoMax:
				cont += 1
				band = dialog.Update(cont)
		dialog.Destroy()


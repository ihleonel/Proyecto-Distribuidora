import wx
from vistas.frame_repartos import Frame
from modelos.modelReporte import ModeloReporteRepartos
from modelos.modelArticulos import ModeloArticulos
from modelos.modelRutas import ModeloRutas
from modelos.modelXLRutas import ModeloXLRutas
class ControladorRepartos:
	def __init__(self, parent, camp):
		self.parent = parent
		self.camp = camp

	def run(self):
		self.frame = Frame(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))

		self.capturarEventos()

		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.frame.Destroy()

	def capturarEventos(self):
		self.frame.btn_generar.Bind(wx.EVT_BUTTON, self.Generar)
		self.frame.btn_actualizar.Bind(wx.EVT_BUTTON, self.Actualizar)

	def Generar(self, event):
		mdlArt = ModeloArticulos()
		mdlArt.cam_anio = self.camp['anio']
		mdlArt.cam_num = self.camp['numero']

		mdlRut = ModeloRutas()
		mdlRut.rut_orden = self.frame.c_dias.GetSelection() + 1
		filas = mdlRut.customers_in_router(self.camp['anio'], self.camp['numero'])
		self.contenido = dict()
		for fila in filas:
			self.contenido[fila[-1]] = list()
		for fila in filas:
			self.contenido[fila[-1]].append(fila)

		nombreArchivo = "/%sREP_CAM_%s-%s.xls" % (mdlRut.rut_orden, mdlArt.cam_num, mdlArt.cam_anio)

		dialog = wx.DirDialog(self.frame, "SELECCIONAR CARPETA DE DESTINO:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
		rta = dialog.ShowModal()
		if rta == wx.ID_OK:
			dir = dialog.GetPath() + nombreArchivo

			mdlRepRep = ModeloReporteRepartos(mdlRut.rut_orden, self.camp, self.contenido ,dir)
			#try:
			mdlRepRep.generar_reporte()
			#except:
			#	wx.MessageBox("Ha ocurrido un error al generar reporte.", "Ups!")
			#else:
			#	wx.MessageBox("El reporte ha sido generado con exito.", "Enhorabuena!")

		dialog.Destroy()

	def Actualizar(self, event):
		mdlXLR = ModeloXLRutas()
		wildcard = 	"Archivos de Excel (*.xls)|*.xls"
		dialog = wx.FileDialog(self.frame, "Elegir archivo", "C:\Users\leonel\desktop",
				"", wildcard, wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			mdlXLR.abrir_archivo_xls( dialog.GetPath() )
			if mdlXLR.formato_es_valido():
				mdlXLR.migrar_a_base_de_datos()
			else:
				wx.MessageBox("El formato del archivo no es valido. Revisar!", "Ups!")

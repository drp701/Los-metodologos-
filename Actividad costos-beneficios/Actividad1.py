# Importamos la biblioteca wxPython para la interfaz gráfica y PuLP para la programación lineal
import wx
from pulp import *

# Creamos una clase para nuestra ventana, heredando de wx.Frame
class Mywin(wx.Frame):
    def __init__(self, parent, title):
        # Inicializamos la clase padre con el título y tamaño de la ventana
        super(Mywin, self).__init__(parent, title = title, size = (300,300))
        
        # Cargamos el ícono desde un archivo
        icon = wx.Icon('C:\\Users\\danie\\OneDrive\\Escritorio\\Actividad\\empresa.ico', wx.BITMAP_TYPE_ICO)
        
        # Establecemos el ícono para la ventana
        self.SetIcon(icon)

        # Creamos un panel en la ventana
        panel = wx.Panel(self)
        
        # Creamos un sizer vertical para organizar los elementos de la interfaz
        box = wx.BoxSizer(wx.VERTICAL)

        # Agregamos etiquetas para los campos de texto
        self.label1 = wx.StaticText(panel, label="Introduce los recursos (separados por espacios):")
        
        # Creamos el primer campo de texto para introducir los recursos
        self.text1 = wx.TextCtrl(panel, -1, style = wx.EXPAND|wx.TE_MULTILINE)
        
        self.label2 = wx.StaticText(panel, label="Introduce los beneficios (separados por espacios):")
        
        # Creamos el segundo campo de texto para introducir los beneficios
        self.text2 = wx.TextCtrl(panel, -1, style = wx.EXPAND|wx.TE_MULTILINE)
        
        # Creamos un botón para resolver el problema
        self.button = wx.Button(panel, -1, "Resolver")
        
        # Asociamos el evento de clic del botón a la función OnClick
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        # Añadimos las etiquetas y los campos de texto al sizer
        box.Add(self.label1, 0, flag = wx.LEFT | wx.TOP, border = 10)
        box.Add(self.text1, 1, flag = wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border = 10)
        box.Add(self.label2, 0, flag = wx.LEFT | wx.TOP, border = 10)
        box.Add(self.text2, 1, flag = wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border = 10)
        
        # Añadimos el botón al sizer
        box.Add(self.button, 0, flag = wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border = 10)

        # Asignamos el sizer al panel y ajustamos su tamaño
        panel.SetSizer(box)
        panel.Fit()
        
        # Centramos la ventana y la mostramos
        self.Centre()
        self.Show(True)

    # Esta función se ejecuta cuando se hace clic en el botón
    def OnClick(self,event):
        
        # Obtenemos los recursos y beneficios de los campos de texto
        recursos = [int(x) for x in self.text1.GetValue().split()]
        beneficios = [int(x) for x in self.text2.GetValue().split()]
        
        # Creamos el problema de programación lineal
        prob = LpProblem("Asignación de recursos", LpMaximize)
        
        # Creamos las variables de decisión
        proyectos = ['Proyecto_{}'.format(i+1) for i in range(len(recursos))]
        
        vars = LpVariable.dicts("Proyectos", proyectos, 0)
        
        # Añadimos la función objetivo al problema
        prob += lpSum([beneficios[i]*vars[proyectos[i]] for i in range(len(proyectos))])
        
        # Añadimos las restricciones al problema
        prob += lpSum([recursos[i]*vars[proyectos[i]] for i in range(len(proyectos))]) <= 50
        
        # Resolvemos el problema
        prob.solve()

         # Creamos una cadena con los resultados
        result = "Estado: {}\n".format(LpStatus[prob.status])
         
        for v in prob.variables():
             result += "{} = {}\n".format(v.name, v.varValue)
             
        result += "Beneficio total obtenido: {}".format(value(prob.objective))

         # Mostramos los resultados en un cuadro de diálogo
        dlg = wx.MessageDialog(self, result, "Resultados", wx.OK)
         
        dlg.ShowModal()
         
        dlg.Destroy()

# Creamos una aplicación wxPython y mostramos nuestra ventana
app = wx.App()
Mywin(None,"Programacion lineal")
app.MainLoop()


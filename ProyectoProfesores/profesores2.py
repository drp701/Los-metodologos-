import wx
import pulp

class AsignacionProfesoresApp(wx.App):
    def OnInit(self):
        self.frame = AsignacionProfesoresFrame(None, title="Asignación de Profesores a Cursos")  # Modifica el tamaño aquí

        self.frame.Show()
        return True

class AsignacionProfesoresFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(AsignacionProfesoresFrame, self).__init__(*args, **kw, size=(1500, 800))


        # Datos del problema
        self.profesores = ['A', 'B', 'C', 'D', 'E']
        self.cursos = ['C1', 'C2', 'C3', 'C4', 'C5']

        # Cuadro de texto para mostrar el enunciado y para ingresar preferencias
        self.enunciado_text = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        self.preferencias_text = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.HSCROLL)

        # Botón para resolver el problema
        self.solve_button = wx.Button(self, label="Resolver")
        self.solve_button.Bind(wx.EVT_BUTTON, self.resolver_problema)

        # Cuadro de texto para mostrar los resultados
        self.result_text = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)

        # Crear un sizer para organizar los elementos
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(self, label="Enunciado del problema:"), 0, wx.LEFT | wx.TOP, 10)
        sizer.Add(self.enunciado_text, 2, wx.EXPAND | wx.ALL, 10)
        sizer.Add(wx.StaticText(self, label="Ingrese preferencias (números separados por espacios):"), 0, wx.LEFT | wx.TOP, 10)
        sizer.Add(self.preferencias_text, 1, wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.solve_button, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(wx.StaticText(self, label="Resultados:"), 0, wx.LEFT | wx.TOP, 10)
        sizer.Add(self.result_text, 1, wx.EXPAND | wx.ALL, 10)

        self.SetSizerAndFit(sizer)
        self.Centre()

    def resolver_problema(self, event):
        # Leer preferencias ingresadas por el usuario
        preferencias_entrada = self.preferencias_text.GetValue().split('\n')
        preferencias_usuario = {}
        for i, linea in enumerate(preferencias_entrada):
            if linea:
                preferencias = linea.strip().split()  # Eliminar espacios en blanco y dividir en partes
                if len(preferencias) == len(self.cursos):
                    profesor = self.profesores[i]
                    preferencias_usuario[profesor] = {curso: int(pref) for curso, pref in zip(self.cursos, preferencias)}

        # Crear un problema de asignación lineal
        problema = pulp.LpProblem("AsignacionDeProfesores", pulp.LpMaximize)

        # Crear variables binarias para la asignación de profesores a cursos
        asignacion = pulp.LpVariable.dicts("Asignacion", [(profesor, curso) for profesor in self.profesores for curso in self.cursos], cat='Binary')

        # Función objetivo: maximizar la suma de las preferencias
        problema += pulp.lpSum(preferencias_usuario[profesor][curso] * asignacion[(profesor, curso)] for profesor in self.profesores for curso in self.cursos)

        # Restricciones: cada profesor dicta un solo curso y cada curso tiene un profesor
        for profesor in self.profesores:
            problema += pulp.lpSum(asignacion[(profesor, curso)] for curso in self.cursos) == 1

        for curso in self.cursos:
            problema += pulp.lpSum(asignacion[(profesor, curso)] for profesor in self.profesores) == 1

        # Resolver el problema
        problema.solve()

        # Mostrar resultados en el cuadro de texto
        self.result_text.SetValue("Resultados:\n")
        self.result_text.AppendText(f"Estado de la solución: {pulp.LpStatus[problema.status]}\n")
        for profesor in self.profesores:
            for curso in self.cursos:
                if pulp.value(asignacion[(profesor, curso)]) == 1:
                    self.result_text.AppendText(f"Profesor {profesor} asignado a curso {curso} con preferencia {preferencias_usuario[profesor][curso]}\n")
        self.result_text.AppendText(f"Valor de la función objetivo (suma de preferencias): {pulp.value(problema.objective)}")

        # Actualizar el enunciado con las preferencias ingresadas por el usuario
        enunciado = "Enunciado del problema: \n\n"
        for profesor in preferencias_usuario:
            enunciado += f"{profesor}: {preferencias_usuario[profesor]}\n"
        self.enunciado_text.SetValue(enunciado)

if __name__ == '__main__':
    app = AsignacionProfesoresApp(False)
    app.MainLoop()

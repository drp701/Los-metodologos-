# Importamos las librerias pertinentes
import tkinter as tk                    ### Interfaz grafica
from random import randint, uniform     ### Radianes de la interfaz ynumeros random
from math import cos, sin               ### Operaciones de los radianes

# Funcion para cambiar el icono
def change_icon(window, icon_path):
  
    window.iconbitmap(icon_path)
    
# Constructor de la clase DartGame
class DartGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego de dardos")
        change_icon(self.master, 'C:\\Users\\danie\\Downloads\\r_WxE_icon.ico')
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.player1_score = 0
        self.player2_score = 0
        self.turn = 1
        self.score_label = tk.Label(self.master, text="Jugador 1:0 | Jugador 2: 0")
        self.score_label.pack()
        self.turn_label = tk.Label(self.master, text="Turno del Jugador 1")
        self.turn_label.pack()
        self.throw_button = tk.Button(self.master, text="Lanzar dardo", command=self.throw_dart)
        self.throw_button.pack()
        self.reset_button = tk.Button(self.master, text="Volver a jugar", command=self.reset_game)
        self.reset_button.pack()
        self.darts = []

        # Funcion para lanzar el dardo y calcular puntaje 
    def throw_dart(self):
        r = randint(0, 200)
        theta = uniform(0, 2 * 3.14159)
        x, y = int(r * cos(theta) + 200), int(r * sin(theta) + 200)
        
        while (x,y) in self.darts:
            r = randint(0, 200)
            theta = uniform(0, 2 * 3.14159)
            x, y = int(r * cos(theta) + 200), int(r * sin(theta) + 200)
            
            ### Puntaje de los radianes
        if r <= 25:
            score = 50
        elif r <= 50:
            score = 50
        elif r <= 100:
            score = 20
        elif r <= 150:
            score = 20
        elif r <= 200:
            score = 5
        else:
            score = 0
            
        if self.turn == 1:
            self.player1_score += score
            if self.player1_score >= 250:
                self.end_game(1)
            else:
                self.turn = 2
                self.turn_label.config(text="Turno del Jugador 2")
                
        else:
            self.player2_score += score
            if self.player2_score >= 250:
                self.end_game(2)
            else:
                self.turn = 1
                self.turn_label.config(text="Turno del Jugador 1")
                
        self.score_label.config(text=f"Jugador 1: {self.player1_score} | Jugador 2: {self.player2_score}")
        
        if r <=200:
            color = "#00FF00"
            if (x-200)**2 + (y-200)**2 <= (25)**2:
                color = "#FFFFFF"
            elif (x-200)**2 + (y-200)**2 <= (50)**2:
                color = "#FFFFFF"
            elif (x-200)**2 + (y-200)**2 <= (100)**2:
                color = "#FF0000"
            elif (x-200)**2 + (y-200)**2 <= (150)**2:
                color = "#87CEEB"
            elif (x-200)**2 + (y-200)**2 <= (200)**2:
                color = "#000000"
                
            dart_id=self.canvas.create_oval(x -5 , y -5 , x +5 , y +5 , fill="yellow", outline="")            
            
            self.darts.append((dart_id))
            
    def reset_game(self):
        
    # Función para reiniciar el juego
        
        for dart in self.darts:
            
            dart_id=dart
            
            self.canvas.delete(dart_id)
            
        self.darts=[]
        
        self.player1_score=0
        
        self.player2_score=0
        
        self.turn=1
        
    def end_game(self,winner):
        
    # Función para terminar el juego y mostrar al ganador
        
        win_window=tk.Toplevel(self.master)
        
        win_window.title("Fin del Juego!")
        
        win_label=tk.Label(win_window,text=f"¡Jugador {winner} ha ganado!")
        
        win_label.pack()
        
    def draw_board(self):
        
    # Función para dibujar el tablero de dardos
        
        colors=["#000000","#FF0000","#87CEEB","#FFFFFF","#FFFFFF"]
        
    # Dibuja los radianes del tablero de dardos
        
        for i in range(5):
            
            if i==4:
                
                i=3
                
                j=4
                
                k=25
                
                l=25
                
                m=375
                
                n=375
                
                self.canvas.create_oval(k+i*50,l+i*50,m-i*50,n-i*50,fill=colors[j],outline="")
                
                break
                
            self.canvas.create_oval(50+i*50,50+i*50,350-i*50,350-i*50,fill=colors[i],outline="")
            
root=tk.Tk()

game=DartGame(root)

game.draw_board()

root.mainloop()

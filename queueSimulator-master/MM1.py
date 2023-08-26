#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PYTHON 2.7
#TEORÍA DE COLAS M/M/1 por Simón Salvo Pino

from math import exp

#Utilización Promedio p
def P(tasaLlegada,tasaServicio):
	return (float(tasaLlegada/tasaServicio)*100)
#Factor o porcentaje ocioso del sistema
def POcio(tasaLlegada,tasaServicio):
	return (100-P(tasaLlegada,tasaServicio))

#Numero esperado de clientes en la cola (Lq)
def Lq(tasaLlegada,tasaServicio):
	return (float((tasaLlegada*tasaLlegada)/(tasaServicio*(tasaServicio-tasaLlegada))))

#Numero esperado de clientes recibiendo el servicio (Ls)
def Ls(tasaLlegada,tasaServicio):
	return tasaLlegada/tasaServicio

#Numero esperado de clientes en el sistema de colas (Lw)
def Lw(tasaLlegada,tasaServicio):
	return tasaLlegada/(tasaServicio-tasaLlegada)

#Valor esperado de tiempo que emplea un cliente en la cola (Wq)
def Wq(tasaLlegada,tasaServicio):
	return tasaLlegada/(tasaServicio*(tasaServicio-tasaLlegada))

#Valor esperado del tiempo que emplea un cliente en el servicio (Ws)
def Ws(tasaLlegada,tasaServicio):
	return 1/tasaServicio

#Valor esperado del tiempo que emplea un cliente en recorrer el sistema (Ww)
def Ww(tasaLlegada,tasaServicio):
	return 1/(tasaServicio-tasaLlegada)

#Probabilidad de que existan n clientes en la cola
def ProbPn(tasaLlegada,tasaServicio,n):
	return ((1-(tasaLlegada/tasaServicio))*(tasaLlegada/tasaServicio)**n)*100

#Probabilidad de que el número de clientes en el sistema (Lw) sea mayor a n
def ProbLw(tasaLlegada,tasaServicio,n):
	return (tasaLlegada/tasaServicio)**(n+1)*100

#Probabilidad de que el tiempo empleado por un cliente en la cola (Wq) sea mayor a t unidades de tiempo
def ProbWq(tasaLlegada,tasaServicio,t):
	return (tasaLlegada/tasaServicio)*exp(-tasaServicio*(1-(tasaLlegada/tasaServicio))*t)*100

#Probabilidad de que el tiempo empleado por un cliente en recorrer el sistema (Ww) sea mayor a t unidades de tiempo
def ProbWw(tasaLlegada,tasaServicio,t):
	return exp(-tasaServicio*(1-(tasaLlegada/tasaServicio))*t)*100
 
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce tu opción: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
	print('\nBienvenido, ingrese los datos manteniendo cuidado con las unidades de cada uno (horas, minutos, días)')
	print("1. Obtener datos generales")
	print("2. Obtener probabilidades")
	print("3. Salir")
     
	print ("Elige una opcion")
 
	opcion = pedirNumeroEntero()
 
	if opcion == 1:
		tasaLlegada = float(input("Ingrese el valor de la tasa de llegada (lambda): "))
		tasaServicio = float(input("Ingrese el valor de la tasa de servicio (u): "))
		print ('Tasa de uso del sistema: ' , P(tasaLlegada,tasaServicio),'%')
		print ('Tasa de ocio del sistema: ' , POcio(tasaLlegada,tasaServicio),'%')
		print ('Numero esperado de clientes recibiendo servicio (Ls): ', Ls(tasaLlegada,tasaServicio))
		print ('Numero esperado de clientes en el sistema de colas (Lw): ', Lw(tasaLlegada,tasaServicio))
		print ('Numero esperado de clientes en la cola (Lq): ', Lq(tasaLlegada,tasaServicio))
		print ('Valor esperado del tiempo que emplea un cliente en la cola (Wq): ', Wq(tasaLlegada,tasaServicio))
		print ('Valor esperado del tiempo que emplea un cliente en el servicio (Ws): ', Ws(tasaLlegada,tasaServicio))
		print ('Valor esperado del tiempo que emplea un cliente en recorrer el sistema (Ww): ', Ww(tasaLlegada,tasaServicio))
	elif opcion == 2:
		tasaLlegada = float(input("Ingrese el valor de la tasa de llegada : "))
		tasaServicio = float(input("Ingrese el valor de la tasa de servicio : "))
		t = float(input("Ingrese el valor de t (tiempo): "))
		n = float(input("Ingrese el valor de n: "))
		print ('Probabilidad de que hayan ', n , 'clientes en la cola es: ',ProbPn(tasaLlegada,tasaServicio,n),'%')
		print ('Probabilidad de que el numero de clientes en el sistema (Lw) sea mayor a ',n, ' es: ',ProbLw(tasaLlegada,tasaServicio,n),'%')
		print ('Probabilidad de que el tiempo empleado por un cliente en la cola (Wq) sea mayor a ', t,' es: ',ProbWq(tasaLlegada,tasaServicio,t),'%')
		print ('Probabilidad de que el tiempo empleado por un cliente en recorrer el sistema (Ww) sea mayor a ', t,' es: ',ProbWw(tasaLlegada,tasaServicio,t),'%')

	elif opcion == 3:
		salir = True
	else:
		print ("Introduce un numero entre 1 y 3")

print ("Fin")
    
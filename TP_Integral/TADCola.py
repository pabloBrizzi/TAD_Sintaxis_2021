#!/usr/bin/python
# -*- coding: latin-1 -*-

'''
Tad_cola= {
    vehic: TADVehiculo,
    }
'''

#Operaciones Admitidas

'''
crearCola()
#Crea una Cola vacía

esVacia(cola)
#Chequea que la cola sea vacia - Devuelve true si es vacía

encolar(cola, auto)
#Agrega un elemento al final de la cola

desencolar(cola)
#Retorna y elimina el primer elemento de la cola

tamanio(cola)
#Retorna la cantidad de elementos de la cola

copiarCola(cola1, cola2)
#Retorna en cola2 una copia de cola1
'''

from TADAuto import *
from collections import deque

def crearCola():
	#Crea una cola vacía
	cola = deque() #cola = []
	return cola

def esVacia(cola):
	#Retorna verdadero si la cola no tiene elementos
	return len(cola)==0

def encolar(cola, auto):
	#Agrega un elemento al final de la cola
	cola.append(auto)

def desencolar(cola):
	#Retorna y elimina el primer elemento de la cola
    return cola.popleft()  # auto = cola.pop(0)


def tamanio(cola):
	#Retorna la cantidad de elementos de la cola
	return len(cola)

def copiarCola(cola1, cola2):
	#Retorna en cola2 una copia de cola1
	aux = deque()
	while not esVacia(cola1):
		elem = desencolar(cola1)
		encolar(aux,elem)
	while not esVacia(aux):
		elem = desencolar(aux)
		encolar(cola1,elem)
		encolar(cola2,elem)

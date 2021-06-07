''' FORMA GENERICA DE LOS TAD COMPUESTOS'''

from TADAuto import *

''' ESPECIFICACION '''

#def crearEstacionamiento():
#Crea un Estacionamiento del tipo Lista para agregar todos los autos que se desee
#
#def agregarAuto(e, auto):
#Agrega un auto al Estacionamiento
#
#def eliminarAuto(e, auto):
#Elimina un auto del Estacionamiento
#
#def recuperarAuto(e, i):
#Retorna el auto de la posicion i-esima
#
#def cantidadAutos(e):
#Retorna la cantidad de autos que hay en el Estacionamiento
#
#def existeAuto(e, auto):
#Retorna True para saber si el auto se encuentra en el estacionamiento
#
#   ### otras funciones ###
#def es Vacio(c):-->es otra forma de ver si hay elementos en el TAD Compuesto o la lista
#   return len(c) == 0 #esto devuelve True si esta vacio, sino False
#

''' IMPLEMENTACION '''

def crearEstacionamiento():
    #Crea un Estacionamiento
    e = []
    return e

def agregarAuto(e, auto):
    #Agrega un auto pasado por parametro al Estacionamiento
    e.append(auto)

def eliminarAuto(e, auto):
    #Elimina un auto pasado por parametro del Estacionamiento
    e.remove(auto)

def recuperarAuto(e, posicion):
    #Retorna el auto de la posicion indicada por parametro
    return e[posicion]

def cantidadAutos(e):
    #Retorna la cantidad de autos que hay en el Estacionamiento
    return len(e)

def existeAuto(e, auto):
    #Retorna True para saber si el auto se encuentra en el Estacionamiento
    return auto in e
    '''esto funciona como un condicional'''

def esVacia(e):
    #Retorna True si el Estacionamiento no tiene autos cargados
    return len(e) == 0

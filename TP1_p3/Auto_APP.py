from TP1_p3.TAD_auto import *

'''
TAD_Auto = {
    km: float,
    marca: string,
    mod: string,
    prec: float,
}
'''

#Operaciones Admitidas

'''
crearAuto() 
#Crea un auto vacío

cargarAuto(auto, km, marca, mod, prec)
#Agrega un Auto nuevo

verKm(auto)
#Retorna los Kms del Auto

verMarca(auto)
#Retorna la Marca del auto

verModelo(auto)
#Retorna el modelo del Auto

verPrecio(auto)
#Retorna el Precio del Auto

modKm(auto, otroKm)
#Modifica el Km del Auto

modMarca(auto, otraMarca)
#Modifica la Marca del Auto

modModelo(auto, otroMod)
#Modifica el modelo del Auto

modPrecio(auto, otroPrec)
#Modifica el precio del Auto
'''

'''b)Realizar una aplicación que permita crear dos autos 
e imprimir los datos del auto con menor kilometraje.'''

#Creo el primer auto y agrego sus datos
auto1 = crearAuto()
print("____"*3, "\n\r")
print("Datos Auto 1\n\r")

km1 = float(input("Ingrese los km: \n\r"))
marc1 = input("Ingrese la marca: \n\r")
mod1 = input("Ingrese el modelo: \n\r")
prec1 = float(input("Ingrese el precio: \n\r"))

cargarAuto(auto1, km1, marc1, mod1, prec1)

print(verKm(auto1), " | ", verMarca(auto1), " | ", verModelo(auto1), " | ", verPrecio(auto1), "\n\r")

#Creo el segundo auto y agrego sus datos
auto2 = crearAuto()

print("____"*3, "\n\r")
print("Datos Auto 2\n\r")

km2 = float(input("Ingrese los km: \n\r"))
marc2 = input("Ingrese la marca: \n\r")
mod2 = input("Ingrese el modelo: \n\r")
prec2 = float(input("Ingrese el precio: \n\r"))

cargarAuto(auto2, km2, marc2, mod2, prec2)

#Comparo cuál es el de menor precio e imprimo sus datos
if(verPrecio(auto1)<verPrecio(auto2)):
    print(verKm(auto1), " | ", verMarca(auto1), " | ", verModelo(auto1), " | ", verPrecio(auto1))
else:
    print(verKm(auto2), " | ", verMarca(auto2), " | ", verModelo(auto2), " | ", verPrecio(auto2))

from TAD_libro import *

'''
TAD_Libro = {
    cod: int,
    nomb: string,
    autor: string,
    gen: string,
    edit: string,
    prec: float,
}
'''

#Operaciones Admitidas

'''
crearLibro() 
#Crea un Libro vacío

cargarLibro(libro, cod, nomb, autor, gen, edit, prec)
#Agrega un Libro nuevo

verCod(libro)
#Retorna el Código del Libro

verNomb(libro)
#Retorna el Nombre del Libro

verAutor(libro)
#Retorna el Autor del Libro

verGen(libro)
#Retorna el Género del Libro

verEdit(libro)
#Retorna la Editorial del Libro

verPrec(libro)
#Retorna el Precio del Libro

modCod(libro, otroCod)
#Modifica el Código del Libro

modNomb(libro, otraNomb)
#Modifica el Nombre del Libro

modAutor(libro, otroAut)
#Modifica el Autor del Libro

modGenero(libro, otroGen)
#Modifica el Género del Libro

modEdit(libro, otraEdit)
#Modifica la Editorial del Libro

modPrecio(libro, otroPrec)
#Modifica el precio del Libro

'''

#Creo el primer libro y agrego sus datos
libro1 = crearLibro()
print("____"*3, "\n\r")
print("Datos Libro 1: \n\r")

cod1 = input("Ingrese el Código: \n\r")
nomb1 = input("Ingrese el Nombre: \n\r")
autor1 = input("Ingrese el Autor: \n\r")
gen1 = input("Ingrese el Género: \n\r")
edit1 = input("Ingrese la Editorial: \n\r")
prec1 = input("Ingrese el precio: \n\r")

cargarLibro(libro1, cod1, nomb1, autor1, gen1, edit1, prec1)

#Creo el segundo Libro y agrego sus datos
libro2 = crearLibro()
print("____"*3, "\n\r")
print("Datos Libro 2: \n\r")

cod2 = input("Ingrese el Código: \n\r")
nomb2 = input("Ingrese el Nombre: \n\r")
autor2 = input("Ingrese el Autor: \n\r")
gen2 = input("Ingrese el Género: \n\r")
edit2 = input("Ingrese la Editorial: \n\r")
prec2 = input("Ingrese el precio: \n\r")

cargarLibro(libro2, cod2, nomb2, autor2, gen2, edit2, prec2)

listaLibros=[libro1, libro2]

'''b - Realizar una aplicación que permita cargar dos libros, y luego incrementar el precio en un
8% a los libros de la editorial “Santillana”.'''

#Incremento del 8% del Precio de libros de Edit. Santillana

for i in range(len(listaLibros)):
    if(verEdit(listaLibros[i])=="Santillana"):
        modPrecio(listaLibros[i], (verPrec(listaLibros[i]) * 1.08))
    else:
        continue

for i in range(len(listaLibros)):
    print("Libro ", (i+1), " Precio: ", verPrec(listaLibros[i]))


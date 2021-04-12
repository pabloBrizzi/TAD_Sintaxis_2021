from TAD_med import *

'''
TAD_Med{

    nomg: string;
    nomcom: string;
    lab: string;
    prec: float;
}
'''

#crearMed()
#retorna un remedio sin datos

#cargarMed(r,nomg,nomcom,lab,prec)
#asigna nombre genérico, nombre comercial, laboratorio y precio al remedio r

#verNomGen(r)
#retorna el nombre genérico del remedio r

#verNomCom(r)
#retorna el nombre comercial de r

#verLab(r)
#retorna el laboratorio de r

#verPrecio(r)
#retorna el precio de r

#modNomGen(r, otroNG)
#modifica el nombre genérico de r

#modNomCom(r, otroNC)
#modifica el nombre comercial de r

#modLab(r, otroL)
#modifica el laboratorio de r

#modPrecio(r,otroP)
#modifica el precio de r

#copiar(r1,r2)
#copia todos los datos del remedio r2 en r1

med1 = crearMed()
nomg1 = input("Ingrese el Nombre del Medicamento: \r\n")
nomcom1 = input("Ingrese el Nombre Comercial del Medicamento: \r\n")
lab1 = input("Ingrese el Nombre del Laboratorio: \r\n")
prec1 = input("Ingrese el Precio: \r\n")
prec1 = int(prec1)

cargarMed(med1, nomg1, nomcom1, lab1, prec1)

med2 = crearMed()
nomg2 = input("Ingrese el Nombre del Medicamento: \r\n")
nomcom2 = input("Ingrese el Nombre Comercial del Medicamento: \r\n")
lab2 = input("Ingrese el Nombre del Laboratorio: \r\n")
prec2 = input("Ingrese el Precio: \r\n")
prec2 = int(prec2)

cargarMed(med2, nomg2, nomcom2, lab2, prec2)

if(verPrecio(med1) > verPrecio(med2)):
    verNomCom(med1)
else:
    verNomCom(med2)


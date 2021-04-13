import os
from TAD_Tramite import *

'''
TAD_Tramite{

    tipo: string; (reclamo de reparación, alta de servicio, baja de servicio, cambio de titular del
servicio)

    nroC: int;
    dniC: int;
    dia: int;
    mes: int;
}
'''

def borrarPantalla():
    if (os.name == "nt" or os.name == "dos" or os.name == "ce"):
        os.system("cls")
    else:   
        os.system("clear")
#crearTram()
#retorna un trámite nuevo sin datos

#cargarTram(t,tipo,nroC,dniC,dia,mes)
#asigna los datos al trámite t

#verTipo(t)
#retorna el tipo del trámite t-

#verNroC(t)
#retorna nro de cliente del trámite t

#verDniC(t)
#retorna el dni del cliente que hizo el trámite t

#verDia(t)
#retorna el día que se ingresó el trámite t

#verMes(t)
#retorna el mes en el cual se ingresó el trámite t

#modTipo(t, otroT)
#modifica el tipo del trámite t

#modDni(r,otroDni)
#modifica el dni del cliente que inició el trámite t

#modNroC(r, otroNro)
#modifica el nro de cliente del trámite t

#modDia(t,otroD)
#modifica el día del trámite t

#modMes(t,otroM)
#modifica el mes en el cual se ingresó el trámite t

#copiar(t1,t2)
#copia todos los datos del trámite t2 en t1

'''
Hacer un programa de aplicación que simule la recepción de varios trámites (usar un while) y
los cargue en una lista. 
Luego imprima la cantidad de solicitudes de cambio de titularidad recibidas
y un listado con el tipo de trámite y el nro de cliente de todos aquellos trámites que fueron
realizados entre el 10 y el 25 de marzo. 
Utilizar para manipular las variables de tipo TAD solamente
las operaciones especificadas. 
Aclaración: la lista no es otro TAD

'''

#Estructura auxiliar para incluir en un diccionario los tipos de trámites

dict_TipoTram = {
    1: "Reclamo de Reparación",
    2: "Alta de Servicio",
    3: "Baja de Servicio",
    4: "Cambio del Titular del Servicio",
}

sigue = 1

lista_Tram = []


while(sigue == 1):  #bucle que se utiliza para cargar Varios trámites, solicitando los datos de cada uno de ellos

    t = crearTram()
    
    print("Seleccione el Tipo de Tramite: \n\r")
    
    for i,j in dict_TipoTram.items():
        print(i,"-",j)

    tipo=int(input())
    tipo=dict_TipoTram[tipo]

    nroC = int(input("Ingrese el Num. de Cliente: \n\r"))
    dniC = int(input("Ingrese el Dni: \n\r"))
    dia = int(input("Ingrese el día: \n\r"))
    mes = int(input("Ingrese el mes: \n\r"))

    cargarTram(t,tipo,nroC,dniC,dia,mes)

    lista_Tram.append(t)

    print("¿Desea continuar agragando trámites?: \n\r")
    print("1-SI \n\r")
    print("2-NO \n\r")
    sigue = int(input())

borrarPantalla()

cont = 0

for i in lista_Tram:
    if (verTipo(lista_Tram(i))=="Cambio del Titular del Servicio"):
        cont+=1
    else:
        continue
    
print("La cantidad de Trámites de tipo Cambio de Titularidad son: ", cont, "\n\r")

print("____*3")

for i in lista_Tram:
    if(verMes(lista_Tram(i))==3 and verDia(lista_Tram(i))>=10 and verDia(lista_Tram(i))<=25):
        print(verTipo(lista_Tram(i)), " - ", verNroC(lista_Tram(i)))
    else:
        continue

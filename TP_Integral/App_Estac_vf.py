import datetime
from TADAuto import *
from TADCola import *
from TADEstacionamiento import *
import os


#Procedimientos y Funciones utilizadas.
def pausa():
    if (os.name == "nt" or os.name == "dos" or os.name == "ce"):
        os.system('pause')
    else:
        input("Enter para continuar")

def borrarPantalla():
    if (os.name == "nt" or os.name == "dos" or os.name == "ce"):
        os.system("cls")
    else:
        os.system("clear")



'''###   PUNTO 1 INGRESAR VEHICULO'''
#Procedimiento Ingreso Vehículo y agrego en lista
def ingresarVehiculo(estacN):
    print("\t\t:: INGRESO DE VEHICULO ::")
    autoN = crearAuto()
    pat = input("\n- Ingrese la Patente: ").upper()
    torre = int(input("- Ingrese la Torre: "))
    horaIngreso = datetime.datetime.now()
    horaFormateada = horaIngreso.time().strftime("%H:%M:%S")
    # --> Almacenar en una variable la hora formateada solamente sirve para el momento de imprimir. Deja de entender los metodos de la clase datetime.
    print(f"- Hora de Ingreso: {horaFormateada} ")

    cargarAuto(autoN, pat, horaIngreso,torre,'', 0.0)
    agregarAuto(estacN, autoN)

    return print("\nVehiculo agregado correctamente!!\n")



'''### PUNTO 2 - MODIFICAR VEHICULO'''
#Procedimiento ingreso el vehiculo a modificar y cargo nuevos datos.
def controlFormatHora(horaIngNueva):
    while("0"<horaIngNueva.split(sep=':')[0]>"23" or "0"<horaIngNueva.split(sep=':')[1]>"59"):
        print("Formato Hora equivocada")
        print("Hora no puede ser menor a 00:00 ni mayor a 23:59")
        horaIngNueva=input("Ingrese nueva hora: formato hs:mm -> ")
    return horaIngNueva

def formatDateNuevaHora(horaIngNueva):
    fechaHoy = str(datetime.date.today())
    newFechaHora = fechaHoy + " " + horaIngNueva + ":00"
    horaIngNuevaTDate=datetime.datetime.strptime(newFechaHora, "%Y-%m-%d %X")
    return horaIngNuevaTDate

def modificarVehiculo(estacN):
    print("\t\t:: MODIFICACION DE VEHICULO ::")
    patente = input("\nBuscar patente: ").upper()
    existe = False

    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)

        if verPatente(autoXPos) == patente:
            patNueva = input("\n- Ingrese la nueva Patente: ").upper()
            modificarPatente(autoXPos, patNueva)
            torreNueva = int(input("- Ingrese la nueva Torre: "))
            modificarTorre(autoXPos, torreNueva)

            resp = (input("\n-> Desea modificar hora de Ingreso o Egreso? (s/n) ")).lower()
            if resp == "s":
                print("¿Que desea modificar?: ")
                print("1- Hora de Ingreso")
                print("2- Hora de Egreso")
                print("0- Continuar sin modificar hs")
                respSubMenu = int(input())
                while(respSubMenu!=0):
                    if(respSubMenu==1):
                        horaIngNueva = formatDateNuevaHora(controlFormatHora(input("- Ingrese la nueva hs de Ingreso (hh:mm): ")))
                        if(verHoraEgreso(autoXPos) != ''):
                            while(horaIngNueva > verHoraEgreso(autoXPos)):
                                print("La hora de Ingreso no puede ser superior a la hora de Egreso")
                                print(f"Hora de Igreso cargada: {verHoraIngreso(autoXPos).hour}:{verHoraIngreso(autoXPos).minute}:{verHoraIngreso(autoXPos).second}")
                                print(f"Hora de Egreso cargada: {verHoraEgreso(autoXPos).hour}:{verHoraEgreso(autoXPos).minute}:{verHoraEgreso(autoXPos).second}")
                                horaIngNueva = formatDateNuevaHora(controlFormatHora(input("- Ingrese la nueva hs de Ingreso (hh:mm:ss): ")))
                            modificarHoraIngreso(autoXPos, horaIngNueva)
                            horas=(hsEstadia(verHoraIngreso(autoXPos), verHoraEgreso(autoXPos)))
                            monto=tarifaTotal(precioHora, horas, verTorre(autoXPos))
                            modificarMonto(autoXPos, monto)
                            resp2 = (input("\n-> Desea modificar hora de Egreso? (s/n) ")).lower()
                            if resp2 == "s":
                                respSubMenu=2
                            else:
                                respSubMenu=0
                        else:
                            modificarHoraIngreso(autoXPos, horaIngNueva)
                            respSubMenu=0
                    elif(respSubMenu==2):
                        horaEgrNueva = formatDateNuevaHora(controlFormatHora(input("- Ingrese la nueva hs de Egreso (hh:mm:ss): ")))
                        while(horaEgrNueva < verHoraIngreso(autoXPos)):
                            print("La hora de Egreso no puede ser anterior a la hora de Ingreso")
                            print(f"Hora de Igreso cargada: {verHoraIngreso(autoXPos).hour}:{verHoraIngreso(autoXPos).minute}:{verHoraIngreso(autoXPos).second}")
                            print(f"Hora de Egreso cargada: {verHoraEgreso(autoXPos).hour}:{verHoraEgreso(autoXPos).minute}:{verHoraEgreso(autoXPos).second}")
                            horaEgrNueva = formatDateNuevaHora(controlFormatHora(input("- Ingrese la nueva hs de Egreso (hh:mm:ss): ")))
                        modificarHoraEgreso(autoXPos, horaEgrNueva)
                        horas=(hsEstadia(verHoraIngreso(autoXPos), verHoraEgreso(autoXPos)))
                        monto=tarifaTotal(precioHora, horas, verTorre(autoXPos))
                        modificarMonto(autoXPos, monto)
                        respSubMenu=0
                    else:
                        respSubMenu=0
            else:
                continue
        existe = True
    if existe is True:
        print("\n-> Vehiculo modificado exitosamente!!\n")
    else:
        print("\n-> Patente inexistente!!\n")



'''### PUNTO 3 - REGISTRAR SALIDA DE VEHÍCULO'''
#Procedimiento de registro de salida de vehiculos del estacionamiento
def hsEstadia(hsIngreso, hsEgreso):
    #VER SI COBRAMOS POR MINUTO O POR REDONDEO DE HORAS.
    totalHoras = ((hsEgreso - hsIngreso).total_seconds())/(datetime.timedelta(hours=1).total_seconds())
    if (round(totalHoras)-totalHoras)>0:
        totalHoras=round(totalHoras)
    elif (round(totalHoras)-totalHoras)<0:
        totalHoras=round(totalHoras) + 1
    else:
        totalHoras=totalHoras
    return totalHoras

def tarifaTotal(precio, hsEstadia, torre):
    if (torre != 3):
        montoTotal = precio * hsEstadia
        return montoTotal
    else:
        montoTotal = (precio*(1-0.15)) * hsEstadia
        return montoTotal

def registrarSalidaVehiculo(estacN, precioHora):
    print("\t\t:: REGISTRAR SALIDA DE VEHICULO ::")
    patente = input("\n- Ingrese la patente: ").upper()
    borrarPantalla()
    existe = False

    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)

        if verPatente(autoXPos) == patente:
            horaEgreso = datetime.datetime.now()
            modificarHoraEgreso(autoXPos, horaEgreso)

            horas=(hsEstadia(verHoraIngreso(autoXPos), verHoraEgreso(autoXPos)))

            monto=tarifaTotal(precioHora, horas, verTorre(autoXPos))

            modificarMonto(autoXPos, monto)

            print("\t\t:: RECIBO ::\n")
            print(f"- Patente: {verPatente(autoXPos)}")
            print(f"- Torre: {verTorre(autoXPos)}")
            print(f"- Hora Ingreso: {verHoraIngreso(autoXPos).hour}:{verHoraIngreso(autoXPos).minute}:{verHoraIngreso(autoXPos).second}")
            print(f"- Hora Egreso: {verHoraEgreso(autoXPos).hour}:{verHoraEgreso(autoXPos).minute}:{verHoraEgreso(autoXPos).second}")
            print(f"- Importe: ${verMonto(autoXPos)}\n\r")
            existe = True

    if existe is True:
        print("-> Registro de Egreso exitoso!!\n")
    else:
        print("\n-> Patente inexistente!!\n")



'''### PUNTO 4 - LISTADO DE Vehículos'''
#Procedimientos Listado de Vehículos
def listarVehiculosActivos(estacN):
    print("\t\t:: LISTADO DE VEHICULOS ACTIVOS ::\n")
    cantVehActivos=0
    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        if verHoraEgreso(autoXPos) == '':
            cantVehActivos+=1
            print(f"{cantVehActivos}- Patente: {verPatente(autoXPos)}   | Torre: {verTorre(autoXPos)}   | Hora de Ingreso: {verHoraIngreso(autoXPos).hour}:{verHoraIngreso(autoXPos).minute}:{verHoraIngreso(autoXPos).second}")

    print(f"\n-> Cantidad de Vehículos Activos: {cantVehActivos}")


def listarVehiculosInactivos(estacN):
    print("\t\t:: LISTADO DE VEHICULOS INACTIVOS ::\n")
    cantVehInac=0
    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        if verHoraEgreso(autoXPos) != '':
            cantVehInac+=1
            print(f"{cantVehInac}-Patente: {verPatente(autoXPos)}   | Torre: {verTorre(autoXPos)}   | Hora de Ingreso: {verHoraIngreso(autoXPos).hour}:{verHoraIngreso(autoXPos).minute}:{verHoraIngreso(autoXPos).second}  | Hora de Egreso: {verHoraEgreso(autoXPos).hour}:{verHoraEgreso(autoXPos).minute}:{verHoraEgreso(autoXPos).second}")
    print(f"\n-> Cantidad de Vehículos Inactivos: {cantVehInac}")


def listarTotalVehiculos(estacN):
    print("\t\t:: LISTADO DE VEHICULOS TOTALES ::\n")
    cantVehTotal=0
    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        cantVehTotal+=1
        if verHoraEgreso(autoXPos) == '':
            print(f"{cantVehTotal}-Patente: {verPatente(autoXPos)}  | Torre: {verTorre(autoXPos)}   | ACTIVO")
        else:
            print(f"{cantVehTotal}-Patente: {verPatente(autoXPos)}  | Torre: {verTorre(autoXPos)}   | INACTIVO")
    print(f"\n-> Cantidad de Vehículos Totales: {cantVehTotal}")



'''### PUNTO 5 - INFORME RECAUDACIÓN POR TORRE'''
#Procedimiento que calcula el monto total recaudado por torre.
def informeRecxTorre(estacN):
    print("\t\t:: INFORME RECUDACIÓN TOTAL - TORRES ::\n")
    torresAutos=[]
    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        torresAutos.append(verTorre(autoXPos))
    torresUnicas=sorted(list(set(torresAutos)))
    del torresAutos
    for t in torresUnicas:
        totRec=0
        for i in range(cantidadAutos(estacN)):
            autoXPos = recuperarAuto(estacN, i)
            if verTorre(autoXPos)==t:
                totRec+=verMonto(autoXPos)
        print(f"TORRE {t} | RECAUDACIÓN: ${totRec}")
    print('')
    del torresUnicas


'''### PUNTO 6 - HORARIOS PICOS'''
#Prodecimiento de Cantidad de vehículos ingresados en las horas pico (7hs hasta las 10hs/17hs hasta las 20hs)
def cantVehIngreso(estacN):
    print("\t\t:: CANTIDAD INGRESO DE VEHICULOS EN HORARIOS PICOS (7-10hs y 17-20hs) ::")
    contar = 0

    horapico1 = datetime.time(7,0,0)
    horapico2 = datetime.time(10,0,0)
    horapico3 = datetime.time(17,0,0)
    horapico4 = datetime.time(20,0,0)

    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        #hsRef=(verHoraIngreso(autoXPos)).time()
        if (horapico1 < ((verHoraIngreso(autoXPos)).time()) <horapico2) or (horapico3 < ((verHoraIngreso(autoXPos)).time()) < horapico4):
            contar += 1

    print("\n-> Cantidad de vehiculos ingresados en horarios pico:", contar, "\n")



'''### PUNTO 7 - ELIMINAR VEHICULOS DSPS DE LAS 18HS'''
#Prodecimiento de eliminacion de vehiculos que Ingresaron despues de las 18hs pero de una Torre determina
def eliminarVehiTorre(estacN):
    print("\t\t:: ELIMINACION DE VEHICULOS de las 18hs y TORRE DETERMINADA ::\n")
    torre = int(input("-> Indique la Torre: "))
    dieciocho = datetime.time(18, 0, 0)
    bandera = True
    '''i=0
    while i != (cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        if verTorre(autoXPos) == torre:
            if ((verHoraIngreso(autoXPos)).time()) > dieciocho:
                eliminarAuto(estacN, autoXPos)
                i=0
                bandera = False
        else:
            i += 1
    '''
    torresAutos=[]
    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        torresAutos.append(verTorre(autoXPos))
    torresUnicas=sorted(list(set(torresAutos)))
    del torresAutos
    for t in torresUnicas:
        for i in range(cantidadAutos(estacN)):
            autoXPos = recuperarAuto(estacN, i)
            if ((verTorre(autoXPos)==t) and ((verHoraIngreso(autoXPos)).time()) > dieciocho):
                eliminarAuto(estacN, autoXPos)
                bandera = False
    print('')
    del torresUnicas

    if bandera == True:
        print("\n-> No ingresaron vehiculos despues de las 18hs a la Torre [", torre, "].\n")
    else:
        print("\n-> Vehiculos ingresados despues de las 18hs a la Torre [", torre, "] eliminados exitosamente!!\n")
    del torre


"""### PUNTO 8 - GENERAR COLA DE UNA TORRE """
# Procedimiento de generar cola de una torre determinada
def generarColaxtorre(estacN):
    print("\t\t:: COLA DE VEHICULOS de una TORRE DETERMINADA ::\n")
    cola=crearCola()
    torre=int(input("-Ingrese la Torre que desea generar la cola: "))
    cantidad= cantidadAutos(estacN)

    for posicion in range (cantidad):
        a=recuperarAuto(estacN, posicion)

        if(verTorre(a)==torre):
            encolar(cola, a)

    respuesta = (input("\n-> Desea imprimir los datos a la cola? (s/n) ")).lower()
    if respuesta == "s":
        print('')
        while (esVacia(cola) != True):
            auto = desencolar(cola)
            print("- Patente: " , verPatente(auto))
        print('')






''' ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::    '''
''' :::::::::::::::::::::    INICIO DEL PROGRAMA     :::::::::::::::::::::    '''

#Defino las estructuras que voy a utilizar
estacN=crearEstacionamiento()

#Defino las variables utilizadas en la app
finDia=True
diaFecha=datetime.date.today()

#Impresion del dia que se ejecuta en la App del estacionamiento
print(f"\n\t## INICIO DIA: {diaFecha.day}/{diaFecha.month}/{diaFecha.year} ##")

#Solicito el Precio de la Hora
precioHora = float(input("Ingrese el Precio de la Hora: $ "))

while (precioHora==0):
    print("Debe ingresar un precio mayor a 0 para continuar")
    precioHora = float(input("Ingrese el Precio de la Hora: $ "))

print("")
pausa()
borrarPantalla()


while (finDia):
    #MENU
    print(f"\t---{diaFecha.day}/{diaFecha.month}/{diaFecha.year}---")
    print("\t----- MENU ----")
    print("1- Ingresar vehículo")
    print("2- Modificar vehículo")
    print("3- Registrar salida de vehículo")
    print("4- Listado de vehículos")
    print("5- Generar informe indicando el monto recaudado por cada torre")
    print("6- Cantidad de vehiculos ingresados en las horas pico (7hs hasta las 10hs/17hs hasta las 20hs)")
    print("7- Eliminar los vehículos que ingresaron luego de las 18 hs a una torre determinada")
    print("8- Generar una cola con los vehículos de una torre determinada.")
    print("9- Finalizar el dia.")

    opcionMenu = int(input("\n\r-> Digite una opción: "))
    print("")
    #pausa()
    borrarPantalla()

    if(opcionMenu == 1):
        ingresarVehiculo(estacN)

    if(opcionMenu == 2):
        modificarVehiculo(estacN)

    if(opcionMenu == 3):
        registrarSalidaVehiculo(estacN, precioHora)

    if(opcionMenu == 4):

        print("\t----- OPCIONES DE LISTADO ----")
        print("1- Listado Vehículos Activos")
        print("2- Listado Vehículos Inactivos")
        print("3- Listado Total de Vehículos")
        print("4- Volver al Menu Principal")

        opcionSubMenu = int(input("\n->Digite una Opcion: "))

        if opcionSubMenu==1:
            borrarPantalla()
            listarVehiculosActivos(estacN)
            print('')
        elif opcionSubMenu==2:
            borrarPantalla()
            listarVehiculosInactivos(estacN)
            print('')
        elif opcionSubMenu==3:
            borrarPantalla()
            listarTotalVehiculos(estacN)
            print('')
        else:
            pass

    if(opcionMenu == 5):
        informeRecxTorre(estacN)

    if(opcionMenu == 6):
        cantVehIngreso(estacN)

    if(opcionMenu==7):
        eliminarVehiTorre(estacN)

    if(opcionMenu == 8):
        generarColaxtorre(estacN)

    if(opcionMenu == 9):
        borrarPantalla()
        print("\n   ** Fin del dia **\n")
        finDia=False

    pausa()
    borrarPantalla()

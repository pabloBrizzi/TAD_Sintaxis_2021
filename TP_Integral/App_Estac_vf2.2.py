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
#Procedimiento para controlar que las horas y minutos esten en los rangos correctos.
def controlHoraMinutos(hora_InEg, minu_InEg, bandera):
    if (0<=hora_InEg<24) and (0<=minu_InEg<=59):
        bandera = False
        return bandera
    else:
        print("  ** ERROR **")
        print("  Ingrese Horas y Minutos validos.\n")
        return bandera

#Procedimiento para corroborar que la hora ingresada no sea superior o inferior a las horas de Ingreso o Egreso
def controlNuevaHora(horaEgre, horaIngre, nueva_hora_InEg, bandera, autoXPos, resp2):
    if resp2 == 1:    #verifica q hora de Ingreso sea menor q la de ingreso
        if (horaEgre == "") or (horaEgre > nueva_hora_InEg):
            modificarHoraIngreso(autoXPos, nueva_hora_InEg)
            return bandera
        elif (horaEgre < nueva_hora_InEg):
            print("     ** ERROR **")
            print("     La Hora ingresada debe ser inferior al horario de Egreso.\n")
            bandera = True
            return bandera
    elif resp2 == 2:    #verifica q hora de Egreso sea mayor q la de ingreso
        if (horaIngre < nueva_hora_InEg):
            modificarHoraEgreso(autoXPos, nueva_hora_InEg)
            return bandera
        elif (horaEgre == "") or (horaIngre > nueva_hora_InEg):
            print("     ** ERROR **")
            print("     La Hora ingresada debe ser mayor al horario de Ingreso.\n")
            bandera = True
            return bandera

#Procedimiento ingreso el vehiculo a modificar y cargo nuevos datos.
def modificarVehiculo(estacN, precioHora):
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

            ### MODIFICAR horario de ingreso y egreso
            existe = True
            resp = input("\nModificar HORA INGRESO/EGRESO: → s/n: ").lower()
            while resp == 's':
                print("\n1- Hora INGRESO")
                print("2- Hora EGRESO")
                resp2 = input("Seleccione: ")
                print('')
                if resp2.isdigit(): #truquito con .ISDIGIT
                    resp2 = int(resp2)  #lo casteo a entero
                bandera = True

                while bandera:
                    if resp2 == 1:
                        print(" :: Hora INGRESO  ::")
                        hora_InEg = int(input("Hora: "))
                        minu_InEg = int(input("Minutos: "))
                        # ¡¡¡VER!!!
                        try:
                            bandera = controlHoraMinutos(hora_InEg, minu_InEg, bandera)

                        if bandera == False:
                            ##---- aca reutilizo los datos de fecha ya cargado (pq ya es tipo: Datetime), y solo modifico HORA y MINUTOS, los Seg por defecto son 00
                            nueva_hora_InEg = datetime.datetime(verHoraIngreso(autoXPos).year, verHoraIngreso(autoXPos).month, verHoraIngreso(autoXPos).day, hora_InEg, minu_InEg)
                            bandera = controlNuevaHora(verHoraEgreso(autoXPos), verHoraIngreso(autoXPos), nueva_hora_InEg, bandera, autoXPos, resp2)

                    elif resp2 == 2:
                        print(" :: Hora EGRESO  ::")
                        hora_InEg = int(input("Hora: "))
                        minu_InEg = int(input("Minutos: "))
                        # ¡¡¡VER!!!
                        bandera = controlHoraMinutos(hora_InEg, minu_InEg, bandera)

                        if bandera == False:
                            ##---- le copio los datos de FECHA ya ingresada xq si el EGRESO esta sin datos, no tengo una variable de donde extraerle la fecha
                            nueva_hora_InEg = datetime.datetime(verHoraIngreso(autoXPos).year, verHoraIngreso(autoXPos).month, verHoraIngreso(autoXPos).day, hora_InEg, minu_InEg)
                            bandera = controlNuevaHora(verHoraEgreso(autoXPos), verHoraIngreso(autoXPos), nueva_hora_InEg, bandera, autoXPos, resp2)

                            if bandera == False:
                                #saco todo practicamente de la parte del registro de hora de egreso, como para ver el nuevo recibo con el MONTO $$$
                                intervalo = (tiempoEstadia(verHoraIngreso(autoXPos), verHoraEgreso(autoXPos)))
                                monto=tarifaTotal(precioHora, intervalo, verTorre(autoXPos))
                                modificarMonto(autoXPos, monto)


                                print("\t\t:: RECIBO ::\n")
                                print(f"- Patente: {verPatente(autoXPos)}")
                                print(f"- Torre: {verTorre(autoXPos)}")
                                print(f"- Hora Ingreso: {verHoraIngreso(autoXPos).hour}:{verHoraIngreso(autoXPos).minute}:{verHoraIngreso(autoXPos).second}")
                                print(f"- Hora Egreso: {verHoraEgreso(autoXPos).hour}:{verHoraEgreso(autoXPos).minute}:{verHoraEgreso(autoXPos).second}")
                                print(f"- Importe: ${verMonto(autoXPos)}\n\r")

                    else:
                        print(" ** ERROR **")
                        print(" Ingrese una opcion valida.\n")
                        print("1- Hora INGRESO")
                        print("2- Hora EGRESO")
                        resp2 = input("Seleccione: ")
                        if resp2.isdigit():
                            resp2 = int(resp2)
                            print('')

                resp = input("\n- Continua modificando HORA INGRESO/EGRESO: → s/n: ").lower()

    if existe is True:
        print("\n-> Vehiculo modificado exitosamente!!\n")
    else:
        print("\n-> Patente inexistente!!\n")



'''### PUNTO 3 - REGISTRAR SALIDA DE VEHÍCULO'''
#Procedimiento de registro de salida de vehiculos del estacionamiento
def tiempoEstadia(hsIngreso, hsEgreso):
    #VER SI COBRAMOS POR MINUTO O POR REDONDEO DE HORAS.
    #Fraccionamos el tiempo de estadía en minutos y comparamos si es < de 60 cobramos hora completa
    #Si la fracción es mayor a 60 min cobramos por minuto extra
    totalTiempo = ((hsEgreso - hsIngreso).total_seconds())/(datetime.timedelta(minutes=1).total_seconds()) #Corte en 30 min, podemos hacerlo en 15 - 20 o el corte que elijamos

    #Condición de redondeo
    if (round(totalTiempo)-totalTiempo)>0:
        totalTiempo=round(totalTiempo)
    elif (round(totalTiempo)-totalTiempo)<0:
        totalTiempo=round(totalTiempo) + 1
    else:
        totalTiempo=totalTiempo

    #Condicion de minimo cobra 1 hora
    if totalTiempo<60:
        totalTiempo=60
    else:
        totalTiempo
    return totalTiempo

def tarifaTotal(precio, tiempoTotal, torre):
    precioxMin = precio/(datetime.timedelta(minutes=60).total_seconds())*(datetime.timedelta(minutes=1).total_seconds())
    if torre != 3:
        montoTotal = precioxMin * tiempoTotal
        return montoTotal
    else:
        montoTotal = (precioxMin*(1-0.15)) * tiempoTotal
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

            tiempoTotal=(tiempoEstadia(verHoraIngreso(autoXPos), verHoraEgreso(autoXPos)))

            monto=tarifaTotal(precioHora, tiempoTotal, verTorre(autoXPos))

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
            print(f"{cantVehActivos}- Patente: {verPatente(autoXPos)}       | Torre: {verTorre(autoXPos)}   | Hora de Ingreso: {verHoraIngreso(autoXPos).hour}:{verHoraIngreso(autoXPos).minute}:{verHoraIngreso(autoXPos).second}")

    print(f"\n-> Cantidad de Vehículos Activos: {cantVehActivos}")


def listarVehiculosInactivos(estacN):
    print("\t\t:: LISTADO DE VEHICULOS INACTIVOS ::\n")
    cantVehInac=0
    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        if verHoraEgreso(autoXPos) != '':
            cantVehInac+=1
            print(f"{cantVehInac}-Patente: {verPatente(autoXPos)}       | Torre: {verTorre(autoXPos)}   | Hora de Ingreso: {verHoraIngreso(autoXPos).hour}:{verHoraIngreso(autoXPos).minute}:{verHoraIngreso(autoXPos).second}  | Hora de Egreso: {verHoraEgreso(autoXPos).hour}:{verHoraEgreso(autoXPos).minute}:{verHoraEgreso(autoXPos).second}")
    print(f"\n-> Cantidad de Vehículos Inactivos: {cantVehInac}")


def listarTotalVehiculos(estacN):
    print("\t\t:: LISTADO DE VEHICULOS TOTALES ::\n")
    cantVehTotal=0
    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        cantVehTotal+=1
        if verHoraEgreso(autoXPos) == '':
            print(f"{cantVehTotal}-Patente: {verPatente(autoXPos)}      | Torre: {verTorre(autoXPos)}   | ACTIVO")
        else:
            print(f"{cantVehTotal}-Patente: {verPatente(autoXPos)}      | Torre: {verTorre(autoXPos)}   | INACTIVO")
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
    i=0
    while i != int((cantidadAutos(estacN))):
        autoXPos = recuperarAuto(estacN, i)
        if verTorre(autoXPos) == torre:
            if ((verHoraIngreso(autoXPos)).time()) > dieciocho:
                eliminarAuto(estacN, autoXPos)
                i=0
                bandera = False
            else:
                i+=1
        else:
            i+=1

    if bandera == True:
        print("\n-> No ingresaron vehiculos despues de las 18hs a la Torre", torre, ".\n")
    else:
        print("\n-> Vehiculos ingresados despues de las 18hs a la Torre", torre, "fueron eliminados exitosamente!!\n")



"""### PUNTO 8 - GENERAR COLA DE UNA TORRE """
# Procedimiento de generar cola de una torre determinada
def generarColaxtorre(estacN):
    print("\t\t:: COLA DE VEHICULOS de una TORRE DETERMINADA ::\n")
    cola=crearCola()
    torre=int(input("-Ingrese la Torre que desea generar la cola: "))
    cantidad= cantidadAutos(estacN)
    bandera = True

    for posicion in range (cantidad):
        a=recuperarAuto(estacN, posicion)

        if(verTorre(a)==torre):
            encolar(cola, a)
            bandera = False

    if bandera == True:
        print("\n-> No hay vehiculos en la torre", torre, ".\n")
    else:
        print("\n-> Cola de Vehiculos de la torre", torre, "fue generada exitosamente!!\n")

        respuesta = (input("-> Desea imprimir los datos a la cola? (s/n) ")).lower()
        if respuesta == "s":
            borrarPantalla()
            print("\t\t:: COLA DE VEHICULOS de una TORRE DETERMINADA ::\n")
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
        modificarVehiculo(estacN, precioHora)

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

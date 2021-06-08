import datetime
from TADAuto import *
from TADCola import *
from TADEstacionamiento import *

def pausa():
    if (os.name == "nt" or os.name == "dos" or os.name == "ce"):
        os.system('pause')
    else:
        os.sytem('sleep 2')

def borrarPantalla():
    if (os.name == "nt" or os.name == "dos" or os.name == "ce"):
        os.system("cls")
    else:
        os.system("clear")

def ingresarVehiculo():
    pat=input("\n\rIngrese la Patente: ")
    torre=int(input("\n\rIngrese la Torre: "))
    horaIngreso=datetime.datetime.now()
    horaEgreso=horaIngreso + datetime.timedelta(hours=1,minutes=30,seconds=50)
    autoN=crearAuto()
    monto=float(input("Monto Total: "))
    cargarAuto(autoN, pat, horaIngreso,torre,horaEgreso,monto)
    agregarAuto(estacN, autoN)
    return print("Auto Agregado Correctamente")
    pausa()

'''def listarVehiculosActivos(estacN):
    cantVehActivos=0
    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        if verHoraEgreso(autoXPos) == 0:
            cantVehActivos+=1
            print(f"{cantVehActivos}- Patente: {verPatente(autoXPos)} | Torre: {verTorre(autoXPos)} | Hora de Ingreso: {verHoraIngreso(autoXPos).hour}:{verHoraIngreso(autoXPos).minute}:{verHoraIngreso(autoXPos).second}")

    print(f"\n-> Cantidad de Vehículos Activos: {cantVehActivos}")
#    pausa()
#    borrarPantalla()

def listarVehiculosInactivos(estacN):
    cantVehInac=0
    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        if verHoraEgreso(autoXPos) != 0:
            cantVehInac+=1
            print(f"{cantVehInac}-Patente: {verPatente(autoXPos)} | Torre: {verTorre(autoXPos)} | Hora de Ingreso: {verHoraIngreso(autoXPos).hour}:{verHoraIngreso(autoXPos).minute}:{verHoraIngreso(autoXPos).second} | Hora de Egreso: {verHoraEgreso(autoXPos).hour}:{verHoraEngreso(autoXPos).minute}:{verHoraEngreso(autoXPos).second}")
    print(f"\n-> Cantidad de Vehículos Activos: {cantVehInac}")
#    pausa()
#    borrarPantalla()

def listarTotalVehiculos(estacN):
    cantVehTotal=0
    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        cantVehTotal+=1
        if verHoraEgreso(autoXPos) == 0:
            print(f"{cantVehTotal}-Patente: {verPatente(autoXPos)} | Torre: {verTorre(autoXPos)} | ACTIVO")
        else:
            print(f"{cantVehTotal}-Patente: {verPatente(autoXPos)} | Torre: {verTorre(autoXPos)} | INACTIVO")
    print(f"\n-> Cantidad de Vehículos Totales: {cantVehTotal}")
#    pausa()
#    borrarPantalla()
'''

def hsEstadia(hsIngreso,hsEgreso):
    totalHoras = ((hsEgreso - hsIngreso).total_seconds())/(datetime.timedelta(hours=1).total_seconds())
    if (round(totalHoras)-totalHoras)>0:
        totalHoras=round(totalHoras)
    elif (round(totalHoras)-totalHoras)<0:
        totalHoras=round(totalHoras) + 1
    else:
        totalHoras=totalHoras
    return totalHoras

def tarifaTotal(precio, hsEstadia, torre):
    if torre != 3:
        montoTotal = precio * hsEstadia
        return montoTotal
    else:
        montoTotal = (precio*(1-0.15)) * hsEstadia
        return montoTotal

'''def informeRecxTorre(estacN):
    torres=[]
    torresUnicas=[]
    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        torres.append(verTorre(autoXPos))
    for t in torres:
        if t not in torresUnicas:
            torresUnicas.append(t)
    return torresUnicas
'''

def informeRecxTorre(estacN):
    torresAutos=[]
    for i in range(cantidadAutos(estacN)):
        autoXPos = recuperarAuto(estacN, i)
        torresAutos.append(verTorre(autoXPos))
    torresUnicas=list(set(torresAutos))
    for t in torresUnicas:
        totRec=0
        for i in range(cantidadAutos(estacN)):
            autoXPos = recuperarAuto(estacN, i)
            if verTorre(autoXPos)==t:
                totRec+=verMonto(autoXPos)
        print(f"TORRE {t} | RECAUDACIÓN: ${totRec}")


estacN=crearEstacionamiento()
colaE=crearCola()

precio=10

#for i in range(5):
#    ingresarVehiculo()
for i in range(2):
    ingresarVehiculo()

print(cantidadAutos(estacN))

'''
for i in range(cantidadAutos(estacN)):
    autoXPos = recuperarAuto(estacN, i)
    hsAutoXPos = hsEstadia(verHoraIngreso(autoXPos), verHoraEgreso(autoXPos))
    print(hsEstadia(verHoraIngreso(autoXPos), verHoraEgreso(autoXPos)))
    print(tarifaTotal(precio,hsAutoXPos,verTorre(autoXPos)))
    #total_horas=(verHoraEgreso(autoXPos)-verHoraIngreso(autoXPos)).total_seconds()
    #print(total_horas)
'''
#listarVehiculosActivos(estacN)

#listarTotalVehiculos(estacN)

#informeRecxTorre(estacN)

hs1=datetime.datetime.now()
hs2=hs1+ datetime.timedelta(hours=1,minutes=30,seconds=50)
print(hs1.time())
print(hs2.time())
print(hsEstadia(hs1,hs2))

for i in range(cantidadAutos(estacN)):
    autoXPos=recuperarAuto(estacN, i)
    hsAutoXPos = (verHoraIngreso(autoXPos)).time()
    print(hsAutoXPos)

horapico1 = datetime.time(7,0,0)
print(horapico1)
'''
horaIngreso=datetime.datetime.now()
print(f"- Hora de Ingreso: {horaIngreso.hour}:{horaIngreso.minute}:{horaIngreso.second}")

horaFormateada = torresUnicas=list(set(torresAutos))horaIngreso.strftime("%H:%M:%S")   ##----------nuevo formato de hora SOLO de visualizacion, sin micosegundos
print(f"- Hora de Ingreso: {horaFormateada} ")
ej = datetime.time(20,00,00)
ej1 = datetime.datetime.now().time()
print(ej)
print(ej1)

if ej>ej1:
    print(f"Ej es mayor: {ej}")
if ej<ej1:
    print(f"Ej1 es mayor: {ej1}")
'''

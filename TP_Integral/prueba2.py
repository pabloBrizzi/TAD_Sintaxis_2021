import datetime
from TADAuto import *
from TADCola import *
from TADEstacionamiento import *

'''
def formatDateNuevaHora(horaIngNueva):
    if(horaIngNueva>"23:59:59" and horaIngNueva<"00:00:00"):
        return ("Ingreso inválido")
    else:
        fechaHoy = str(datetime.date.today())
        newFechaHora = fechaHoy + " " + horaIngNueva
        horaIngNuevaTDate=datetime.datetime.strptime(newFechaHora, "%Y-%m-%d %X")
        return horaIngNuevaTDate

def controlFormatHora(horaIngNueva):
    while(horaIngNueva>"23:59:59" or horaIngNueva < "00:00:00"):
        print("Formato Hora equivocada")
        print("Hora no puede ser menor a 00:00:00 ni mayor a 23:59:59")
        horaIngNueva=input("Ingrese nueva hora: formato hs:mm:ss -> ")
    return horaIngNueva

horapico1 = datetime.time(7,0,0)

print(horapico1)

horaActual = datetime.datetime.today()

print(horaActual)


hora1 = datetime.datetime.strptime("2021-05-31 22:00:00", "%Y-%m-%d %X")
print(hora1)

horaControl=formatDateNuevaHora(controlFormatHora(input("Ingrese nueva hora: formato hs:mm:ss -> ")))
#newHora=formatDateNuevaHora(horaControl)
#fechaHoy = str(datetime.date.today())
#newFechaHora = fechaHoy + " " + newHora

print(horaControl)
print(type(horaControl))

str1 = "00:00:00"
str2= "22:59:59"

if(str1>str2):
    print(f"Str1 {str1} es mayor")
else:
    print(f"Str2 {str2} es mayor")

if horaActual < horaControl:
    print("OK")
else:
    print("Error")


precioHora = int(input("Ingrese el precio de la hora: "))
precioxMin = precioHora/(datetime.timedelta(minutes=60).total_seconds())*(datetime.timedelta(minutes=1).total_seconds())
print(precioxMin)
'''
def ingreseHora(hs):
    while isinstance(hs, int)==False:
        try:
            hs=int(hs)
        except:
            print("Debe ingresar un formato de hora valido NumEntero")
            hs=input("Ingrese Hora: ")
    return hs

def ingreseMin(min):
    bandera=True
    while bandera:
        try:
            min=int(min)
            bandera=False
        except:
            print("Debe ingresar un formato de min válido - NumEntero")
            min=input("Ingrese Min: ")
    return min

def controlDatetime(hs,min):
        bandera=True
        while bandera:
            try:
                fecha=datetime.datetime(datetime.datetime.today().year,datetime.datetime.today().month,datetime.datetime.today().day,hs,min)
                bandera=False
            except:
                print("Debe ingresar un formato de hora | min valido")
                print(" 0 <= hs < 24")
                print(" 0 <= min < 60")
                hs=ingreseHora(input("Ingrese Hora: "))
                min=ingreseMin(input("Ingrese Min: "))
        return fecha


año_hoy=datetime.datetime.today().day
print(año_hoy)
print(type(año_hoy))
hs=ingreseHora(input("Ingrese Hora: "))
min=ingreseMin(input("Ingrese Min: "))

fecha=datetime.datetime(2012,3,1,22,50)

fecha1=controlDatetime(hs,min)
print(fecha)
print(fecha1)

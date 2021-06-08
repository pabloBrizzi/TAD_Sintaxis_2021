import datetime

'''x = [0,1,2,3]

def imprime(x, i):
    return x[i]

if(imprime(x,3) > imprime(x, 0)):
    print(imprime(x,3))
else:
    print(imprime(x,0))
'''



#Obtener el dia actual
'''today = date.today()
print(f"El dia de la fecha es {today}")'''

#Obtener hora
'''
hour = datetime.datetime.now()
print(f"Hora: {hour}")
hour2 = datetime.datetime.now()
print(f"Hora: {hour2}")
hour3 = hour2 - hour
total = hour3.total_seconds()
print(f"Segundos de diferencia: {hour3}")
'''

t1 = datetime.timedelta(hours=1,minutes=2,seconds=3).total_seconds()
t2 = datetime.timedelta(hours=2,minutes=3,seconds=4).total_seconds()
t3 = (t2 - t1)/(datetime.timedelta(hours=1).total_seconds())
print(f"Horas de diferencia: {t3}")


hora_ingreso = datetime.datetime.now()
print(f"Hora Ingreso: {hora_ingreso}")

hora_egreso = hora_ingreso + datetime.timedelta(hours=1,minutes=0,seconds=1)
print(f"Hora Egreso: {hora_egreso}")
diferencia = hora_egreso - hora_ingreso
print("Diferencia en segundos: ", diferencia.seconds)
total_horas = ((hora_egreso - hora_ingreso).total_seconds())/(datetime.timedelta(hours=1).total_seconds())

if (round(total_horas)-total_horas)>0:
    total_hs=round(total_horas)
elif (round(total_horas)-total_horas)<0:
    total_hs = round(total_horas) + 1
else:
    total_hs = total_horas

print(f"Horas Totales: {total_hs}")

precio = float(input("Ingrese Precio de hora: "))

total_monto = total_horas * precio
print(f"Monto total: {total_monto}")

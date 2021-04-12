import os
'''marcas = {
    1: "ford",
    2: "chevrolet",
    3: "fiat",
}

print("Seleccione la Marca: \n\r")
for i, j in marcas.items():
    print(i, "-", j)

t = int(input())
t=marcas[t]

print(t)

nroC = int(input("Ingrese el Num. de Cliente: \n\r"))
dniC = int(input("Ingrese el Dni: \n\r"))
dia = int(input("Ingrese el día: \n\r"))
mes = int(input("Ingrese el mes: \n\r"))

print(nroC, "-" ,dniC, "-" ,dia, "-" ,mes)'''

'''var = os.name
print(var)
cont=6

print("La cantidad de Trámites de tipo Cambio de Titularidad son: ", cont)'''

lista = [10,14,26,78,9]
cuenta = 0
for i in lista:
    if(i>=10 and i<= 20):
        cuenta += 1 
    else:
        continue
print(cuenta)


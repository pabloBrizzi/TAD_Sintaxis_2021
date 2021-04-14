#TAD_auto

def crearAuto():
    #Crea un auto vacío
    auto=["", 0, "", "", 0]
    return auto

def cargarAuto(auto, pat ,km, marca, mod, prec):
    #Agrega un Auto nuevo
    auto[0]=pat
    auto[1]=km
    auto[2]=marca
    auto[3]=mod
    auto[4]=prec

''' OTRA MANERA DE HACERLO   
    auto.append(pat)
    auto.append(km)
    auto.append(marca)
    auto.append(mod)
    auto.append(prec)'''

def verPat(auto):
    return auto[0]
    #Retorna los Kms del Auto


def verKm(auto):
    return auto[1]
    #Retorna los Kms del Auto

def verMarca(auto):
    return auto[2]
    #Retorna la Marca del auto

def verModelo(auto):
    return auto[3]
    #Retorna el modelo del Auto

def verPrecio(auto):
    return auto[4]
    #Retorna el Precio del Auto

def modKm(auto, otraPat):
    auto[0]=otraPat
    #Modifica el Km del Auto


def modKm(auto, otroKm):
    auto[1]=otroKm
    #Modifica el Km del Auto

def modMarca(auto, otraMarca):
    auto[2]=otraMarca
    #Modifica la Marca del Auto

def modModelo(auto, otroMod):
    auto[3]=otroMod
    #Modifica el modelo del Auto

def modPrecio(auto, otroPrec):
    auto[4]=otroPrec
    #Modifica el precio del Auto
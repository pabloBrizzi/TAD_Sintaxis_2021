#TAD_auto

def crearAuto():
    #Crea un auto vacío
    auto=[]
    return auto

def cargarAuto(auto, km, marca, mod, prec):
    #Agrega un Auto nuevo
    auto.append(km)
    auto.append(marca)
    auto.append(mod)
    auto.append(prec)


def verKm(auto):
    return auto[0]
    #Retorna los Kms del Auto

def verMarca(auto):
    return auto[1]
    #Retorna la Marca del auto

def verModelo(auto):
    return auto[2]
    #Retorna el modelo del Auto

def verPrecio(auto):
    return auto[3]
    #Retorna el Precio del Auto

def modKm(auto, otroKm):
    auto[0]=otroKm
    #Modifica el Km del Auto

def modMarca(auto, otraMarca):
    auto[1]=otraMarca
    #Modifica la Marca del Auto

def modModelo(auto, otroMod):
    auto[2]=otroMod
    #Modifica el modelo del Auto

def modPrecio(auto, otroPrec):
    auto[3]=otroPrec
    #Modifica el precio del Auto
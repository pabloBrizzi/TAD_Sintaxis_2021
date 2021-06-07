

'''
TADAuto = [
	Patente: string,
	HoraIngreso: datetime,
	Torre: int,
	HoraEgreso: datetime,
    Monto: float,
]


def crearAuto():
    #crea una instancia del vehiculo

def cargarAuto():
    #carga los datos correspondientes al auto

def verPatente(auto):
    #retorna la patente del auto

def verHoraIngreso (auto):
    #retorna la hora ingreso del auto

def verTorre(auto):
    #retorna la torre que se le asigno al auto

def verHoraEgreso(auto):
    #retirna la hora de egreso del auto

def moficarPatente(auto):
    #modifica la patente del auto

def modificarHoraIngreso(auto):
    #modifica la hora de ingreso del auto

def modificarTorre(auto):
    #modifica la torre que le fue asignada al auto

def modificarHoraEgreso(auto):
    #modifica la hora de egreso del auto

def mofidicarMonto(auto):
    #modifica el monto de la estadía

def copiarauto(auto):
    #copia los datos del auto 1 en el auto 2

'''

def crearAuto(): #crea auto vacio
	auto = ['','',0,'',0.0]
	return auto

def cargarAuto(auto,Patente,HoraIngreso,Torre,HoraEgreso,Monto): #carga el auto
	auto[0] = Patente
	auto[1] = HoraIngreso
	auto[2] = Torre
	auto[3] = HoraEgreso
	auto[4] = Monto

def verPatente(auto): #muestra patente auto
	return auto[0]

def verHoraIngreso(auto): #muestra la hora de ingreso del auto
	return auto[1]

def verTorre(auto): # muestra la torre que se le asigno al auto
	return auto[2]

def verHoraEgreso(auto):
    return auto[3]

def verMonto(auto):
    return auto[4]

def modificarPatente(auto,Patente): #modifica patente del auto
	auto[0] = Patente

def modificarHoraIngreso(auto,HoraIngreso): #modifica la hora de ingreso  del auto
	auto[1] = HoraIngreso

def modificarTorre(auto,Torre): #modifica  la torre que le fue asignada al auto
	auto[2] = Torre

def modificarHoraEgreso(auto,HoraEgreso): #modifica la hora de egreso del auto
    auto[3] = HoraEgreso

def modificarMonto(auto,NuevoMonto): #modifica el monto de la estadia del auto
    auto[4] = NuevoMonto

def copiarauto(auto1,auto2):
    auto2[0] = auto1[0]
    auto2[1] = auto1[1]
    auto2[2] = auto1[2]
    auto2[3] = auto1[3]
#	auto2[4] = auto1[4]

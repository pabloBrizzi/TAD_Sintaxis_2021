#TAD_libro

def crearLibro():
    #Crea un libro vacío
    libro=[]
    return libro

def cargarLibro(libro, cod, nomb, autor, gen, edit, prec):
    #Agrega un Libro nuevo
    libro.append(int(cod))
    libro.append(nomb)
    libro.append(autor)
    libro.append(gen)
    libro.append(edit)
    libro.append(float(prec))

def verCod(libro):
    return libro[0]
    #Retorna el Código del Libro

def verNomb(libro):
    return libro[1]
    #Retorna el Nombre del Libro

def verAutor(libro):
    return libro[2]
    #Retorna el Autor del Libro

def verGen(libro):
    return libro[3]
    #Retorna el Género del Libro

def verEdit(libro):
    return libro[4]
    #Retorna la Editorial del Libro

def verPrec(libro):
    return libro[5]
    #Retorna el Precio del Libro

def modCod(libro, otroCod):
    libro[0]=int(otroCod)
    #Modifica el Código del Libro

def modNomb(libro, otraNomb):
    libro[1]=otraNomb
    #Modifica el Nombre del Libro

def modAutor(libro, otroAut):
    libro[2]=otroAut
    #Modifica el Autor del Libro

def modGenero(libro, otroGen):
    libro[3]=otroGen
    #Modifica el Género del Libro

def modEdit(libro, otraEdit):
    libro[4]=otraEdit
    #Modifica la Editorial del Libro

def modPrecio(libro, otroPrec):
    libro[5]=float(otroPrec)
    #Modifica el precio del Libro
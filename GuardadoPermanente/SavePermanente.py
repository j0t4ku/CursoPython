

import pickle
from re import L

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de=> ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero, self.edad)


class ListaPersona:

    personas=[]

    def __init__(self):
        ficheroLista=open("FicheroExterno","ab+")
        ficheroLista.seek(0)
#Error si es la primera vez que se ejecute el programa  ya que esta vacio
        try:
            self.personas=pickle.load(ficheroLista)
            print("Se cargaron {} personas".format(len(self.personas)))
        except:
            print("El fichero esta vacio o no existe")
        finally:
            ficheroLista.close()
            del(ficheroLista)

        

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonas()


    def mostrarPersona(self):
        for p in self.personas:
            print(p)

    #Guarda las personas en el ficero externo
    def guardarPersonas(self):
        ficheroLista=open("FicheroExterno","wb")
        pickle.dump(self.personas, ficheroLista)
        ficheroLista.close()
        del(ficheroLista)

    def mostrarInfo(self):
        print("La informacion del fichero es la siguiente")
        for p in self.personas:
            print(p)


miListaPersona= ListaPersona()
#P= Persona("Jose","masculino",30)
#miListaPersona.agregarPersonas(P)
#P= Persona("Juan","masculino",25)
#miListaPersona.agregarPersonas(P)
#P= Persona("Ana","femenino",26)
#miListaPersona.agregarPersonas(P)

miListaPersona.mostrarInfo()



#Generador de Python regresa un objeto iterable
def generaPares(limite):
    num= 1
    while num<limite:
        yield num * 2
        num= num + 1

#objeto iterable
devulvePares=generaPares(10)
#llamada a un objeto iterable
#print(next(devulvePares))
#print(next(devulvePares))


####### Parte 2 ######


def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades= devuelveCiudades("Horqueta","Belen","Loreto","concepcion")
print(next(ciudades))
print(next(ciudades))
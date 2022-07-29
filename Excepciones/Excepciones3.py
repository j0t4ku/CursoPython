import math
#Lanzar una Excepcion propia 

#Primera Parte
def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("No se puede edades negativas")

    if edad < 20:
        return "Eres joven"
    elif edad < 40:
        return "Eres mayor"
    elif edad < 65:
        return "Eres anciano"
    elif edad < 100:
        return "Cuidate...."

#print(evaluaEdad(-15))


#Segunda Parte Crear y Capturando error
def raizCuadrada(num):
    if num < 0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num)

op1=(int(input("Introduce un numero: ")))

try:
    print(raizCuadrada(op1))
except ValueError as EX:
    print(EX)

print("Programa Finalizado")



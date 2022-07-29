

#### Excepciones parte 1 ######

# Error en tiempo de ejecucion. ocurren durante la ejecucion del programa

def suma(num1, num2):
    return num1+num2

def resta (num1, num2):
    return num1-num2

def multiplicar (num1, num2):
    return num1*num2

#Operacion erronea al dividir por CERO 
def dividir (num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("no se puede dividir entre zero")
        return "Operacion Erronea"
while True:
    #Excepcion de valor numerico y alfanumerico
    try:

        op1= (int(input("Intoduce el primer numero= ")))
        op2= (int(input("Intoduce el segundo numero= ")))
        break
    except ValueError:
        print("Valor ingresado no valido. Inetnta de nuevo")


operation= (str(input("Intoduce la operacion= ")))
if operation=="suma":
    print(suma(op1,op2))
elif operation=="resta":
    print(resta(op1,op2))
elif operation=="multiplica":
    print(multiplicar(op1,op2))
elif operation=="divide":
    print(dividir(op1,op2))
else:
    print("Ingreso una operacion no valida")

print("Operacion Terminada Finalmente")



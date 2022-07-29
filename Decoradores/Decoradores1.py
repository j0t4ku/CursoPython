# Funciones Decoradores
#Añaden funcionalidades a otras funcions
#Esta formado por 3 funciones 
#Devuelve una funcion
#

def func_decoradora(funcion):
    #*args recive un numero indeterminado de parametros
    def funcion_interior(*args, **kwargs): #argumentos con keywords
        #acciones adicionales que van a decorar la funcion que se quiera
        print("Se realizara un calculo")
        funcion(*args, **kwargs)
        #acciones adicionales 
        print("Se Termino el calculo")

    #retorna la funcion que va a decorar la funcion que se quiera
    return funcion_interior


@func_decoradora
def suma(num1,num2,num3):
    print(num1+num2+num3)

@func_decoradora
def resta(num1,num2):
    print(num1-num2)

@func_decoradora
def potencia(base, potencia):
    print(pow(base,potencia))

suma(5,5,2)

resta(5,5)

potencia(base=5,potencia=5)
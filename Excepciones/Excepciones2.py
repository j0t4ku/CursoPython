
#Capturando Excepcion

def divide():
    try:
        op1=(float(input("Introduce un numero")))
        op2=(float(input("Introduce un numero")))
        print( "La divicion es: "+ str(op1/op2))
    
    #Tambien se puede omitir la excepcion pero ejecuta el finally y muestra el error
    #except: para un mensaje de error general 
    except ValueError:
        print("El valor ingresado no valido")
    except ZeroDivisionError:
        print("No se puede dividir por zero")
    finally: #se ejecuta si o si
        print("Operacion finalizado")


divide()
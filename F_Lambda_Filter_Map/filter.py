#funcion filter
#fitra cosas
"""
def numero_par(num):
    if num % 2== 0:
        return True
"""

"""numeros=[15,2,16,15,19,99]

print(list(filter(lambda par:par%2==0,numeros)))
"""

class Empleado:
    def __init__(self, nombre, cargo, salario) -> None:
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self) -> str:
        return "{} que trabaja como {} con salario: {}".format(self.nombre,self.cargo,self.salario)



listaEmpleados=[
    Empleado("Juan","Director",5500000),
    Empleado("Ana","Presidente",10000000),
    Empleado("Jose","Asistente",3000000),
    Empleado("Maria","Gerente",4500000),
    Empleado("Fulanito","Administrador",2500000)
]


salariosAltos=filter(lambda empleado:empleado.salario>4000000,listaEmpleados)

for salario in salariosAltos:
    print(salario)
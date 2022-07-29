#Funcion Map


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



def calculoComision(empleado):
    if(empleado.salario <= 3000000):
        empleado.salario=empleado.salario*1.03
    return empleado

listaComision=map(calculoComision, listaEmpleados)

for comision in listaComision:
    print(comision)

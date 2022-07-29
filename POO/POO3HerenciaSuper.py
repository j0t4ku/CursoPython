#Principio de sustitucion
#Es siempre un/a
#


class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre=nombre
        self.edad= edad
        self.residencia= residencia


    def descripcion(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Residencia: ", self.residencia)


class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_e, edad_e, residencia_e):
        super().__init__(nombre_e,edad_e,residencia_e)
        self.salario= salario
        self.antiguedad= antiguedad

    def descripcion(self):
        super().descripcion()
        print("El salario es: ", self.salario)
        print("Su antiguedad es:",self.antiguedad)


jose= Empleado(100, 10, "jose", 25, "horqueta")
jose.descripcion()

print(isinstance(jose, Persona))
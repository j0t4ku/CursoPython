
#https://docs.python.org/es/3/library/stdtypes.html#text-sequence-type-str
# Metodods de Cadenas
# Uper() Lowe() Capitalize() Count() Find() Isdigit()
#Isalum() Isalpha() Split() Strip() Replace() rfind()


nombre=input("Introduce un nombre: ")
print("El nombre es: ", nombre.capitalize())

edad= input("Introduce una edad: ")
while(edad.isdigit() == False):
    print("introduce un numero")
    edad=input("Introduce la edad: ")

if(int(edad) < 18):
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

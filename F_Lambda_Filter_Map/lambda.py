#Funciones LAMBDA 

"""def areaTriangulo(b,a):
    return (b*a)/2

t1=areaTriangulo(1,2)
t2=areaTriangulo(2,3)
print(t1)
print(t1)
"""


#solo funciona con funciones simple, jamas con los que tienen bucles y o mas
areaTriangulo=lambda base,altura:(base*altura)/2
print(areaTriangulo(5,2))


al_cubo=lambda numero:numero**3 #pow(numero,3)
print(al_cubo(2))


destacar=lambda salario:"¡{}!$".format(salario)

print(destacar(50000))



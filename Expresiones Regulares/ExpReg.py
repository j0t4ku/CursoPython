# Expresiones regulares sintaxis y ejemplos sencillos
#Patron de busqueda 

import re

cadena="Vamos a aprender expresiones regulares en python con pildoras informaticas en su curso de python"

textoBuscar="python"

"""if(re.search(textoBuscar,cadena) is not None):
    print("Cadena Encontrada")
else:
    print("Cadena no encontrada")"""



textoEncontrado=re.search(textoBuscar,cadena)
#donde comienza la cadena
print(textoEncontrado.start())
#donde termina la cadena
print(textoEncontrado.end())
#ambos a la vez
print(textoEncontrado.span())

#encuentra ccuantos del texto buscado existe en la cadena donde se busca
#si le agregas len() a la funcion para saber cuantos hay
print(re.findall(textoBuscar,cadena))





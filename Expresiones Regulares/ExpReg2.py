#Meta Caracteres (caracteres comodin)

# simbolo '^Algo' (comienzo con)
#simbolo 'Algo$' (terminan con)
#simbolo [] '[sfg]' busca si existe alguno de los caracteres que hay entre corchetes en la cadena
# alg[oa] buscar algo o alga 


import re

listaNombre=["Ana gomez",
"Maria Martin",
"jose jose",
"juan mendoza",
"Maria fernandez"
]

buscar="jose"

for elemento in listaNombre:
    if(re.findall(buscar+"$", elemento)):
        print(elemento)




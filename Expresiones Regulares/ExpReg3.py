# Rangos 
#Rangos de caracter o numeros o ambos
# [a-z] o [A-Z] o [1-9]
# Negacion [^a-z] [^1-3]
# Union [0-3A-B] que son de dos rangos
# [.:] elementos que tengon o punto o 2puntos

import re

listaNombre=["Ma1",
"Ma2",
"Ma3",
"MaA",
"MaB",
"MaC",
"Ma.4"
]

for elemento in listaNombre:
    if re.findall('Ma[.:]', elemento):
        print(elemento)
#Match 
#Buscar Siempre al comienzo del string
# tercer parametro  re.IGNORECASE
#comodin . punto .ara busca lara y jara y zara 


#funcion search

import re


"""nombre1="Sandra Lopez"
nombre2="Jose Antonio"
nombre3="Maria Fernandez"

if re.match("Sandra", nombre1, re.IGNORECASE):
    print("Nombre Encontrado")"""

"""
cadena1="jose"
cadena2="4244242"
cadena3="a424"

if re.match("\d",cadena2):
    print("encontrado numero")"""


#Funcion sarch
nombre1="Sandra Lopez"
nombre2="Jose Antonio"
nombre3="Maria Fernandez"
if re.search("lopez",nombre1, re.IGNORECASE):
    print("Se encontro")



codigo1="fnkfnewoijwgjwoijgowejg71"
codigo2="71fasfasfsafasfsafasfasf"
codigo3="fkldsnfjofjerofjorejf"

if re.search("71",codigo3):
    print("Se encontro")
import pickle

lista=["Pedro","Ana","Maria","Juan"]


#Fichero en binario
fichero_b= open("ListaNombre","wb")

pickle.dump(lista,fichero_b)

fichero_b.close()
del(fichero_b)
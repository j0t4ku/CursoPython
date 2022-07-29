import pickle

fichero= open("ListaNombre", "rb")

lista= pickle.load(fichero)

print(lista)




#Manejo de Archivo  (Punteros)

from io import open

#r+ (lectura y escritura)
archivo= open("archivo.txt","r+")

#Primera Parte (Punteros)
#print(archivo.read()) #Se le puede indicar cuantos caracters leer 
#archivo.seek(0) #Desplaza el puntero del archivo al principio
#Si el archivo ya ha sido leido anterior a este comando
#El archivo.read() como ya esta ubicado al ultimo del archio
#devuelve 0 
#archivo.seek(len(archivo.readline()))
#print(archivo.read())
#archivo.close()


#Segunda Parte
#como lee desde el principio del archivo
#El puntero no se ha movido anteriormente
##archivo.write("Comienzo de archivo")


lineas= archivo.readlines()
lineas[1]="Esta es la linea 2 se ha modificado \n"
archivo.seek(0)
archivo.writelines(lineas)
archivo.close()

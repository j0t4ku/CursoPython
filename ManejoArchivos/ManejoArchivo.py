from io import open 

#Se puede abrir de forma de (lectura, escritura, append(añadir))
#w,r,a
archivo=open("archivo.txt","a")

#Primera Parte
#frase="Hola mundo. \n este es mi primer archivo"
#archivo.write(frase)
#archivo.close()


#Segunda Parte
#texto= archivo.read()
#archivo.close()
#print(texto)


#Tercera Parte
#Array de todas las lineas del archivo
#lineas= archivo.readlines()
#archivo.close()
#print(lineas)


#Cuarta Parte
archivo.write("\nHoy es un buen dia para programar")
archivo.close()


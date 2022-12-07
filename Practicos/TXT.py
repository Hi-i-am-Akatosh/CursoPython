from io import open

archivo_texto=open("prueba.txt", "r")
frase = archivo_texto.readlines()

archivo_texto.close()
print (frase[2])

#(w): Escribir dentro del .txt
#(a): Agregar sin sobreescribir.
#(r): Leer el contenido del txt.
#(archivo_texto.readlines()): Para leer lineas especificas.

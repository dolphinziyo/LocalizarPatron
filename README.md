Este programa buscará el patrón deseado en todos los ficheros (de texto plano) de una carpeta, mostrando por pantalla el fichero en el que está (si es que está en alguno), la línea, y la posición exacta. Está hecho para Python 2.7.
La búsqueda de ficheros se realiza de forma recursiva por lo que analizar carpetas que contienen muchos ficheros y subdirectorios puede requerir algo de tiempo.

Uso:
	localizarPatron patron [directorio] [extensión]
	
El primer parámetro que le hay que indicar es el patrón a buscar (PATRON) y es el único obligatorio, el segundo es el directorio en el que se realizará la búsqueda (DIRECTORIO) y el tercero es la extensión (sin el punto) de los archivos en los que se realizará la búsqueda (EXTENSION). Si no pasamos más parámetros que el obligatorio lo que hará será buscar el patrón en todos los archivos ubicados en el directorio actual. Si prescindimos de la extensión pero ponemos la carpeta, pues buscará en todos los ficheros de esa carpeta el patrón a buscar.
	
Por ejemplo: 

	·Para buscar "hola" en la carpeta actual en los ficheros con extensión ".txt":
		python2.7 localizarPatron.py hola . txt 

	·Buscar "hola" en la carpeta "/home/dolphin" en los ficheros con extensión ".php"
		python2.7 localizarPatron.py hola /home/dolphin php

	·Localizar la posición exacta, línea y fichero del patrón "hola" en todos los ubicados en el directorio actual:
		python2.7 localizarPatron.py hola
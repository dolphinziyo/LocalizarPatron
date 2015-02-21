Este programa buscar� el patr�n deseado en todos los ficheros (de texto plano) de una carpeta, mostrando por pantalla el fichero en el que est� (si es que est� en alguno), la l�nea, y la posici�n exacta. Est� hecho para Python 2.7.
La b�squeda de ficheros se realiza de forma recursiva por lo que analizar carpetas que contienen muchos ficheros y subdirectorios puede requerir algo de tiempo.

Uso:
	localizarPatron patron [directorio] [extensi�n]
	
El primer par�metro que le hay que indicar es el patr�n a buscar (PATRON) y es el �nico obligatorio, el segundo es el directorio en el que se realizar� la b�squeda (DIRECTORIO) y el tercero es la extensi�n (sin el punto) de los archivos en los que se realizar� la b�squeda (EXTENSION). Si no pasamos m�s par�metros que el obligatorio lo que har� ser� buscar el patr�n en todos los archivos ubicados en el directorio actual. Si prescindimos de la extensi�n pero ponemos la carpeta, pues buscar� en todos los ficheros de esa carpeta el patr�n a buscar.
	
Por ejemplo: 

	�Para buscar "hola" en la carpeta actual en los ficheros con extensi�n ".txt":
		python2.7 localizarPatron.py hola . txt 

	�Buscar "hola" en la carpeta "/home/dolphin" en los ficheros con extensi�n ".php"
		python2.7 localizarPatron.py hola /home/dolphin php

	�Localizar la posici�n exacta, l�nea y fichero del patr�n "hola" en todos los ubicados en el directorio actual:
		python2.7 localizarPatron.py hola
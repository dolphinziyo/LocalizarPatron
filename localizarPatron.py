# coding=ISO-8859-1
'''
Creado el 10/06/2011
@autor: dolphinziyo
    http://twitter.com/dolphinziyo
	Web: http://tecnogame.org
'''
# Este programa sirve para buscar ciertos patrones en archivos de texto plano,
# Su forma de uso es muy sencilla, requiere de la introducción del patrón a buscar,
# el directorio en el que se realizará la búsqueda y la extensión de los
# ficheros en los que se buscará. El directorio y la extensión son parámetros
# opcionales, si no se introducen se buscará en el directorio actual, en cual quiera 
# que sea la extensión de los ficheros, respectivamente. 
#
# encontrarPatron patron [directorio] [extensión]
#
# Se requiere Python 2.7

# Módulos
import string,os,sys
from subprocess import call
# Constantes

# Clases
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------
def encontrar(patron,carpeta,extension):     # Función que busca lo que se envía desde el main
    cmd = 'find ' + carpeta+ ' -name "*' + extension + '" -print 2> /dev/null'       # Comando a ejecutar
    for file in os.popen(cmd).readlines():      #Por cada fichero encontrado dentro del comando cargamos las lineas
        num = 1
        name = file[:-1]                        # Almacenamos el nombre del fichero
        if os.path.isdir(name) == False:            # Comprobamos que lo analizado no sea un directorio
            try:                                            #Tratamiento de excepciones
                for line in open(name).readlines():         # Realizamos la comparación línea por línea
                    pos = string.find(line,patron)          # Recogemos la posición en la línea del patrón buscado
                    if pos>=0:                              # Si la posición es mayor que 0
                        print "Fichero: ",name,"Línea: ",num,"Posición: ",pos            # Imprimimos el nombre del fichero, la línea dónde se ha encontrado el patrón y la posición concreta
                        print '....',line[:-1]                      # Imprimimos la línea concreta
                        print '....', ' '*pos + '*', '\n'           # Indicamos con un * la posición exacta
			print '----------------------------------------------------'	# Usamos una línea de guiones para delimitar los datos mostrados
                    num+=1                                          # Aumentamos el número de línea
            except: 
                print "El archivo " + name + " no se puede leer"            # Mostramos un mensaje de error para aquellos archivos que no pueden ser abiertos
    return True;
    
def options():
    print "Uso:\t localizarPatron patron [directorio] [extensión]"          # Mensaje explicativo sobre cómo utilizar el programa
    return 
    
def keyInterrupt():
    print "\nSe ha interrumpido la ejecución del programa"                  # Mensaje que se muestra el interrumpir la ejecución del programa desde el teclado (por el usuario)
    return
# ---------------------------------------------------------------------

def main(): 
    if len(sys.argv)==1:                    # Si no se ha introducido el patrón a buscar 
        options()                           # Mostramos un mensaje sobre el usi del programa
    elif len(sys.argv)==2:                   # Si sólo hay 2 parámetros pasados
        try:    
            patron = sys.argv[1]                # Obtenemos el patrón a buscar
            carpeta = "."                       # Establecemos el directorio actual para la búsqueda
            ext = ""                            # Y dejamos la extensión vacía (buscar en todos los ficheros)
            encontrar(patron,carpeta,ext)           # Llamamos a la función y le pasamos el patrón a buscar, el directorio y la extensión
        except KeyboardInterrupt:               # Controlamos la excepción de interrupción por teclado
            keyInterrupt()                      # Llamamos a la función para mostrar un mensaje
    elif len(sys.argv)==3:                     # En caso de haber tres parámetros introducidos
        try:
            patron = sys.argv[1]                # Recogemos el patrón a buscar
            carpeta = sys.argv[2]               # Recogemos el PATH dónde se encuentran los ficheros en los que realizaremos la búsqueda
            ext = ""                            # Dejamos la extensión vacía para buscar en todos los ficheros
            encontrar(patron,carpeta,ext)           # Llamamos a la función y le pasamos el patrón a buscar, el directorio y la extensión
        except KeyboardInterrupt:               # Controlamos la excepción de interrupción por teclado
            keyInterrupt()                      # Llamamos a la función para mostrar un mensaje
    elif len(sys.argv)==4:                      # En caso de haber cuatro parámetros introducidos
        try:
            patron = sys.argv[1]                # Recogemos el patrón a buscar
            carpeta = sys.argv[2]               # Recogemos el PATH dónde se encuentran los ficheros en los que realizaremos la búsqueda
            ext = sys.argv[3]                   # Recogemos la extensión
            ext = "." + ext                     # Le concatenamos el punto delante (para que el usuario no tenga que introducirlo)
            encontrar(patron,carpeta,ext)           # Llamamos a la función y le pasamos el patrón a buscar, el directorio y la extensión
        except KeyboardInterrupt:               # Controlamos la excepción de interrupción por teclado
            keyInterrupt()                      # Llamamos a la función para mostrar un mensaje
    else:                                       # Si se han introducido más parámetros de los necesarios
        options()                               # Mostramos el mensaje de "uso" del programa
            
            
if __name__ == "__main__":
    main()

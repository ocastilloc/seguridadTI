#El modulo os nos permite acceder a funcionalidades dependientes del Sistema Operativo, por ejemplo
#manipular estructura del sistema de archivos (Leer y escribir).
#El modulo sys es el encargado de proveer variables y funcionalidades, directamente relacionadas con el intérprete.
import sys, os 
#Modulo para cifrar datos
import cifrar
#Modulo para descifrar datos
import descifrar
#Modulo para el uso de expresiones regulares
import re
from unicodedata import normalize
#Funcion principal
#modo: para cifrar utilizar la palabra "cifrar" y para descifrar "descifrar"
#rutaArchivoEntrada: ruta del archivo de entrada de tipo, texto plano (.TXT)
#rutaArchivoSalida: ruta del archivo de salida de tipo, texto plano que contiene los datos
#resultantes del cifrado o descifrado.
def main(modo,rutaArchivoEntrada,rutaArchivoSalida):
    
    contenidoArchivo=""
    leerArchivoEntrada=open(rutaArchivoEntrada, 'r') #abrir archivo con permisos de lectura.
    palabraResultado=""
    leerArchivoSalida=open(rutaArchivoSalida, "w") #abrir archivo con permisoso de escritura.
    respuestaFinal="No fue posible realizar la operación."
    
    try:
        #leer archivo 
        contenidoArchivo+=leerArchivoEntrada.read()
        #Eliminar diacriticos
        contenidoArchivo = re.sub(
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", contenidoArchivo), 0, re.I
        )
        #Normalizar NFC
        contenidoArchivo = normalize( 'NFC', contenidoArchivo)
        #Eliminar comas, comillas dobles y saltos de linea.
        contenidoArchivo = contenidoArchivo.upper().strip().replace(",","")
        contenidoArchivo = contenidoArchivo.upper().strip().replace('"','')
        palabraFormateada = contenidoArchivo.upper().strip().replace("\n"," ")
        #convertir el texto formateado a una lista
        lista = list(palabraFormateada)
        #convertir a mayuscula la palabra cifrar o descifrar
        modoOperar = modo.upper()
        #Diccionario con el alfabeto español
        alfabeto={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,
                  "K":10,"L":11,"M":12,"N":13,"Ñ":14,"O":15,"P":16,"Q":17,"R":18,
                  "S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26," ":27,".":28}
        #Corresponde al valor del módulo N
        modulo=29
        #Modo de operacion cifrar o descifrar
        if modoOperar == "CIFRAR":
            #Seleccion de la funcion cifrar del modulo cifrar
            palabraResultado = cifrar.cifrar(alfabeto,lista,modulo)
        elif modoOperar == "DESCIFRAR":
            #Seleccion de la funcion descifrar del modulo descifrar
            palabraResultado = descifrar.descifrar(alfabeto,lista,modulo)
        else:
             #Mostrara mensaje por pantalla en el caso de digitar una palabra distinta a cifrar o descifrar
             sys.exit('No existe el modo de operación ingresado')
        
        #escribir archivo de salida
        print(palabraResultado, file=leerArchivoSalida)
        #Mensaje con la salida de la funcion
        respuestaFinal="Operación realizada con exito, revisar archivo de salida."
        #Instrucciones del error   
    except BlockingIOError as eb:
        print("Problema con el archivo: ",eb)
    except FileNotFoundError as ef:
        print("Archivo no encontrado: ",ef)
    except Exception as e:
        print("Error general: ",e)
        tipoException, exc_obj, exc_tb = sys.exc_info()
        archivoError = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("Tipo de excepcion : ",tipoException)
        print("Archivo que contiene el error : ",archivoError)
        print("Numero de la linea con el error : ",exc_tb.tb_lineno)
        
    finally:
        #cerrar la lectura y escritura de archivos
         leerArchivoEntrada.close()
         leerArchivoSalida.close()
    
    return respuestaFinal

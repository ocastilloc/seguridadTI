import sys, os
import cifrar
import descifrar
import re
from unicodedata import normalize
#archivo principal
#palabra: corresponde a un texto a cifrar o descifrar
#modo: para cifrar utilizar la palabra "cifrar" y para descifrar "descifrar"
def main(modo,rutaArchivoEntrada,rutaArchivoSalida):
    
    contenidoArchivo=""
    #debe entregar la ruta del archivo de entrada, por ejemplo:
    #/ProyectoPython/seguridadTI/recursos/entrada.txt
    #la ruta aplica tanto en windows como en linux
    leerArchivoEntrada=open(rutaArchivoEntrada, 'r')
    palabraResultado=""
    leerArchivoSalida=open(rutaArchivoSalida, "w")
    respuestaFinal="No fue posible realizar la operación."
    
    try:
        
        #Instrucciones del aplicativo
        #Abrir texto y lerlo
        contenidoArchivo+=leerArchivoEntrada.read()
        
        #Eliminar diacriticos
        contenidoArchivo = re.sub(
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", contenidoArchivo), 0, re.I
        )
    
        #Normalizar NFC
        contenidoArchivo = normalize( 'NFC', contenidoArchivo)
   
        #eliminar espacios en blanco
        contenidoArchivo = contenidoArchivo.upper().strip().replace(",","")
        contenidoArchivo = contenidoArchivo.upper().strip().replace('"','')
        palabraFormateada = contenidoArchivo.upper().strip().replace("\n"," ")
        
        lista = list(palabraFormateada)
        modoOperar = modo.upper()
        
        #diccionario con el alfabeto español
        alfabeto={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,
                  "K":10,"L":11,"M":12,"N":13,"Ñ":14,"O":15,"P":16,"Q":17,"R":18,
                  "S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26," ":27,".":28}
        
        modulo=29 # n
        
        #Modo de operacion cifrar o descifrar
        
        if modoOperar == "CIFRAR":
            palabraResultado = cifrar.cifrar(alfabeto,lista,modulo)
        elif modoOperar == "DESCIFRAR":
            palabraResultado = descifrar.descifrar(alfabeto,lista,modulo)
        else:
             sys.exit('No existe el modo de operación ingresado')
        
        #escribir archivo
        print(palabraResultado, file=leerArchivoSalida)
        
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
        #cerrar recursos
         leerArchivoEntrada.close()
         leerArchivoSalida.close()
    
    #Leer archivo de entrada desde dirección web:
    
    return respuestaFinal

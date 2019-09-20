#El modulo os nos permite acceder a funcionalidades dependientes del Sistema Operativo, por ejemplo
#manipular estructura del sistema de archivos (Leer y escribir).
#El modulo sys es el encargado de proveer variables y funcionalidades, directamente relacionadas con el intérprete.
import sys, os
#Funcion utilizada para obtener el valor decimacion y desplazamiento.
#x: indice actual del ciclo
#y: indice siguiente del ciclo
#clave: corresponde a una clave privada
#alfabeto: lista con el alfabeto español.
def clave(x,y,clave,alfabeto):
    
    try:
        letraMensajeDecimacion = clave[x]
        letraMensajeDesplazamiento = clave[y]
    
        valorDecimacion = alfabeto[letraMensajeDecimacion]
        valorDesplazamiento = alfabeto[letraMensajeDesplazamiento]
    
        resultado=""
        #Lista con el retorno de la función, valor de decimacion y desplazamiento.
        resultado= {"valorDecimacion":valorDecimacion, "valorDesplazamiento":valorDesplazamiento}
    
    except Exception as e:
         tipoException, exc_obj, exc_tb = sys.exc_info()
         archivoError = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         #Lanzar la excepcion al modulo que invoca la funcion.
         raise ValueError("Error en archivo : ",archivoError," en la linea : ",exc_tb.tb_lineno) from e    

    return resultado

#funcion que contiene una o mas claves privadas
def diccionarioClave(indiceClave):
    
    try:
        #Lista con 8 claves privadas
        diccionarioClave = {'clave': ['XHCDFEWI','ZFHJVÃ‘TS','OJGNRQPM','HRLÃ‘GVW','SXODUZER','ICQYG.Ã‘T','EWLIFSZO','RKNUVKXL'] }
        #corresponde a una clave privada
        clave = diccionarioClave['clave'][indiceClave]
        #valor numerico con el total de claves privadas
        cantidadClave = len(diccionarioClave['clave'])
        #retorno de la funcion, una clave privada y cantidad de claves
        retorno = {"clave":clave,"cantidadClaves":cantidadClave}
    
    except Exception as e:
        tipoException, exc_obj, exc_tb = sys.exc_info()
        archivoError = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         #Lanzar la excepcion al modulo que invoca la funcion.
        raise ValueError("Error en archivo : ",archivoError," en la linea : ",exc_tb.tb_lineno) from e
     
    return retorno
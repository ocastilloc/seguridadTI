# Contiene una clave o grupo de ellas para generar la cosntante de decimación y desplazamiento.
import sys, os

def clave(x,y,clave,alfabeto):
    
    try:
        letraMensajeDecimacion = clave[x]
        letraMensajeDesplazamiento = clave[y]
    
        valorDecimacion = alfabeto[letraMensajeDecimacion]
        valorDesplazamiento = alfabeto[letraMensajeDesplazamiento]
    
        resultado=""
        resultado= {"valorDecimacion":valorDecimacion, "valorDesplazamiento":valorDesplazamiento}
    
    except Exception as e:
        print("Error general: ",e)
        tipoException, exc_obj, exc_tb = sys.exc_info()
        archivoError = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("Tipo de excepción : ",tipoException)
        print("Archivo que contiene el error : ",archivoError)
        print("Número de la linea con el error : ",exc_tb.tb_lineno)     
     

    return resultado

#funcion que contiene una o más claves privadas
def diccionarioClave(indiceClave):
    
    try:
        diccionarioClave = {'clave': ['XHCDFEWI','ZFHJVÑTS','OJGNRQPM','HRLÑGVW','SXODUZER','ICQYG.ÑT','EWLIFSZO','RKNUVKXL'] }
        clave = diccionarioClave['clave'][indiceClave]
        cantidadClave = len(diccionarioClave['clave'])
    
        retorno = {"clave":clave,"cantidadClaves":cantidadClave}
    
    except Exception as e:
        print("Error general: ",e)
        tipoException, exc_obj, exc_tb = sys.exc_info()
        archivoError = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("Tipo de excepción : ",tipoException)
        print("Archivo que contiene el error : ",archivoError)
        print("Número de la linea con el error : ",exc_tb.tb_lineno)     
     
    return retorno
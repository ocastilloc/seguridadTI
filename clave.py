# Contiene una clave o grupo de ellas para generar la cosntante de decimación y desplazamiento.

def clave(x,y,clave,alfabeto):
    
    letraMensajeDecimacion = clave[x]
    letraMensajeDesplazamiento = clave[y]
    
    valorDecimacion = alfabeto[letraMensajeDecimacion]
    valorDesplazamiento = alfabeto[letraMensajeDesplazamiento]
    
    resultado=""
    resultado= {"valorDecimacion":valorDecimacion, "valorDesplazamiento":valorDesplazamiento}
    
    return resultado

#funcion que contiene una o más claves privadas
def diccionarioClave(indiceClave):
     
    
    diccionarioClave = {'clave': ['XHCDFEWI','ZFHJVÑTS','OJGNRQPM','HRLÑGVW','SXODUZER','ICQYG.ÑT','EWLIFSZO','RKNUVKXL'] }
    
    clave = diccionarioClave['clave'][indiceClave]
    cantidadClave = len(diccionarioClave['clave'])
    
    retorno = {"clave":clave,"cantidadClaves":cantidadClave}
     
    return retorno
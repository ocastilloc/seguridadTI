# Contiene una clave o grupo de ellas para generar la cosntante de decimación y desplazamiento.
def clave(x,y,clave,alfabeto):
    
    letraMensajeDecimacion = clave[x]
    letraMensajeDesplazamiento = clave[y]
    
    valorDecimacion = alfabeto[letraMensajeDecimacion]
    valorDesplazamiento = alfabeto[letraMensajeDesplazamiento]
    
    #print("Decimacion ",valorDecimacion," Desplazamiento ",valorDesplazamiento)
    
    resultado=""
    resultado= {"valorDecimacion":valorDecimacion, "valorDesplazamiento":valorDesplazamiento}
    
    return resultado

#funcion que contiene una o más claves privadas
def diccionarioClave():
     
    claves = "XHCDFEWI"
     
    return claves
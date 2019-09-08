# Contiene una clave o grupo de ellas para generar la cosntante de decimación y desplazamiento.
def clave(x,y,clave):
    
    letraActual = clave[x];
    letraSiguiente = clave[y]
    
    print("Decimacion ",letraActual)
    print("Desplazamiento",letraSiguiente)
    
    resultado=""
    resultado= {"decimacion":letraActual, "desplazamiento":letraSiguiente}
    
    return resultado

#funcion que contiene una o más claves privadas
def diccionarioClave():
     
    claves = "XBCDFEWI"
     
    return claves
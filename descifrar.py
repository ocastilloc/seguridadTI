import euclidesExtendido
import clave

def descifrar(alfabeto,palabraFormateada,modulo):
    
    #Obtener el codigo de cada letra para cifrar
    largoPalabra=len(palabraFormateada)
    palabraDescifrada = ""
    
    valX=0
    valY=1
    x=0
    y=0
    
    #Descifrar letra por letra
    for contador in range(largoPalabra):
        
        if x == 0:
            x=valX
            y=valY
         
        contenidoClave = clave.diccionarioClave()
        largoClave = len(contenidoClave)-1
        
        if x >= largoClave:
            x=0
            y=1
        
        resultadoClave = clave.clave(x,y,contenidoClave,alfabeto)
        x=x+1
        y=x+1
        
        valorDecimacion = resultadoClave["valorDecimacion"]
        valorDesplazamiento = resultadoClave["valorDesplazamiento"]
        
        #Inverso multiplicativo
        inversoMultiplicativo = euclidesExtendido.euclidesExtendido(modulo,valorDecimacion)["inversoMultiplicativo"]
        
        
        letraMensaje = palabraFormateada[contador]
        codigoLetra = alfabeto[letraMensaje]
        
        parteUno = codigoLetra - valorDesplazamiento
        
        if(parteUno < 0):
            parteUno = codigoLetra + modulo - valorDesplazamiento
        
        #Aplicar formula considerando validaciones
        valorLetraDescifrada = (inversoMultiplicativo * (parteUno) ) % modulo
        
        letraDescifrada = list(alfabeto.keys())[list(alfabeto.values()).index(valorLetraDescifrada)]
        
        palabraDescifrada = palabraDescifrada + letraDescifrada
            
    
    return palabraDescifrada
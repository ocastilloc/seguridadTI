def descifrar(alfabeto,diccionario,palabraFormateada,constanteDecimacion,constanteDesplazamiento,modulo):
    
    #validaciones
    
    #Si la constanteDecimacion = 1 se dice que el desplazamiento es puro y no se debe usar en la formula.
    inversoMultiplicativo=1
    
    if constanteDecimacion != 1:
        inversoMultiplicativo = diccionario["inversoMultiplicativo"]
            
    #Obtener el codigo de cada letra para cifrar
    largoPalabra=len(palabraFormateada)
    palabraDescifrada = ""
    
    #Descifrar letra por letra
    for contador in range(largoPalabra):
        letraMensaje = palabraFormateada[contador]
        codigoLetra = alfabeto[letraMensaje]
        
        parteUno = codigoLetra - constanteDesplazamiento
        
        if(parteUno < 0):
            parteUno = codigoLetra + modulo - constanteDesplazamiento
        
        #Aplicar formula considerando validaciones
        valorLetraDescifrada = (inversoMultiplicativo * (parteUno) ) % modulo
        
        letraDescifrada = list(alfabeto.keys())[list(alfabeto.values()).index(valorLetraDescifrada)]
        
        palabraDescifrada = palabraDescifrada + letraDescifrada
            
    
    return palabraDescifrada

import clave
def cifrar(alfabeto,palabraFormateada,constanteDecimacion,constanteDesplazamiento,modulo):
    
     #Obtener el codigo de cada letra para cifrar
    largoPalabra=len(palabraFormateada)
    largoAlfabeto=len(alfabeto)-1;
    
    palabraCifrada = ""
    
    valX=0
    valY=1
    x=0
    y=0
    
    for contador in range(largoPalabra):
        
        if x == 0:
            x=valX
            y=valY
         
        contenidoClave = clave.diccionarioClave()
        largoClave = len(contenidoClave)-1
        
        if x >= largoClave:
            x=0
            y=1
        
        clave.clave(x,y,contenidoClave)
        x=x+1
        y=x+1
    
        
        letraMensaje = palabraFormateada[contador]
        codigoLetra = alfabeto[letraMensaje]
        
        #Formula cifrar:
        #C= (X*A+Y) MOD N
        valorLetraCifrada=0
        valorLetraCifrada = (constanteDecimacion * codigoLetra + constanteDesplazamiento) % modulo
        
        if valorLetraCifrada > largoAlfabeto:
            letraCifrada = list(alfabeto.keys())[list(alfabeto.values()).index(largoAlfabeto)]
        else:
            letraCifrada = list(alfabeto.keys())[list(alfabeto.values()).index(valorLetraCifrada)]
        
        palabraCifrada = palabraCifrada + letraCifrada
    
    return palabraCifrada

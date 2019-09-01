def cifrar(alfabeto,palabraFormateada,constanteDecimacion,constanteDesplazamiento,modulo):
    
     #Obtener el codigo de cada letra para cifrar
    largoPalabra=len(palabraFormateada)
    palabraCifrada = ""
    
    for contador in range(largoPalabra):
        letraMensaje = palabraFormateada[contador]
        codigoLetra = alfabeto[letraMensaje]
      
        #Formula cifrar:
        #C= (X*A+Y) MOD N
        valorLetraCifrada = (constanteDecimacion * codigoLetra + constanteDesplazamiento) % modulo
        
        letraCifrada = list(alfabeto.keys())[list(alfabeto.values()).index(valorLetraCifrada)]
        
        palabraCifrada = palabraCifrada + letraCifrada
    
    return palabraCifrada

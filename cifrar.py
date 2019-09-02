def cifrar(alfabeto,palabraFormateada,constanteDecimacion,constanteDesplazamiento,modulo):
    
     #Obtener el codigo de cada letra para cifrar
    largoPalabra=len(palabraFormateada)
    largoAlfabeto=len(alfabeto)-1;
    
    palabraCifrada = ""
    
    for contador in range(largoPalabra):
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

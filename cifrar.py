def cifrar(alfabeto,palabraFormateada,constanteDecimacion,constanteDesplazamiento,modulo):
    
     #Obtener el codigo de cada letra para cifrar
    largoPalabra=len(palabraFormateada)
    
    for contador in range(largoPalabra):
        letraMensaje = palabraFormateada[contador]
        codigoLetra = alfabeto[letraMensaje]
        print(codigoLetra)
    
    return 0

import euclidesExtendido
import clave
import sys, os

def descifrar(alfabeto,palabraFormateada,modulo):
    
    #Obtener el codigo de cada letra para cifrar
    
    try:
        
        largoPalabra=len(palabraFormateada)
        palabraDescifrada = ""
        
        valX=0
        valY=1
        x=0
        y=0
        indiceClave=0
    
        #Descifrar letra por letra
        for contador in range(largoPalabra):
            
            if x == 0:
                x=valX
                y=valY
         
            llamarContenidoClave = clave.diccionarioClave(indiceClave)
            contenidoClave = llamarContenidoClave["clave"]
            largoClave = len(contenidoClave)-1
            cantidadClave = llamarContenidoClave["cantidadClaves"] -1
         
            if indiceClave >= cantidadClave:
                indiceClave = 0
        
            if x >= largoClave:
                x=0
                y=1
                indiceClave = indiceClave+1
        
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
    
    except Exception as e :
         tipoException, exc_obj, exc_tb = sys.exc_info()
         archivoError = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         raise ValueError("Error en archivo : ",archivoError," en la linea : ",exc_tb.tb_lineno) from e    
    
    return palabraDescifrada
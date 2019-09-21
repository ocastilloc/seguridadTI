#Modulo clave, la cual contiene las funciones: clave y diccionarioClave.
import clave
#El modulo os nos permite acceder a funcionalidades dependientes del Sistema Operativo, por ejemplo
#manipular estructura del sistema de archivos (Leer y escribir).
#El modulo sys es el encargado de proveer variables y funcionalidades, directamente relacionadas con el intérprete.
import sys, os
#Función cifrar con tres parametros de entrada:
#alfabeto: lista con el alfabeto español.
#palabraFormateada: Contenido del archivo de texto.
#modulo: Valor numerico del modulo.
def cifrar(alfabeto,palabraFormateada,modulo):
    
    try:
         #cantidad de caracteres del texto a cifrar
         largoPalabra=len(palabraFormateada)
         largoAlfabeto=len(alfabeto)-1;
    
         #Inicializar variables utilizadas en el proceso de cifrado
         palabraCifrada = ""
         valX=0
         valY=1
         x=0
         y=0
         indiceClave=0
         
         #Ciclo para cifrar caracter por caracter.
         for contador in range(largoPalabra):
             #Si x es igual a 0, x tomara el valor 0 e y el valor 1   
             if x == 0:
                 x=valX
                 y=valY
             #llamar una clave de la lista de claves         
             llamarContenidoClave = clave.diccionarioClave(indiceClave)
             contenidoClave = llamarContenidoClave["clave"]
             #cantidad de caracteres de la clave   
             largoClave = len(contenidoClave)-1
             cantidadClave = llamarContenidoClave["cantidadClaves"] -1
             #Si indiceClave es mayor o igual a cantidadClave, indiceClave volvera a 0   
             if indiceClave >= cantidadClave:
                 indiceClave = 0
             #Si x es mayor o igual a largoClave, entonces x volvera a 0 e y a 1. indiceClave aumentara en 1.   
             if x >= largoClave:
                 x=0
                 y=1
                 indiceClave = indiceClave+1
             #invocar a funcion clave para obtener valor decimacion y desplazamiento   
             resultadoClave = clave.clave(x,y,contenidoClave,alfabeto)
             x=x+1
             y=x+1
                
             valorDecimacion = resultadoClave["valorDecimacion"]
             valorDesplazamiento = resultadoClave["valorDesplazamiento"]
            
             #Obtener letra y codigo de la letra asignado en el diccionario del alfabeto   
             letraMensaje = palabraFormateada[contador]
             codigoLetra = alfabeto[letraMensaje]
                
             #Formula cifrar:
             #C= (X*A+Y) MOD N
             valorLetraCifrada=0
             valorLetraCifrada = (valorDecimacion * codigoLetra + valorDesplazamiento) % modulo
                
             if valorLetraCifrada > largoAlfabeto:
                 letraCifrada = list(alfabeto.keys())[list(alfabeto.values()).index(largoAlfabeto)]
             else:
                 letraCifrada = list(alfabeto.keys())[list(alfabeto.values()).index(valorLetraCifrada)]
             #Texto cifrado   
             palabraCifrada = palabraCifrada + letraCifrada
    
    except Exception as e:
         tipoException, exc_obj, exc_tb = sys.exc_info()
         archivoError = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         #Lanzar excepcion al modulo que lo invoca.
         raise ValueError("Error en archivo : ",archivoError," en la linea : ",exc_tb.tb_lineno) from e
    #Retorno del texto cifrado
    return palabraCifrada

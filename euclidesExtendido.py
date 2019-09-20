#El modulo os nos permite acceder a funcionalidades dependientes del Sistema Operativo, por ejemplo
#manipular estructura del sistema de archivos (Leer y escribir).
#El modulo sys es el encargado de proveer variables y funcionalidades, directamente relacionadas con el intérprete.
import sys, os
#Funcion utilizada para obtener el maximo comun divisor y el inverso multiplicativo, utilizado en la funcion
#para descifrar.
#a: corresponde al valor de decimacion
#b: corresponde al valor del modulo
def euclidesExtendido(a, b):
    
	#En el caso de que b tenga el valor 0, retornar 0,1,0
	# no puede existir un dividor 0
    try:
        if b == 0:
            return 0,1,0
    
        u0 = 1; v0 = 0
        u1 = 0; v1 = 1
    
        while b != 0:
            cociente = a//b
            resto = a - b * cociente
        
            #Actualizar a,b
            a = b
            b = resto
            # valores para u, v para obtener la mínima, combinación lineal.
            u = u0 - cociente * u1
            v = v0 - cociente * v1
            
            #Actualizar valores en cada iteración
            u0 = u1; v0 = v1
            u1 = u; v1 = v
            #La funcion retorna un diccionario con tres valores:
            #Maximo comun divisor, el minimo y el inverso multiplicativo.
            diccionario={"maximoComunDivisor":a,"minimo":u0,"inversoMultiplicativo":v0}
        
    except Exception as e:
        tipoException, exc_obj, exc_tb = sys.exc_info()
        archivoError = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        #En el caso de error la excepción sera lanzada al programa que invoca a la función euclidesExtendido.
        raise ValueError("Error en archivo : ",archivoError," en la linea : ",exc_tb.tb_lineno) from e  
 
    return diccionario
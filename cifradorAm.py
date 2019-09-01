import euclidesExtendido

#palabra: corresponde a un texto a cifrar o descifrar
#modo: para cifrar utilizar la palabra "cifrar" y para descifrar "descifrar"
def main(palabra,modo):
    #eliminar espacios en blanco
    palabraFormateada =palabra.replace(" ", "")
    
    #Obtener el máximo común divisor para comprobar que n e x sean coprimos (solo divisibles por 1)
    #Tener el inverso multiplicativo para la función descifrar.
    diccionario = euclidesExtendido.euclidesExtendido(29,5)
    
    return diccionario, palabraFormateada

import sys
import euclidesExtendido
import cifrar
import descifrar

#palabra: corresponde a un texto a cifrar o descifrar
#modo: para cifrar utilizar la palabra "cifrar" y para descifrar "descifrar"
def main(palabra,modo):
    #eliminar espacios en blanco
    palabraFormateada =palabra.replace(" ", "").upper()
    
    #diccionario con el alfabeto español
    alfabeto={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,
              "K":10,"L":11,"M":12,"N":13,"Ñ":14,"O":15,"P":16,"Q":17,"R":18,
              "S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    
    #constanteDecimacion y constanteDesplazamiento serán obtenidas
    #de la funcion f(clave)=x,y
    constanteDecimacion=5 #x
    constanteDesplazamiento=15 #y
    modulo=29 # n
    
    #Validaciones variables
    if (constanteDesplazamiento < 0 or constanteDesplazamiento > modulo or constanteDecimacion < 0):
        sys.exit('Valores incorrectos en la constanteDesplazamiento o constanteDecimacion')
    
    #modulo y constanteDecimacion deben ser coprimos (solo divisibles por 1)
    #necesario para obtener el inverso multiplicador
    diccionario = euclidesExtendido.euclidesExtendido(modulo,constanteDecimacion)
    
    if diccionario["maximoComunDivisor"] != 1:
        sys.exit('La constanteDecimacion y modulo no son coprimos')
    
    #Modo de operacion cifrar o descifrar
    if modo == "cifrar":
        cifrar.cifrar(alfabeto,palabraFormateada,constanteDecimacion,constanteDesplazamiento,modulo)
    else:
        descifrar.descifrar()

    return diccionario,palabraFormateada,alfabeto

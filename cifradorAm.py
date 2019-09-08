import sys
#import euclidesExtendido
import cifrar
import descifrar

#palabra: corresponde a un texto a cifrar o descifrar
#modo: para cifrar utilizar la palabra "cifrar" y para descifrar "descifrar"
def main(palabra,modo):
    #eliminar espacios en blanco
    #palabraFormateada =palabra.replace(" ", "").upper()
    palabraFormateada = palabra.upper().strip()
    modoOperar = modo.upper()
    
    #diccionario con el alfabeto español
    alfabeto={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,
              "K":10,"L":11,"M":12,"N":13,"Ñ":14,"O":15,"P":16,"Q":17,"R":18,
              "S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26," ":27,".":28}
    
    modulo=29 # n
    
    #Modo de operacion cifrar o descifrar
    
    if modoOperar == "CIFRAR":
        palabraResultado = cifrar.cifrar(alfabeto,palabraFormateada,modulo)
    elif modoOperar == "DESCIFRAR":
        palabraResultado = descifrar.descifrar(alfabeto,palabraFormateada,modulo)
    else:
         sys.exit('No existe el modo de operación ingresado')

    return palabraResultado

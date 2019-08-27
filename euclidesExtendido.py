def euclidesExtendido(a, b):
    
	#En el caso de que b tenga el valor 0, retornar 0,1,0
	# no puede existir un dividor 0
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
        # valores para u, v
        u = u0 - cociente * u1
        v = v0 - cociente * v1
        
        #Actualizar valores en cada iteración
        u0 = u1; v0 = v1
        u1 = u; v1 = v
 
    return  a, u0, v0

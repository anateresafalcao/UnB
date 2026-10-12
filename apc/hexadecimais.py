def hexadecimais(R, G, B):
    numeros = '0123456789ABCDEF'
    R = int(R)
    ir = R % 16
    
    kr = R // 16
    
    R = numeros[ir] + numeros[kr]
    
    G = int(G)
    restoG = G % 16
    resultadoG = G // 16
    restoG = str(restoG)
    resultadoG = str(resultadoG)
    G = numeros[restoG] + numeros[resultadoG]
    
    B = int(B)
    restoB = B % 16
    resultadoB = B // 16
    restoB = str(restoB)
    resultadoB = str(resultadoB)
    G = numeros[restoB] + numeros[resultadoB]
    
    print(f'{cor} #{R:02}{G:02}{B:02}')
    

cor, R, G, B = input().split(',')
print(f'{hexadecimais(R, G, B)}')

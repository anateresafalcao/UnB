def ehPrimo(x):
#retorna 0 se não é primo
#retorna 1 se é primo
    if x == 2:
        print('1')
    if (x % 2) == 0:
        print('0')
    else:
        contador = 1
        while contador <= x:
            contador += 1
            if (x % contador) == 0:
                print ('0')
                break
            else:
                print ('1')
                break
    
    
    
    
    
    
    
    
    
    
    
    
    
    contador = 0
    while x >= contador:
        contador = contador + 1
        if (x % contador) == 0 and contador != x:
            print('0')
            break
        else:
            print('1')
            break
            
            
ehPrimo(4)            
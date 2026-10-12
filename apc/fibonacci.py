def fibonacci(N):
    if N == 1:
        print('0')
    elif N == 2:
        print('0 1')
    else:
        termo_1 = 0
        termo_2 = 1
        contador = 2
        while contador <= N:
            #precisa atualizar termo_1 e termo_2
            termo_sequencia = termo_1 + termo_2
            termo_1 = termo_2
            termo_2 = termo_sequencia
            contador = contador + 1
            if contador > N:
                break
            print(f'{termo_sequencia}', end=' ')
            
            
           
            
        
        
        
        
        
        
        
        
            
            
            
    
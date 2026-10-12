def não_possui_a_letra_u(palavra):
    letras_u = 'uûüùú'
    palavra = palavra.lower()
    cont = 0
    
    for letra in palavra:
        if letra in letras_u:
            cont += 1
            
    if cont == 0:
         return True
    else:
         return False

    
    
palavra = input()
print(f'{não_possui_a_letra_u(palavra)}')


s = input()

if 'aluguel' in s.lower() or 'alugo' in s.lower() or 'alugar' in s.lower():
    print ('Modalidade: Alguel')
    
if 'venda' in s.lower() or 'vendo' in s.lower() or 'vender' in s.lower():
    print('Modalidade: Venda')
    
if 'casa' in s.lower():
    print('Tipo: Casa')
    
if 'apartamento' in s.lower():
    print('Tipo: Apartamento')

lista = s.split()
endereco =[]

for elemento in lista:
    indice_endereco = 0
    if elemento == 'Rua' or elemento == 'Avenida':
        endereco.append(elemento)
        indice_endereco = lista.index(elemento)
        break
    
for i in range(indice_endereco + 1, len(lista)):
    elemento = lista[i]
    if ',' in elemento:
        novo_elemento = ''
        for caractere in elemento:
            if caractere != ',':
                novo_elemento += caractere
    else:
        novo_elemento = elemento
            
                
    if novo_elemento.isnumeric() == False:
        endereco.append(novo_elemento)
    else:
        endereco.append(novo_elemento)
        break
    
    
    
        
print(f'Endereco: ', end='')
print(*endereco)

cep = []        
for elemento in s.split():
    if elemento == 'CEP':
        indice_cep = (s.split()).index(elemento)
        break
    
if 'CEP' in s:
    print(f'CEP: ', end='')
    for i in range(indice_cep +1, len(s.split()), indice_cep + 7):
        elemento = (s.split())[i]
        cep.append(elemento)
    print(*cep)
else:
    print('CEP: nao informado')
    
area = ['Area: ']   
if 'metros quadrados' or 'm2' in s:
    for elemento in lista:
        if elemento == 'metros' or elemento == 'm2' or elemento == 'quadrados':
            indice_area = lista.index(elemento)
            break
    tamanho = lista[indice_area - 1]
    area.append(tamanho)
    print(*area)

        
            
        
else:
    print('Area: nao informado')


    

        
        

    
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
    if elemento.strip(',').isnumeric():
        endereco.append(elemento.strip(','))
        break
    else:
        endereco.append(elemento)
print(f'Endereco: ', end='')
print(*endereco)


CEP = []
telefone = []
for elemento in lista:
    if '-' in elemento:
        if len(elemento.strip('.,').split('-')[1]) == 3 and (elemento.strip('.,').split('-')[1]).isnumeric():
            CEP = elemento.strip('.,')
        if len(elemento.strip(',.').split('-')[0]) == 4 or len(elemento.strip('.,').split('-')[0])==5 and (elemento.split('-')[0]).isnumeric():
            telefone.append(elemento.strip('.,'))
if CEP == []:
    print('CEP: nao informado')
else:
    print(f'CEP: ', end='')
    print(CEP)
#area
#valor
area = []
if 'metros quadrados' in s or 'm2' in s:
    for elemento in lista:
        indice_area = 0
        if elemento.strip('.,') == 'metros':
            indice_area = lista.index(elemento)
            area.append(lista[indice_area-1])
            break
        if elemento.strip('.,') == 'm2':
            indice_area = lista.index(elemento)
            area.append(lista[indice_area -1])
            break
    
    print(f'Area: ', end='')
    print(*area)
else:
    print('Area: nao informado')
    
valor = []
if 'R$' or 'reais' in lista:
    for elemento in lista:
        indice_valor = 0
        if 'R$' in elemento.strip(',.'):
            if len (elemento.strip(',.')) > 2:
                valor.append(elemento.strip(',.')[2:])
            else:
                indice_valor = lista.index(elemento)
                valor.append(lista[indice_valor +1])
            break
        if elemento.strip(',.') == 'reais':
            indice_valor = lista.index(elemento)
            valor.append(lista[indice_valor -1])
            break
    if valor != []:
        print(f'Valor: ', end='')
        print(*valor)

if len(telefone) == 1:
    print(f'Telefone: ', end='')
    print(*telefone)
else:
    print(f'Telefones: ', end='')    
    print(', '.join(telefone))
    
#responsavel
ultimo_periodo = s.split('.')
achar_nome = ultimo_periodo[-2]
nome = []

if len(achar_nome.split()) == 1:
    nome.append(achar_nome)
    
else:
    for i in range (len(achar_nome.split())):
        if i == len(achar_nome.split())-1:
            if achar_nome.split()[i][0] == achar_nome.split()[i][0].upper() and achar_nome.split()[i] not in nome:
                nome.append(achar_nome.split()[i])
                break
            
        if achar_nome.split()[i][0] == achar_nome.split()[i][0].upper() and achar_nome.split()[i+1][0] == achar_nome.split()[i+1][0].upper():
            nome.append(achar_nome.split()[i])
            nome.append(achar_nome.split()[i+1])
            if len(nome) > 3:
                break
            


print(f'Responsavel: ', end='')        
print(*nome)
    
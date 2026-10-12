s = input()

if 'aluguel' in s.lower() or 'alugo' in s.lower() or 'alugar' in s.lower():
    print ('Modalidade: Aluguel')
    
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
    if elemento.strip(',.').isnumeric():
        endereco.append(elemento.strip(',.'))
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
        if len(elemento.strip(',.').split('-')[1]) == 4 and (elemento.strip(',.').split('-')[0]).isnumeric():
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
    elif valor == []:
        print('Valor: nao informado')
if len(telefone) == 1:
    print(f'Telefone: ', end='')
    print(*telefone)
else:
    print(f'Telefones: ', end='')    
    print(', '.join(telefone))
    
#responsavel
periodos = s.split('.')
ultimo_periodo = periodos[-2]
ultimo_periodo = ultimo_periodo.split()
contador = 0
maiuscula = ''
nome = []

if len(ultimo_periodo) == 1:
    nome.append(ultimo_periodo)
else:
    for elemento in ultimo_periodo:
        if elemento[0].islower():
            contador = 0
        elif elemento[0].isupper() and contador == 0:
            contador += 1
            maiuscula = elemento
        else:
            if elemento[0].isupper() and contador == 1:
                nome.append(maiuscula.strip('.,'))
                nome.append(elemento.strip('.,'))
                contador += 1
            elif elemento[0].isupper() and contador > 1:
                nome.append(elemento.strip('.,'))
            



print(f'Responsavel: ', end='')        
print(*nome)
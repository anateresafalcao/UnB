n_mercearias, mangos, min_produtos = input().split()
n_mercearias = int(n_mercearias)
mangos = int(mangos)
min_produtos = int(min_produtos)


produtos_por_mercearia = input().split()
produtos_por_mercearia = list(map(int, produtos_por_mercearia))

produtos = []
for i in range(n_mercearias):
    descricao = input().split()
    descricao = list(map(int, descricao))
    produtos.append(descricao)

contador = 0
tem_suficiente = 'sim'
while contador < n_mercearias:
    if (produtos_por_mercearia[contador]) < min_produtos:
        tem_suficiente = 'nao'
    contador += 1

if tem_suficiente == 'nao':
    print('Não')
    
else:
    para_comprar = []
    produtos.sort()
    for elemento in produtos:
        elemento = elemento[:min_produtos]
        para_comprar.append(elemento)
    
    total = 0  
    for elemento in para_comprar:
        total += sum(elemento)
    
    if total <= mangos:
        print('Sim')
    
    else:
        print('Não')
    
    
        
    




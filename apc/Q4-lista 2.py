qntd_mercearias, mangos, min_produtos = input().split()
qntd_mercearias = int(qntd_mercearias)
mangos = int(mangos)
min_produtos = int(min_produtos)
produtos_por_mercearia = input().split()
lista_produtos =[]

for i in range(qntd_mercearias):
    produtos = input().split()
    produtos = list(map(int, produtos))
    produtos.sort()
    lista_produtos.append(produtos)
    

tem_suficiente = 'sim'
for produtos in lista_produtos:
    if len(produtos) < min_produtos:
        tem_suficiente = 'nao'
        
if tem_suficiente == 'nao':
    print('Nao')
    
else:
    preco_total = 0

    for i in range(qntd_mercearias):
        lista_produtos[i] = lista_produtos[i][:min_produtos]
        preco_total += sum(lista_produtos[i])
    if preco_total > mangos:
        print('Nao')
        
    else:
        print('Sim')
        
        
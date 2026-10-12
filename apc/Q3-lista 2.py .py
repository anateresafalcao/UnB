linhas, colunas = input().split()
linhas = int(linhas)
colunas = int(colunas)

lancamentos = int(input())
matriz =[]
for i in range(linhas):
    matriz.append([0]*colunas)

for i in range(lancamentos):
    x, y = input().split()
    x = int(x) - 1
    y = int(y) - 1
    
    for i in range(colunas):
        if i != y:
            matriz[x][i] += 1
            
    for j in range(linhas):
            matriz[j][y] += 1
    
maior_buraco = 0
for linha in matriz:
    for elemento in linha:
        if elemento > maior_buraco:
            maior_buraco = elemento

quantidade = 0
for linha in matriz:
    quantidade += linha.count(maior_buraco)
    
print(quantidade)
    
    
    
    
    
    
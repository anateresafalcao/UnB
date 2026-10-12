n = int(input())
t = int(input())
dados_linha = []
matriz = []

for i in range(n):
    linha = input().split()
    linha = list(map(int, linha))
    dados_linha = []
    dados_linha.append(linha[t])
    dados_linha.append(sum(linha))
    dados_linha.append(linha)
    matriz.append(dados_linha)
    
matriz.sort()

for informacao in matriz:
    print(*informacao[2])
    
    
    

    
linhas, colunas, f = input().split()
linhas = int(linhas)
colunas = int(colunas)
f = int(f)
matriz = []

for i in range(linhas):
    linha = input().split()
    linha = list(map(int, linha))
    linha.sort()
    linha.reverse()
    matriz.append(linha)

novas_linhas = int(linhas/f)
novas_colunas = int(colunas/f)
nova_matriz = []

for i in range(novas_linhas):
    nova_matriz.append([0]*novas_colunas)

tam_nova_matriz = 0
for linha in nova_matriz:
    for elemento in linha:
        tam_nova_matriz += 1
        
matriz_final= [0]*tam_nova_matriz


for i in range(tam_nova_matriz):
    matriz_final[i] = matriz[i][0]
    
print(*matriz_final)

    
    

    
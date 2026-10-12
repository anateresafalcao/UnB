n = int(input())
matriz = []

for i in range(n):
    matriz.append(input().split())
    
#diagonal principal
i = 0
diagonal_principal = []
for linha in matriz:
    diagonal_principal.append(matriz[i][i])
    i += 1
    
j = 0
elemento = n-1
diagonal_secundaria = []
for linha in matriz:
    diagonal_secundaria.append(matriz[j][elemento])
    j +=1
    elemento -= 1
    

principal_tem_x = 'sim'
for elemento in diagonal_principal:
    if elemento != 'X':
        principal_tem_x = 'nao'
        
secundaria_tem_x = 'sim'
for elemento in diagonal_secundaria:
    if elemento != 'X':
        secundaria_tem_x = 'nao'
        
if principal_tem_x == 'nao'or secundaria_tem_x == 'nao':
    print('Talvez o tesouro seja os amigos que fizemos no caminho')
else:
    maximo_de_x = len(diagonal_principal) + len(diagonal_secundaria)
    total_de_x = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == 'X':
                total_de_x += 1
    if total_de_x > maximo_de_x:
        print('Talvez o tesouro seja os amigos que fizemos no caminho')
    else:
        print('O one piece eh real!')
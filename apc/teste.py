N = int(input())

def ordem_nomes(N):
    chamada = []
    count = 0
    elementos = 0
    while count < N:
        nome = input()
        count += 1
        chamada.append(nome)
        elementos = 1
    chamada.sort(reverse=True)
    while elementos >= 1:
        print(f'chamada[elementos]', \n)
        elementos += 1
    


print(ordem_nomes(N))
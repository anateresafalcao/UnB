s = input()

palavras = s.split()

quantidades = {}

for palavra in palavras:
    letras = 0
    for letra in palavra:
        letras += 1
    if letras not in quantidades:
        quantidades[letras] = 1
    else:
        quantidades[letras] += 1

ordem = sorted(quantidades)

for i in ordem:
    print(f'tem {quantidades[i]} palavras de {i} letras')
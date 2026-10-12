m, n = input().split()
m = int(m)
n = int(n)
count = 0
fileira = []
sala = []

while count < m:
    fileira = input().split()
    fileira = list(map(int, fileira))
    sala.append(fileira)
    count += 1

menor_distancia = 100
distancias = []

for fileira in sala:
    for cadeira in fileira:
        if cadeira == 0:
            for proxima in fileira:
                if proxima == 1:
                    distancia = abs(cadeira-proxima)
                    menor_distancia = min(menor_distancia, distancia)
                  
    distancias.append(menor_distancia)
        
distancias.sort()
print(distancias[0])

    
            
    
    
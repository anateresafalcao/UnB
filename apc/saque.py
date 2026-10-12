
x = int(input())
    
a = x//100
b = (x-(a*100))//50
c = (x-(a*100 + b*50))//20
d = (x-(a*100 + b*50 + c*20))//10
e = (x-(a*100 + b*50 + c*20 + d*10))//2
f = (x-(a*100 + b*50 + c*20 + d*10 + e*2))//1
    
print(f'Valor do saque R$ {x}')
if a > 0:
    print(f'Entregue {a} notas de R$ 100,00')
if b > 0:
    print(f'Entregue {b} notas de R$ 50,00')
if c > 0:
    print(f'Entregue {c} notas de R$ 20,00')
if d > 0:
    print(f'Entregue {d} notas de R$ 10,00')
if e > 0:
    print(f'Entregue {e} notas de R$ 2,00')
if f > 0:
    print(f'Entregue {f} notas de R$ 1,00')
      
        



    
    
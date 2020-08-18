# Função do segundo grau com a formula de Bhaskara
import math
a = float(input("Digite o valor de A:" ))
b = float(input("Digite o valor de B:" ))
c = float(input("Digite o valor de C:" ))

if a != 0:
    d = (b**2)-4 * a * c
#print(d)

    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        print("R1 é igual a %s e r2 é igual a %s" %(r1, r2))
    else:
        print("Não existem valores reais para os numeros informados")
else:
    print("Não é uma equação do segundo grau")
        

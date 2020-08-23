"""
p = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão da PA: "))
qtde = int(input("Digite a quantidade de termos: "))

l = []
cont = 0

while (cont < qtde):
    l.append(p)
    p = p + r
    cont += 1
print("PA resultante: ", l)
"""
"""l = []
n = int(input("Digite um numero inteiro: "))
while n != 0:
    l.append(n)
    n = int(input("Digite um numero inteiro: "))
print("Lista resultante: ", l)
print("O tamanho da lista é:", len(l))
"""
import random
try:
    tamanhoLista = input("Digite o tamnho da lista: ")
except:
    print("Digite um valor valido")
i = 0
lista = []
while (i < tamanhoLista):
    numeroAleatorio = random.randint(10,50)
    lista.append(numeroAleatorio)
    i += 1

print(lista)
lista.sort()
print(lista)
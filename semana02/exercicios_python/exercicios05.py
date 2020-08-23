"""Escreva um programa que leia um string que deve conter, obrigatoriamente,
um número inteiro e, caso isso não aconteça, emita uma mensagem de erro"""
s = input("Digite um numero inteiro: ")
if s.isnumeric():
    n = int(s)
    print("O numero digitado foi {0}".format(n))
else:
    print("Digite um numero inteiro válido")

"""Faça a leitura de uma linha de dados que contenha tres números separados
por espaços em branco e carregue os objetos A, B, C com os valores individuais."""

s = input("Digite três numeros inteiros: ")
l = s.split(" ")
print("Lista L:",l)
A = int(l[0])
B = int(l[1])
C = int(l[2])
print("A = {0}, B = {1}, C = {2}".format(A,B,C))

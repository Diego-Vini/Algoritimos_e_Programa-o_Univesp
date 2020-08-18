#Calculo de média escolar

n1 = float(input("Digite a nota da primeira prova (0 a 10): "))
n2 = float(input("Digite a nota da segunda prova (0 a 10): "))
n3 = float(input("Digite a nota da terceira prova (0 a 10): "))
n4 = float(input("Digite a nota da quarta prova (0 a 10): "))


md = float(n1 + n2 + n3 + n4) / 4.0

if md >= 5:
    print("Aluno Aprovado")
    print("Media final ", md)
else:
    print("Aluno Reprovado")
    print("Média final ", md)

#Retonar média das notas utilizando estrutura de repetição while
notas = [9,7,7,10,3,9,6,6,4]
i = 0
qtdeNotas = len(notas)
somaNotas = 0
while i < qtdeNotas:
    somaNotas = somaNotas + notas[i]
    i = i + 1
media = somaNotas / i
print(media)

#Retonar média das notas utilizando estrutura de repetição for
somaNotas2 = 0
for notaAluno in notas:
    somaNotas2 = somaNotas2 + notaAluno
mediaAlunos = somaNotas2 / len(notas)
print(media)
#Exercicios de fixação Expressões e Operadores Booleanos
#A soma de 2 e 2 é menor que 4.
comparaSoma = 2 + 2 > 4
print(comparaSoma)

#O valor de 7 // 3 é igual a 1 + 1.
comparaInteiro = 7 // 3 == 1 + 1
print(comparaInteiro)

#A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
comparaQuadrado = 3**2 + 4**2 == 25
print(comparaQuadrado)

#A soma de 2, 4 e 6 é maior que 12.
comparaSoma2 = 2 + 4 + 6 > 12
print(comparaSoma2)

#1387 é divisível por 19.
comparaDivisao = 1387 % 19 == 0
print(comparaDivisao)

#31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
comparaPar = 31 % 2 == 0
print(comparaPar)

#O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*
comparaPreco = min(34.99, 29.95, 31.50 ) < 30.00
print(comparaPreco)

#(a)Atribua o valor inteiro 3 à variável a.
#(b)Atribua 4 à variável b.
#(c)Atribua à variável c o valor da expressão a * a + b * b.
a = 3
b = 4
c = a * a + b * b
print("O valor da expressão é", c)


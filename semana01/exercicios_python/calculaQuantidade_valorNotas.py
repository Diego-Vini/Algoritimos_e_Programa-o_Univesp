#calcular quantas notas de 50, 10 e 1 são necessárias para pagar uma conta
#cujo valor é fornecido.

#Variaveis e valores
v = int(input("Diegite o valor da conta a ser paga: "))

c = 50
d = 10
u = 1

#Calciulos aritiméticos
nc = v/c
rest_c = v % c

nd = rest_c / d

nu = rest_c % d

#Saida com o resultado dos calculos e impressão em tela
if nc != 0:
    print("Utilizar %d notas de 50 reais" %(nc))
if nd != 0:
    print("Utilizar %d notas de 10 reis" %(nd))
if nu != 0:
    print("Utilizar %d notas de 1 real" %(nu))

#print(int(nc), int(nd), nu)

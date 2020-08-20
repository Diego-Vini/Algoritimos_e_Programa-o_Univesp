"""Escreva um programa que calcule o faturamento de um representante comer-cial que recebe R$ 500,00 fixos e 6% de
comissão sobre as vendas do mês. Considere que ele fechou o mês com um valor de R$ 12.398,00 em vendas.
Exiba o resultado com duas casas decimais."""
vendas = float(input("Digite o valor das vendas no mês: "))
salario = 500
comissao = 6 / 100

comissaoVendas = float(vendas * comissao) + salario

print("O pagamento mais a comissão do mes é de {0:.2f}".format(comissaoVendas))

#Calculo da area de um triangulo

base = float(input("Digite o valor da base: "))
altura = float(input("Digite a altura: "))

area = (base * altura) / 2

print("A area calculada é: {0}".format(area))

"""Escreva a sequência de comandos para calcular o salário bruto de um pro-fissional que ganha por hora, sabendo que 
ele ganha R$ 14,25/h e trabalhou 163 horas normais e 20 horas extras (pagam o dobro)"""

NomeDoFuncionario = input("Digite o Nome do funcionario: ")
horasTrabalhadas = int(input("Digite a qunatidade de horas trabalhadas: "))
horaExtraTrabalhadas = int(input("Digite a quantidade de horas extras do mês: "))
valorSalarioHora = 14.25
calculoHoraExtra = 14.25 * 2

salarioReceber = horasTrabalhadas * valorSalarioHora
horaExtraReceber = horaExtraTrabalhadas * calculoHoraExtra
salarioBruto = salarioReceber + horaExtraReceber

print("O funcionário {1} receberá o valor de salario mensal de: {0}".format(salarioReceber, NomeDoFuncionario))
print("O funcionário {1} terá em hora extra para receber: {0}".format(horaExtraReceber, NomeDoFuncionario))
print("Salario bruto a receber: {0}".format(salarioBruto))
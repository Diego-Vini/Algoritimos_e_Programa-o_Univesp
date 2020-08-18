x = int(input("Digite o primeiro valor para o calculo MDC: "))
y = int(input("Digite o segundo valor para o calculo MDC: "))

while y != 0:
    r = x % y
    x = y
    y = r
print(x)

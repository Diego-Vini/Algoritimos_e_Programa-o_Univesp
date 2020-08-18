n = int(input("Informe quantidade de temperaturas que serão digitadas: "))

if n > 0:
    s = 0
    i = 1
    while i <= n :
        t = int(input("Digite o valor da temperatura: "))
        s = s + t
        i = i + 1
    m = s/n
    print("A média das temperaturas é %d" %(m))
else:
    print("Digite um valor inteiro não negativo.")


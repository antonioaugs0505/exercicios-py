valorNum = input("Digite o numero: ")
num = int(valorNum)

dezena = int(num / 10)
unidade = num % 10

if 0 < num <= 99:
    print("Dezena = ",dezena)
    print("Unidade = ",unidade)
else:
    print("Numero invalido")

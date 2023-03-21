valor = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o desconto - Ex: 20: "))
valorDescontado = valor * desconto / 100
precoNovo = valor - valorDescontado
print("O desconto é:", valorDescontado)
print("O novo preço é:", precoNovo)
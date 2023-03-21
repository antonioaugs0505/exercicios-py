metro = float(input("Digite o valor da distancia percorrida em metros: "))
segundos = float(input("Digite o tempo que essa distancia foi percorrida: "))

metroSegundo = metro/segundos
kmHora = metroSegundo * 3.6

print("Velocidade em m/s", metroSegundo)
print("Velocidade em km/h", kmHora)

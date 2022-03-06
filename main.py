def distancia(Xa, Ya, Xb, Yb):
    return ((Xb - Xa) ** 2 + (Yb - Ya) ** 2) ** 0.5

distanciaCoordenadas = []
n = int(input())

for i in range(n):
    valoresCoordenadas = str(input()).split()
    valoresCoordenadasInt = []
    for j in range(len(valoresCoordenadas)):
        valoresCoordenadasInt.append(int(valoresCoordenadas[j]))
    distanciaCoordenadas.append(distancia(valoresCoordenadasInt[0], valoresCoordenadasInt[1], valoresCoordenadasInt[2], valoresCoordenadasInt[3]))

for i in range(len(distanciaCoordenadas)):
    print("{:.2f}".format(distanciaCoordenadas[i]))
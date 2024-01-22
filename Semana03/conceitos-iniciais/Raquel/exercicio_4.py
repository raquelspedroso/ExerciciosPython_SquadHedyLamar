# 4. Receba do usuário a quantidade de litros de combustível consumidos e
# a distância percorrida. Calcule e imprima o consumo médio em km/l.

litros = int(input("Informe a quantidade de litros de combustível consumidos: "))
distancia = int(input("Informe a distancia percorrida: "))

consumo = float(distancia/litros)
print(consumo)
# 3. Faça um Programa que peça a quantidade de quilômetros, transforme
# em metros, centímetros e milímetros.

quilometros = int(input("Informe a quantidade de quilômetros que deseja converter: "))

# conveter em metros
metros = quilometros * 1000
# conveter em centímetros
centimetros = quilometros * 100000
# conveter em milímetros
milimetros = quilometros * 1000000
print(f"Transformando quilomentros em metros o resultado é {metros}.")
print(f"Transformando quilomentros em centímetros o resultado é {centimetros}.")
print(f"Transformando quilomentros em milímetros o resultado é {milimetros}.")
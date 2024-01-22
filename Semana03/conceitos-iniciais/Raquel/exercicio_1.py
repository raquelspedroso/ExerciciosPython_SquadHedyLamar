# 1. Faça um Programa que peça dois números, realize as principais
# operações soma, subtração, multiplicação, divisão

print("Digite dois números para começar o programa:")
primeiro_numero = int(input("Digite o primeiro numero: "))

segundo_numero = int(input("Digite o segundo número: "))

print(f"O primeiro número digitado foi [{primeiro_numero}], e o segundo número digitado foi [{segundo_numero}].")

# soma
somar = (primeiro_numero + segundo_numero)
print(f" Somando esses números o resultado será {somar}.")

# subtração 
diminuir = (primeiro_numero - segundo_numero)
print(f"Subitraindo esses números o resultado será {diminuir}.")

# multiplicação
multiplicar = (primeiro_numero * segundo_numero)
print(f"Multiplicando esses números o resultado será {multiplicar}.")

# divisão
dividir = (primeiro_numero / segundo_numero)
print(f"Dividindo esses números o resultado será {dividir}.")
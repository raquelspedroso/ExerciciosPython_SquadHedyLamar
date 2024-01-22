# 7. Solicite ao usuário o peso em kg e a altura em metros. Calcule e
# imprima o Índice de Massa Corporal (IMC) usando a fórmula:
# IMC = peso / (altura x altura).

peso = int(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso/(altura * altura)

if imc < 18.5:
    print(f"O seu  Índice de Massa Corporal (IMC) é: {imc:.2f}, está abaixo do peso.")
elif 18.5 <= imc <= 24.9:
    print(f"O seu  Índice de Massa Corporal (IMC) é: {imc:.2f}, seu peso é normal.")
elif 25 <= imc <= 29.9:
    print(f"O seu  Índice de Massa Corporal (IMC) é: {imc:.2f}, está com sobrepeso.")
elif 30 <= imc <= 34.9:
    print(f"O seu  Índice de Massa Corporal (IMC) é: {imc:.2f}, está com obesidade grau I.")
elif 35 <= imc <= 39.9:
    print(f"O seu  Índice de Massa Corporal (IMC) é: {imc:.2f}, está com obesidade grau II.")
else:
    print(f"O seu  Índice de Massa Corporal (IMC) é: {imc:.2f}, está com obesidade grau III (obesidade mórbida).")
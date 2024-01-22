'''
5. Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
'''

import decimal


salario_bruto = float(input("Digite o valor do salário bruto: "))

if salario_bruto <= 1903.98:
    salario_liquido = salario_bruto
    
elif salario_bruto <= 2826.65:
    salario_liquido = salario_bruto - (0.075 * salario_bruto)
elif salario_bruto <= 3751.05:
    salario_liquido = salario_bruto - (0.15 * salario_bruto)
elif salario_bruto <= 4664.68:
    salario_liquido = salario_bruto - (0.225 * salario_bruto)
else:
    salario_liquido = salario_bruto - (0.275 * salario_bruto)

print(f"Se o salário bruto é R$ {salario_bruto:.2f}, o salário líquido será R$ {salario_liquido:.2f}.")

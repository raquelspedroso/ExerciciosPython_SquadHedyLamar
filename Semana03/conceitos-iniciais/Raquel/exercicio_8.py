# 8. Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês.Calcule e mostre o total do seu
# salário no referido mês.

salario_hora = float(input("Quanto você recebe por hora trabalhada? "))
horas_trabalhadas_mes = int(input("Quantas horas você trabalha por mês? "))

salario = salario_hora * horas_trabalhadas_mes
print(f"O salário no mês será: R${salario:.2f}")
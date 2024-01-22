# 2. Peça ao usuário para informar o ano de nascimento. Em seguida,
# calcule e imprima a idade atual.
from datetime import datetime

ano_atual = datetime.now().year
ano_nascimento = int(input("Informe o seu ano de nascimento: "))

calculo = ano_atual - ano_nascimento
print(calculo)
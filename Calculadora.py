# Montar calculadora, requisitos: 
#
# - Deve realizar as operações(SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO, RADICIAÇÃO E POTENCIAÇÃO);
# - O usuário deve escolher qual operação utilizar;
# - Informar quantos números queira;
# - O programa deve exibir o resultado e perguntar ao usuário o que ele quer fazer em seguida: 
#
#   * REALIZAR UMA NOVA OPERAÇÃO USANDO O RESULTADO DA ANTERIOR (ans)
#   * REALIZAR NOVA OPERAÇÃO
#   * SAIR do programa

#Importa a biblioteca para operações matemáticas:

import math

#Exibe informações e verifica qual operação deve realizar:
print("\n CALCULADORA \n")
print("Escolha o número referente a operação matemática que deseja realizar: \n")
print("[01] - SOMA")
print("[02] - SUBTRAÇÃO")
print("[03] - MULTIPLICAÇÃO")
print("[04] - DIVISÃO")
print("[05] - RADICIAÇÃO")
print("[06] - POTENCIAÇÃO")

operation = int(input(">/ "))

#Recebe os valores: 
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))

#Cria as funções de cada operação: 
def sum(num1, num2):
    sum = num1 + num2
    print("\n %i + %i = %i"%(num1, num2, sum))

def subtration(num1, num2):
    subtration = num1 - num2
    print("\n %i - %i = %i"%(num1, num2, subtration))

def multiplication(num1, num2):
    multiplication = num1 * num2
    print("\n %i * %i = %i"%(num1, num2, multiplication))

def division(num1, num2):
    division = float(num1 / num2)
    print("\n %i / %i = %i"%(num1, num2, division))

def NthRoot(num1, num2):
    NthRoot = math.sqrt(num1)

# Verifica qual operação o usuário escolheu e a realiza: 
if operation == 1 :
    sum(num1, num2)

elif operation == 2:
    subtration(num1, num2)

elif operation == 3:
    multiplication(num1, num2)

elif operation == 4:
    division(num1, num2)

elif operation == 5:
    NthRoot(num1, num2)

elif operation == 6:
    (num1, num2)
else:
    print("O valor digitado é inválido!\nExeculte novamente inserindo valores válidos para as operações.")

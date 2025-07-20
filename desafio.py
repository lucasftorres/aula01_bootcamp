#1 Solicita ao usuario que digite seu nome
nome = input("Digite seu nome aqui: ")

#2 Solicita ao usuario que digite o valor do seu salario
# Converte o valor para float
salario = float(input("Digite o valor do seu salário: "))

#3 Solicita ao usuario que digite o valor do bonus recebido
bonus = float(input("Digite o valor do seu bônus: "))

#4 Calcule o valor do bonus final
bonus_final = (1000 + salario) * bonus

#5 Imprima o calculo de KPI do usuario
print(f"O calculo de KPI eh: ({float(1000)} + {salario}) * {bonus}")

#6 Imprima o nome do usuario e o valor do bonus final
print(f"Nome: {nome}, Bônus Final: {bonus_final:.2f}")
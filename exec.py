x = input("Digite o primeiro numero: ")
y = input("Digite o segundo numero: ")
operacao = input("Digite a operacao desejada soma, subtracao, multiplicacao, divisao: ")


if operacao == "soma":
    resultado = int(x) + int(y)
elif operacao == "subtracao":
    resultado = int(x) - int(y)
elif operacao == "multiplicacao":
    resultado = int(x) * int(y)
elif operacao == "divisao":
    resultado = int(x) / int(y)

print(f"O resultado da operacao de {operacao} entre {x} e {y} eh: {resultado}")
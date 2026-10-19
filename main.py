def ler_inteiro(mensagem):
    while True:
        entrada = input(mensagem).strip()

        if not entrada:
            print("Erro: o campo não pode ficar vazio.")
            continue

        try:
            return int(entrada)
        except ValueError:
            print("Erro: digite um número inteiro válido.")


# Entrada dos números
num1 = ler_inteiro("Digite o primeiro número: ")
num2 = ler_inteiro("Digite o segundo número: ")

# Menu de operações
print("\nEscolha uma operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operador = ler_inteiro("Digite o número da operação: ")

# Realização dos cálculos
if operador == 1:
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operador == 2:
    resultado = num1 - num2
    print("Resultado:", resultado)

elif operador == 3:
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operador == 4:
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro: não é possível dividir por zero.")

else:
    print("Erro: opção inválida. Escolha de 1 a 4.")
#Questão2 - Target Sistemas

print("-" *42)
print(" " *3, "Consulta da Sequência de Fibonacci")
print("-" *42)

lista = []
termo1 = int(0)
termo2 = int(1)
termo3 = int(0)
valor = 0

valor = int(input("Digite um número e veja se ele está contido na Sequência de Fibonacci: "))

while valor > termo3:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    lista.append(termo3)

print("Confira a lista gerada:", lista)
if valor == 0 or valor == 1:
    print("O número está contido na Sequência de Fibonacci.")
elif valor == termo3:
    print("O número está contido na Sequência de Fibonacci.")
else:
    print("O número não está contido na Sequência de Fibonacci.")


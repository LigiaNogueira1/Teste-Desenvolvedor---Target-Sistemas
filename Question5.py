#Questão5 - Target Sistemas

print("-" *42)
print(" " *6, "Exibindo palavra invertida")
print("-" *42)

string = input("Digite uma palavra para ser invertida: ")
print("A palavra, invertida, é: ")

for str in range(len(string) -1, -1, -1):
    print(string[str], end="")
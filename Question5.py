#Questão3 - Target Sistemas

string = input("Digite uma palavra para ser invertida: ")
print("A palavra, invertida, é: ")

for str in range(len(string) -1, -1, -1):
    print(string[str], end="")
#Questão5 - Target Sistemas

#Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE: 
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 
#b) Evite usar funções prontas, como, por exemplo, reverse.


print("-" *42)
print(" " *6, "Exibindo palavra invertida")
print("-" *42)

string = input("Digite uma palavra para ser invertida: ")
print("A palavra, invertida, é: ")

for str in range(len(string) -1, -1, -1):
    print(string[str], end="")
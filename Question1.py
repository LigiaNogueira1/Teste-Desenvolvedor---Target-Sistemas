#Questão1 - Target Sistemas

#Observe o trecho de código abaixo:

#int INDICE = 13, SOMA = 0, K = 0;
#enquanto K < INDICE faça {
#   K = K + 1;
#   SOMA = SOMA + K;
#}
#imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?


print("-" *42)
print(" " *10, "Calculando variável")
print("-" *42)

indice = 13
soma = 0 
k = 0

while k < indice:
    k = k + 1
    soma = soma + k

print(soma)

#Resposta da questão: ao final do processamento, o valor da variável "soma" será 91.
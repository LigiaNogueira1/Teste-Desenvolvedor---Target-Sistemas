#Questão3 - Target Sistemas

# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# •O menor valor de faturamento ocorrido em um dia do mês;
# •O maior valor de faturamento ocorrido em um dia do mês;
# •Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE: 
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; 
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média.

print("-" *42)
print(" " *7, "Consulta de Faturamento")
print("-" *42)

import json

with open("dados.json") as arquivo:
    dados = json.load(arquivo)

valores = {}
count = 0
for linha in dados:
    count += 1
    print(linha)
    for chave in linha:
        print(chave, linha[chave])
        if (chave == "valor" and linha[chave] != 0):
            valores[count] = linha[chave]
    print('--------------------------')

maior = max(valores, key=valores.get)
menor = min(valores, key=valores.get)

calc = 0
for valor in valores.values(): 
    calc += valor
calc = calc / len(valores) 

print('>>> FATURAMENTO MENSAL <<<')
print('O maior faturamento foi no dia', maior, 'com um valor de', valores[maior])
print('O menor faturamento foi no dia', menor, 'com um valor de', valores[menor])
print("A média mensal é de " + str(calc) + " e o valor de faturamento diário foi superior à ela em: "  "dias") 

arquivo.close()
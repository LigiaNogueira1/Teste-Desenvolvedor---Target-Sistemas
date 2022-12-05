#Questão4 - Target Sistemas

#Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#SP – R$67.836,43 
#RJ – R$36.678,66 
#MG – R$29.229,88
#ES – R$27.165,48 
#Outros – R$19.849,53
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.


print("-" *42)
print("Calculando o percentual de representação")
print("-" *42)

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = (sp+rj+mg+es+outros)

porcentagem_sp = ((sp*100)/total)
porcentagem_rj = ((rj*100)/total)
porcentagem_mg = ((mg*100)/total)
porcentagem_es = ((es*100)/total)
porcentagem_outros = ((outros*100)/total)

print("O percentual de representação do estado de SP é de: {:.2f}".format(porcentagem_sp), "%")

print("O percentual de representação do estado de RJ é de: {:.2f}".format(porcentagem_rj), "%")

print("O percentual de representação do estado de MG é de: {:.2f}".format(porcentagem_mg), "%")

print("O percentual de representação do estado de ES é de: {:.2f}".format(porcentagem_es), "%")

print("O percentual de representação de outros estados é de: {:.2f}".format(porcentagem_outros), "%")
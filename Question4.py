#Questão4 - Target Sistemas

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
'''
 A Locadora de Veículos Eudora lançou uma grande promoção esse mês: pagando apenas R$ 90 por diária, o cliente pode alugar um carro de passeio. 
Para cada diária, o cliente recebe uma cota de quilometragem de 100 Km. Cada quilômetro a mais custará uma taxa extra de R$ 12.
Escreva um programa que receba como entrada a quantidade de dias e a quilometragem total rodada por um cliente dessa locadora e exiba o valor total a ser pago com duas casas decimais.
'''

dias = float(input("Informe a quantidade de dias: "))
quilometragem = float(input("Informe a quilometragem: "))

diaria = dias*90

if quilometragem > 100:
    quilometragem = (quilometragem-100)*12
else:
    quilometragem = 0

total = quilometragem+diaria

print("O valor total devido é de: ", total)
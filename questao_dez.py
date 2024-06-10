"""
10) Joãozinho investiu R$1000,00 na sua conta do Banco Iradoso por um ano. Sabendo que seu investimento rende 0.02% por dia útil, qual o montante que Joãozinho terá após 7 semanas de investimento?
"""
investimento = 1000
rendimento = 0.0002
dias_uteis_semana = 5
semanas = 7

dias = dias_uteis_semana*semanas

dias_totais = 0

while dias_totais < dias:
    dias_totais += 1

juros = dias_totais*rendimento
resultado = investimento*juros
print(investimento+resultado)
"""
17) Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve
perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação
mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a
comprar dividido pelo número de meses a pagar.
"""

valor_da_casa = float(input("informe o valor do imóvel: "))
salario = float(input("Qual sua renda mensal? "))
anos_pgto = float(input("Em quantos anos deseja pagar o financiamento? "))

limite_valor_sl = salario*0.3
meses_pgto = anos_pgto*12

periodicidade = valor_da_casa / meses_pgto

if periodicidade <= limite_valor_sl:
    print(f"Você pagará {periodicidade} por mês durante {anos_pgto} anos.")
else:
    print("Sua renda não é compatível com o valor do imóvel. Tente aumentar o período de financiamento.")



"""
13) banco de dados de números inteiros. 
Você decide salvar cada valor numa variável e percebe que, em algum momento do código, você precisa trocar os valores de duas variáveis ( e ) entre si. 
Faça um programa que realize essa troca de valores entre duas variáveis.
"""

#numeros inteiros
#trocar o valor ENTRE duas variaveis

valor1 = input("Digite o primeiro valor: ")
valor2 = input("Digite o segundo valor: ")

print(f"valor 1 = {valor1}, valor 2 = {valor2}")
valor1, valor2 = valor2, valor1

print(f"valor 1 = {valor1}, valor 2 = {valor2}")



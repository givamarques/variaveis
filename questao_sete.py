"""
7) todo número ímpar é a diferença de dois quadrados consecutivos.

1 - 0 = 1
4 - 1 = 3
9 - 4 = 5
16 - 9 = 7
25 - 16 = 9

fazer um programa que escreva um número ímpar como a diferença de dois quadrados.
"""

#mais**2 - menos**2 == numero

numero = int(input("Digite um número ímpar: "))
mais = (numero+1)//2
menos = (numero-1)//2


if numero % 2 == 0:
    print("O número é par. Digite um númeor impar")
else:
    print(numero, f"{mais}^2", f"{menos}^2")
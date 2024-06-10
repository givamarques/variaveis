"""
18) Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa
verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o
número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1
não são primos e que 2 é o único número primo que é par
"""

numero = int(input("Informe um número ímpar:"))

if numero %2 == 0:
    print("O número deve ser ímpar")
else:
    x = 3
    while x < numero:
        if numero % x == 0:
            break
        x += 2
    if x == numero:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")

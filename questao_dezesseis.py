"""
16) Escreva um programa que leia três números e que imprima o maior e o menor.
"""

menor_numero = int(input('Primeiro numero: '))
segundo_numero  = int(input('Segundo numero : '))
terceiro_numero = int(input('Terceiro numero: '))

maior = menor_numero

if (segundo_numero > maior):
    maior = segundo_numero
if (terceiro_numero > maior):
    maior = terceiro_numero

print('Maior: ',maior)

menor = menor_numero

if (segundo_numero < menor):
    menor = segundo_numero
if (terceiro_numero < menor):
    menor = terceiro_numero

print('Menor: ',menor)
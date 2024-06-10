"""
15) Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa
conversão é:
     9 × C
 F = ----- + 32
       5
"""

c = int(input("Digite a temperatura em Celsius: "))

f = ((9 * c) / 5) + 32

print(f)
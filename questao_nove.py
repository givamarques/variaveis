"""
9) Na física, um problema clássico de cinemática é encontrar a posição de um corpo ao longo do processo de queda acelerada por meio da gravidade.
Faça um programa que calcula a altura H que um corpo cai sob ação da gravidade (g=9.8m/s^2) durante 7.5 segundos, sabendo que ele tem uma velocidade inicial v0 = 0.75m/s^2, vertical para baixo.
"""

g = 9.8
t = 7.5
v0 = 0.75

linear = v0 * t
quadratico = 0.5 * g * t**2
altura = linear + quadratico

print(altura)



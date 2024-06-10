#Faça programa que recebe um tempo dado em segundos e calcula quantos dias, horas, minutos e segundos ele representa.
segundos = int(input("Digite os segundos"))
minutos = (segundos/60)
horas = (minutos/60)
dias = (horas/24)

print("Você digitou o equivalente a ", dias, " dias, ", horas, " horas, ", minutos, " minutos e ", segundos, " segundos.")
'''
Faça um programa que leia um valor de mercadorias que um turista está trazendo de volta e calcula quanto ele terá que pagar de imposto na alfândega.
A regra de imposto é:
Até 500 de valor: sem imposto
Acima de 500: 50% sobre o excedente 
'''

valor = float(input("Digite o valor das mercadorias: "))

if valor >= 500:
    valor=valor*1.5

print(valor)
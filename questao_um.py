'''
1) Escreva um programa que recebe 3 notas de prova e calcula:
- A média delas
- A média ponderada delas, considerando pesos 2, 2 e 3
- A média ponderada delas, considerando pesos 1, 2 e 2
'''

nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
nota_tres = float(input("Digite a terceira nota: "))

media = ((nota_um+nota_dois+nota_tres)/3)
media_ponderada_um = (((nota_um*2)+(nota_dois*2)+(nota_tres*3))/7)
media_ponderada_dois = (((nota_um)+(nota_dois*2)+(nota_tres*2))/5)

print("A média foi ", media)
print("A média ponderada UM foi ", media_ponderada_um)
print("A média ponderada DOIS foi ", media_ponderada_dois)
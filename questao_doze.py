"""
12) Classifique o itens abaixo como nome de variável válido ou inválido.

teclado_lidinho
Germa66
1º_lugar
PlayerID
class

Exiba "valido" ou "invalido no terminal"
"""

def validar_variaveis(lista):
    for variavel in lista:
        if not variavel[0].isupper() and not variavel[0].isdigit():
            print(f"A variavel '{variavel}' é válida.")
        else:
            print(f"A variavel '{variavel}' é inválida.")

lista_variaveis = ["teclado_lidinho", "Germa66", "1º_lugar", "PlayerID", "class"]
validar_variaveis(lista_variaveis)

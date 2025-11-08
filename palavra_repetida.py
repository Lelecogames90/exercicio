# Código que recebe uma frase em um campo de entrada
# Mostra a quantidade de vezes cada palavra se repetiu na frase
# Código limpo
from collections import Counter

def contar_palavras(frase):
    palavras = frase.split()
    contagem = Counter(palavras)
    return contagem

frase = input("Digite uma frase: ")
resultado = contar_palavras(frase)
for palavra, quantidade in resultado.items():
    if quantidade > 1:
        print(f"A palavra '{palavra}' apareceu {quantidade} vezes.")
    else:
        print(f"A palavra '{palavra}' apareceu {quantidade} vez.")
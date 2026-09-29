import random
import sys
palavras = [
    "casa",
    "carro",
    "computador",
    "programação",
    "python",
    "escola",
    "faculdade",
    "trabalho",
    "livro",
    "internet"
]

palavra = random.choice(palavras)
letra_acertada = ''

while True:
    letra_digitada = input("Digite uma letra: ").lower()

    if letra_digitada == "exit":
        print("Saindo do jogo...")
        sys.exit()

    if letra_digitada in palavra:
        letra_acertada += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    if len(letra_digitada) > 1:
            print("Digite apenas uma letra.")
            continue
    
    print(palavra_formada)

    if palavra_formada == palavra:
        print("Parabéns! Você acertou a palavra!")
        break


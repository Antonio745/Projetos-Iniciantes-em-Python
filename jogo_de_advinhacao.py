import random

nome = input("Qual é o seu nome? ")

print("Boa sorte!", nome)

palavras = ['arco-íris', 'computador', 'ciência', 'programação',
            'python', 'matemática', 'jogador', 'condição',
            'inverter', 'água', 'tabuleiro', 'nuvem']

palavra = random.choice(palavras)

print("Adivinhe as letras")

chutes = ''
tentativas = 10

while tentativas > 0:
    falhas = 0

    for letra in palavra:

        if letra in chutes:
            print(letra, end=" ")

        else:
            print("_")
            falhas += 1

    if falhas == 0:
        print("Você Ganhou")
        print("A palavra é:", palavra)
        break

    print()
    chute = input("Digite uma letra:")

    chutes += chute

    if chute not in palavra:

        tentativas -= 1
        print("Errado")
        print("Você tem", + tentativas, 'tentativas restantes')

        if tentativas == 0:
            print("Você Perdeu")

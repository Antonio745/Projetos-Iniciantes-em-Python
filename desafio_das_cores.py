import random

# Lista de cores
cores = ["vermelho", "azul", "verde", "amarelo", "preto"]

# Seleciona uma cor secreta aleatória
cor_secreta = random.choice(cores)

# Loop para as tentativas
while True:
    # Solicita uma tentativa do usuário
    tentativa = input("Adivinhe a cor secreta (vermelho, azul, verde, amarelo, preto): ").strip().lower()

    # Verifica se o usuário acertou
    if tentativa == cor_secreta:
        print("Parabéns! Você adivinhou a cor secreta!")
        break
    else:
        print("Cor incorreta!")

    # Pergunta se o usuário quer tentar novamente
    resposta = input("Deseja tentar novamente? (sim/não): ").strip().lower()
    if resposta == "não":
        print("Tudo bem! A cor secreta era", cor_secreta)
        break

# Mensagem final
print("Obrigado por jogar!")

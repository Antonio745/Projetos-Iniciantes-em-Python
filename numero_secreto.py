numero_secreto = 8
while True:
    tentativa = int(input("Advinhe um numero entre 1 e 10 :"))
    if tentativa == numero_secreto:
        print("Parabens você acertou")
        break
    elif tentativa < numero_secreto:
        print("O numero é maior")
    else:
        print("O numero é menor")
    resposta = input("Deseja tentar novamente ? sim/nao :" .strip().lower())
    if resposta == ("nao"):
        print(f"Tudo bem o numero secreto era {numero_secreto}")
        break
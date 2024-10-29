import math
import random

def main():
    lower = int(input("Digite o limite inferior: "))
    upper = int(input("Digite o limite superior: "))

    # Gerando um número aleatório entre o limite inferior e superior
    x = random.randint(lower, upper)
    total_chances = math.ceil(math.log2(upper - lower + 1))

    print(f"\n\tVocê tem apenas {total_chances} chances para adivinhar o número inteiro!\n")

    count = 0
    flag = 0

    # Para cálculo do número mínimo de tentativas
    while count < total_chances:
        count += 1

        # Tomando o número de tentativa como entrada
        guess = int(input("Chute um numero: "))

        # Testando as condições
        if x == guess:
            print(f"Parabéns, você conseguiu em {count} tentativas!")
            flag = 1
            break
        elif x > guess:
            print("É um numero maior!")
        elif x < guess:
            print("É um numero menor!")

    # Se as tentativas forem mais do que as necessárias
    if not flag:
        print(f"\nO número é {x}\n\tMelhor sorte na próxima vez!")

if __name__ == "__main__":
    main()

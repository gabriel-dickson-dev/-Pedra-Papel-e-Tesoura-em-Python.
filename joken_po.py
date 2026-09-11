import random

opcoes = ["pedra", "papel", "tesoura"]

print("Opções: pedra, papel ou tesoura\n")

jogador = input("Sua vez: ").lower().strip()

# Checa se o usuário digitou algo certo
if jogador not in opcoes:
    print("\nOps, você digitou algo errado! Tem que ser pedra, papel ou tesoura.")
else:
    # O computador faz a escolha dele
    computador = random.choice(opcoes)

    print(f"Eu escolhi: {computador}")

    if jogador == computador:
        print("\nNossa, deu empate!")
    elif (
        (jogador == "pedra" and computador == "tesoura")
        or (jogador == "papel" and computador == "pedra")
        or (jogador == "tesoura" and computador == "papel")
    ):
        print("\nMandou bem! \nVocê venceu essa.")
    else:
        print("\nGanhei de você dessa vez!")

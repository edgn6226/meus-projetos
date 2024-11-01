import random

def escolher_palavra():
    palavras = ['trota', 'programar', 'pai', 'gente ', 'luta']
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    exibir = ""
    for letra in palavra:
        if letra in letras_corretas:
            exibir += letra + " "
        else: 
            exibir += "_ "
    return exibir.strip()  # Retorno deve estar fora do loop

palavra_secreta = escolher_palavra()
letras_corretas = []
letras_erradas = []
tentativas = 6

print("Vamos jogar forca!")

while tentativas > 0:
    print(f"\nPalavra: {exibir_palavra(palavra_secreta, letras_corretas)}")
    print(f"Tentativas restantes: {tentativas}")
    print(f"Letras erradas: {', '.join(letras_erradas)}")
    palpite = input("Qual seu chute: ").lower()  # Convertendo para minúsculas

    if palpite in letras_corretas or palpite in letras_erradas:
        print("Você já tentou essa letra antes. Tente outra.")
        continue  # Volta ao início do loop 'while'

    if palpite in palavra_secreta:
        letras_corretas.append(palpite)
        print(f"Boa! A letra '{palpite}' está na palavra.")
    else:
        letras_erradas.append(palpite)
        tentativas -= 1
        print(f"A letra '{palpite}' não está na palavra.")

    # Verifica se todas as letras foram descobertas
    if set(letras_corretas) == set(palavra_secreta):
        print(f"\nParabéns! Você descobriu a palavra: {palavra_secreta}")
        break
else:
    print(f"\nFim do jogo")

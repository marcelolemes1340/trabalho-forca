import random

def print_menu():
    print("=================================")
    print("   BEM VINDO AO JOGO DA FORCA    ")
    print("=================================")
    print("1. Iniciar Jogo")
    print("2. Instruções")
    print("3. Créditos")
    print("4. Sair")
    print("=================================")

def iniciar_jogo():
    palavras = ['madrid', 'milan', 'psg', 'roma', 'juventus', 'barcelona', 'manchester', 'chelsea', 'Arsenal ', 'borussia']
    palavra = random.choice(palavras)
    tentativas = 6
    letras_adivinhadas = []

    print("Iniciando o jogo da Forca")
    
    while tentativas > 0:
        display_palavra = ""
        for letra in palavra:
            if letra in letras_adivinhadas:
                display_palavra += letra
            else:
                display_palavra += " _ "
        
        print("\nPalavra:", display_palavra)
        print("Tentativas restantes:", tentativas)
        
        if "_" not in display_palavra:
            print("Parabéns! Você adivinhou a palavra:", palavra)
            break
        
        chute = input("Adivinhe uma letra: ").lower()
        
        if chute in letras_adivinhadas:
            print("Você já adivinhou essa letra. Tente outra.")
        elif chute in palavra:
            letras_adivinhadas.append(chute)
            print("Boa! A letra", chute, "está na palavra.")
        else:
            tentativas -= 1
            print("Que pena! A letra", chute, "não está na palavra.")
    
    if tentativas == 0:
        print("Fim de jogo! Você não adivinhou a palavra:", palavra)

def mostrar_instrucoes():
    print("Instruções do Jogo:")
    print("1. O objetivo do jogo é adivinhar a palavra secreta.")
    print("2. Você tem um número limitado de tentativas.")
    print("3. A cada tentativa, você pode adivinhar uma letra.")
    print("4. Se a letra estiver na palavra, ela será revelada.")
    print("5. Se a letra não estiver na palavra, você perde uma tentativa.")
    print("6. O jogo termina quando você adivinha a palavra ou perde todas as tentativas.")

def mostrar_creditos():
    print("Créditos:")
    print("Desenvolvedor: Vitor e Marcelo")
    print("Agradecimentos: Edécio")

def sair():
    print("Saindo do jogo.")

def menu():
    while True:
        print_menu()
        escolha = input("Selecione uma opção (1-4): ")

        if escolha == '1':
            iniciar_jogo()
        elif escolha == '2':
            mostrar_instrucoes()
        elif escolha == '3':
            mostrar_creditos()
        elif escolha == '4':
            sair()
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()

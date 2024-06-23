
#? Estrutura do jogo;

print("Começando o Jogo!")

palavra = input('Digite uma palavra sercreta: ').lower().strip() # Dois métodos um para se o usuário digitar palavras maiúsculas e ficar
# minúsculas, e a outra caso dê espaço ele eliminar os espaços;

for x in range(50):
    print()

palavras_digitadas = []
acertos            = []
erros              = 0

while True:
    #todo) IMPRIMIR A PALAVRA SECRETA;
    adivinha = ""
    for letra in palavra:
        if letra in acertos:
            adivinha += letra
        else: 
            adivinha += "\u2588"
    print(f'ADIVINHE ({len(palavra)} letras): ')
    for letra in adivinha:
        print(f'{letra} ', end='')
    
    
    #todo) CONDIÇÃO DA VITÓRIA;
    if adivinha == palavra:
        print("\n"f'Você Ganhou! A palavra foi: {palavra} ')
        break
    
    #todo) TENTATIVAS;

    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in palavras_digitadas:
        print("Você já usou esta letra!")
        continue
    else:
        palavras_digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    
    #todo) DESENHO DA FORCA;
    print("X==:==")
    print("X  :  ")
    if erros >= 1:
        print('X  O  ')
    else:
        print('X')
    
    linha2 = ""
    if erros == 2:
        linha2 = "  | "
    elif erros == 3:
        linha2 = " /| "
    elif erros >= 4:
        linha2 = " /|\ "
    print(f"X{linha2}")
    

    linha3 = ""
    if erros == 5:
        linha3 += " / "
    elif erros >= 6:
        linha3 += " / \ "
    print(f"X{linha3}")
    
    print(f"X\n=======")

    #todo) CONDIÇÃO DE VITÓRIA;
    if erros == 6:
        print("Você perdeu, Enforcado!")
        print(f"A palavra correta é: {palavra}")
        break
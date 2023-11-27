import random
import time

def hangman_game():
    print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

""")
    nome_jogador = input("Qual o seu nome? ")
    print(f"Seja bem vindo, {nome_jogador.title()}")
    
    lista_de_palavras = [
    'antropocentrismo',
    'otorrinolaringologista',
    'esternocleidomastoideo',
    'inconstitucionalissimamente',
    'ascensorista',
    'anticonstitucionalmente',
    'interdisciplinaridade',
    'idiossincrasia',
    'impeachment',
    'incompreensibilidade',
    'excesso',
    'conspurcar',
    'capcioso',
    'consenso',
    'caatinga',
    'irrequieto',
    'aquiescer',
    'cinquenta',
    'delinquente',
    'bicarbonato', 
    ]

    palavra_secreta = list(random.choice(lista_de_palavras))

    print("Escolhendo uma palavra no nosso banco de dados...")
    time.sleep(2)
    
    palavra_suprimida = ['_' for i in palavra_secreta]
    
    print(palavra_suprimida)
    letras_ausentes = []
    
    tentativas = 3
    
    while tentativas >= 0:
        chute = input("Digite uma letra: ").lower()

        if chute in palavra_secreta:
            chute_indice = 0
            
            for letra in palavra_secreta:
                if letra == chute:
                    palavra_suprimida[chute_indice] = letra
                chute_indice += 1
            
            if palavra_secreta == palavra_suprimida:
                print(f"Parabéns, {nome_jogador.title()}! Você ganhou!")
                print("A palavra secreta é:")
                for letra in palavra_suprimida:
                    print(letra, end='')
                break;


            print(palavra_suprimida)

        else:
            print('Letra não encontrada.')
            letras_ausentes.append(chute)
            tentativas -= 1
            print(letras_ausentes)
            print(f"Chances: {tentativas}")
            if tentativas == 0:
                print(f"Você perdeu, {nome_jogador.title()}!")
                break;



hangman_game()

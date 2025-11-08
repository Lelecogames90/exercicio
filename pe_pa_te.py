# Código que gere uma partida de Pedra, Papel ou Tesoura

import random 
print('===============================')
print('      Pedra Papel Tesoura      ')
print('===============================\n')
while True:
    bot = random.choice(['Pedra', 'Papel', 'Tesoura'])
    jogador = input('Escolha entre Pedra, Papel ou Tesoura: ')
    if jogador.lower() not in ['pedra', 'papel', 'tesoura']:
        print('Escolha inválida! Tente novamente.\n')
    else:
        print(f'O computador escolheu: {bot.lower()}')
        if jogador.lower() == bot.lower():
            print('Empate!')
        elif (jogador.lower() == 'pedra' and bot.lower() == 'tesoura') or (jogador.lower() == 'papel' and bot.lower() == 'pedra') or (jogador.lower() == 'tesoura' and bot.lower() == 'papel'):
            print(f'Você ganhou pois {jogador.lower()} vence {bot.lower()}!')
        else:
            print(f'Você perdeu pois {bot.lower()} vence {jogador.lower()}!')
    print('Deseja jogar novamente?\n1 - Sim\n2 - Não')
    jogar_novamente = input('Resposta: ')
    print('')
    if jogar_novamente == '2':
        break
    else:
        continue
import random
print(' ')
print('\033[1;34mVocê é um mero andarilho, desbravando as terras de Py em busca de novas aventuras e conhecimentos, carregando consigo somente uma poção de cura e uma espada enferrujada e cansada de tantas batalhas, de repente você avista o espírito da preguiça e procrastinação, determinado a derrotá-lo para continuar sua incansável busca, você saca sua arma e parte para o ataque!\033[m')

player = 50
monstro = 50
pot = 5

print('\033[33m_\033[m'* 18 )
print(f'Seu HP:\033[1;32m{player}\033[m')
print(f'HP do monstro:\033[1;32m{monstro}\033[m')
print('\033[33m_\033[m'* 18 )

while player > 0 and monstro > 0:
    input('\033[1;35m Digite atq para desferir um golpe:\033[m')
    danom = random.randrange(1,13)
    monstro = monstro - danom
    if danom <= 4:
        print(f'\033[1;36mVocê\033[m branda rapidamente a espada mas o monstro consegue se esquivar, causando um leve corte e \033[1;31m{danom}\033[m de dano!')
    elif danom < 8 and danom >= 5:
        print(f'\033[1;36mVocê\033[m acerta de cheio e causa \033[1;31m{danom}\033[m de dano!')
    else:
        print(f'\033[1;36mVocê\033[m golpeia com tamanha força e agilidade que o monstro não tem a menor chance de se defender, causando \033[1;31m{danom}\033[m de dano!')
    danop = random.randrange(1,13)
    player = player - danop
    if danop <= 4:
        print(f'O \033[1;36mmonstro\033[m tenta rasgá-lo com suas garras, mas você se esquiva recebendo somente \033[1;31m{danop}\033[m de dano!')
    elif danop < 8 and danop >= 5:
        print(f'Sem chances para defesa, o \033[1;36mmonstro\033[m causa \033[1;31m{danop}\033[m de dano em você!')
    else:
        print(f'Com toda a sua força, o \033[1;36mmonstro\033[m quebra a sua defesa e desfere \033[1;31m{danop}\033[m de dano em você!')
    print('\033[33m_\033[m'* 18 )
    print(f'Seu HP:\033[1;32m{player}\033[m')
    print(f'HP do monstro:\033[1;32m{monstro}\033[m')
    print('\033[33m_\033[m'* 18 )
    if monstro <= 0 and player > 0:
        print('\033[34mSubjulgado pela sua lâmina, o monstro cai ao chão e você terá mais um dia de conquistas e aprendizados no Reino de PY!\033[m')
    elif player <= 0 and monstro >0:
        print('\033[31mvocê teve determinação, mas o monstro da preguiça e procrastinação foi mais forte, mas não desista, sempre há outro dia!\033[m')
    elif player <= 0 and monstro <= 0:
        print('\033[33mVocê e o monstro desferem um último golpe simultâneo fazendo com que ambos caiam no chão derrotados!\033[m')
    if player <= 20 and player > 0 and pot == 5 and monstro > 0:
        print('\033[1;30;41m Atenção, seu HP está baixo,deseja usar poção de cura?\033[m')
        r = str(input('Sim ou Não?')).upper().strip()
        if r == 'SIM':
            print(f'\033[1;32mVocê usa a poção de cura e regenera {pot} de HP!\033[m')
            player = player + pot
            pot = 0
            print(f'Seu HP: \033[1;32m{player}\033[m')
        if r != 'SIM':
            pot= 0
    if monstro == 1 and player > 0:
        monstro = monstro + 5
        print('\033[1;31mA um fio da morte, o monstro usa sua magia de cura e recebe +5 de HP\033[m')
        print(f'HP do monstro:\033[1;32m{monstro}\033[m')
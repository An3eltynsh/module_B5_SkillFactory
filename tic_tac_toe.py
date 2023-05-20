
from random import randint

def greet():
    print('-------------------------')
    print('          ИГРА           ')
    print('     КРЕСТИКИ-НОЛИКИ     ')
    print('_________________________')
    print('     формат ввода: x y   ')
    print('     x - номер строки    ')
    print('     y - номер столбца   ')
    print('-------------------------')
    print(' (Вы - Х, компьютер - О) ')
    print('_________________________')

greet()
play_field = [[' ' for i in range(3)] for j in range(3)]

#------------Ввод игрового поля--------------------
def show_playing_field(field):
    print('   | 0 | 1 | 2 | ')
    print(' --------------- ')
    for i, item in enumerate(field):
        item_print = f' {i} | {" | ".join(item)} |'
        print(item_print)
        print(' --------------- ')


#------------Ход игрока----------------------------
def move_player():

    while True:
        move = input('      Ваш ход: ').split()
        if len(move) != 2:
            print('Ввод неверный, введите две координаты!')
            continue

        x, y = move

        if not(x.isdigit()) or not(y.isdigit()):
            print('Ввод неверный, введите числа!')
            continue

        x, y = int(x), int(y)

        if 0 > x > 2 or 0 > y > 2:
            print('Ввод неверный, координаты вне диапазона!')
            continue

        if play_field[x][y] != ' ':
            print('Клетка занята!')
            continue

        return x, y


#------------Ход компьютера-----------------------
def move_computer():

    symb = []

    for i in range(3):
        symb = []
        for j in range(3):
            symb.append(play_field[i][j])
        condition = [symb.count('X') == 2, symb.count('O') == 2]
        if any(condition) and ' ' in symb:
            z = i
            p = symb.index(' ')
            return z, p

    for j in range(3):
        symb = []
        for i in range(3):
            symb.append(play_field[i][j])
        condition = [symb.count('X') == 2, symb.count('O') == 2]
        if any(condition) and ' ' in symb:
            z = symb.index(' ')
            p = j
            return z, p

    symb = []
    for i in range(3):
        symb.append(play_field[i][i])
    condition = [symb.count('X') == 2, symb.count('O') == 2]
    if any(condition) and ' ' in symb:
        z, p = symb.index(' '), symb.index(' ')
        if(play_field[z][p] == ' '): return z, p

    symb = []
    for i in range(3):
        symb.append(play_field[i][2-i])
    condition = [symb.count('X') == 2, symb.count('O') == 2]
    if any(condition) and ' ' in symb:
        z = symb.index(' ')
        p = 2-z
        if(play_field[z][p] == ' '): return z, p

    while True:
        z, p = randint(0, 2), randint(0, 2)
        if play_field[z][p] == ' ': return z, p

#------------Проверка выигрыша-----------------------
def check_winner():

    symb = []

    for i in range(3):
        symb = []
        for j in range(3):
            symb.append(play_field[i][j])
        condition = [symb == ['X', 'X', 'X'], symb == ['O', 'O', 'O']]
        if any(condition): return symb[0]

    for j in range(3):
        symb = []
        for i in range(3):
            symb.append(play_field[i][j])
        condition = [symb == ['X', 'X', 'X'], symb == ['O', 'O', 'O']]
        if any(condition): return symb[0]

    symb = []
    for i in range(3):
        symb.append(play_field[i][i])
    condition = [symb == ['X', 'X', 'X'], symb == ['O', 'O', 'O']]
    if any(condition): return symb[0]

    symb = []
    for i in range(3):
        symb.append(play_field[i][2-i])
    condition = [symb == ['X', 'X', 'X'], symb == ['O', 'O', 'O']]
    if any(condition): return symb[0]

    return ' '

#----------------------------------------------------

show_playing_field(play_field)

count_move = 0

while True:
    
    count_move += 1

    if count_move == 9:
        print('Ничья!')
        break

    if count_move % 2 != 0:
        print('Ходит Х ')
        x, y = move_player()
        play_field[x][y] = 'X'
        show_playing_field(play_field)
        if check_winner() == 'X':
            print('Вы выиграли!!!')
            print('Конец игры!')
            break
        continue

    if count_move % 2 == 0:
        print('Ходит О ')
        z, p = move_computer()
        play_field[z][p] = 'O'
        show_playing_field(play_field)
        if check_winner() == 'O':
            print('Вы проиграли!')
            print('Компьютер: Хо - хо - хо !')
            print('Конец игры!')
            break
        continue

#----------------------------------------------------






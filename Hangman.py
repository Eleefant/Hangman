from random import choice

#Список необходимых функций
#1. Выбор слова из файла (есть)
#2. Обработчик начала игры (есть)
#3. Обработчик вводимых букв и отображение загаданного слова
#4. Функция печати виселецы (есть)
#5. Добавить кудато чтобы по окончании игры происходило предложение сыграть ещё (есть)
#6. Функция собирающая все воедино
#! Добавить исключение повторно введенных букв, добавить отображение букв на их местах в слове, после каждого введения
# Повторно вводимый символ отсутствующий в слове не должнен считаться за ошибку (есть)

def select_word():
    with open("words.txt", "r", encoding='utf-8') as words:
        word_list = words.readlines()
        new_word = choice(word_list).strip()
    return new_word

select_word1 = select_word()
#y = [select_word1]
#print(y)
print(select_word1)

def open_word():
    

def start_game():
    print('Привет, давай сыграем в одну игру. Отгдай слово или умри!. Боишся? - уходи.')
    vibor = input('Введи "да" если начинаем или "нет" если уходишь ').lower()
    count_start = 0
    while count_start < 1:
        if vibor == 'да':
            print(select_word1)
            search_letter()
            count_start += 1
        elif vibor == 'нет':
            print('Пока')
            break
        else:
            print('Введите корректное значение для продолжения')
            vibor = input('Введи "да" если начинаем или "нет" если уходишь ').lower()
    return count_start

def draw_hanged_man(): #(wrong_guesses):
    hanged_man = [r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]
    return hanged_man
drow_hm = draw_hanged_man()

list_wrong_letter = set()
list_correct_letter = []

def search_letter():
    count_letter = 0
    index_drow_hm = 0
    while count_letter < 6:
        unkown_word = select_word1.replace(select_word1, 'X')
        print(drow_hm[index_drow_hm])
        print('Загадонное слово', unkown_word * len(select_word1))
        letter = input('Введи букву на русском: ').lower()
        if letter in list_wrong_letter:
            print('Эта буква неправильная и ты ее уже вводил')
            print('Список неправильных букв', list_wrong_letter)
        elif len(letter) > 1:
            print('Только одну букву')
        elif letter in 'abcdefghijklmnopqrstuvwxyz1234567890':
            print('Я же сказал на РУССКОМ!')
        elif letter not in select_word1:
            list_wrong_letter.add(letter)
            count_letter += 1
            index_drow_hm += 1
            print(list_wrong_letter)
            print('Неверно! Количество ошибок', count_letter, 'из 6')
            print('Список неправильных букв', list_wrong_letter)
            #print('Загадонное слово', unkown_word * len(select_word1))
        #elif count_letter == 6:
        #    print('Количество попыток исчерпано, ты повешен')
        #    break
        elif letter in select_word1:
            list_correct_letter.append(letter)
            print(list_correct_letter)
            print('Верно! Количество ошибок', count_letter, 'из 6')
            print('Загаданное слово', unkown_word * len(select_word1))
    else:
        print(drow_hm[6], 'Покойся с миром')
        select_word()
        print(select_word1)
        start_game()
    return count_letter



#select_word()
start_game()

#def igra():
#    start_game()
    #return igra()
#igra()
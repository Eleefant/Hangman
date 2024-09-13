from random import choice

def select_word():
    with open("words.txt", "r", encoding='utf-8') as words:
        word_list = words.readlines()
        new_word = choice(word_list).strip()
    return new_word

def start_game():
    print('Привет, давай сыграем в одну игру. Отгдай слово или умри!. Боишся? - уходи.')
    vibor = input('Введи "да" если начинаем или "нет" если уходишь ').lower()
    count_start = 0
    while count_start < 1:
        if vibor == 'да':
            search_letter()
            count_start += 1
        elif vibor == 'нет':
            print('Пока')
            break
        else:
            print('Введите корректное значение для продолжения')
            vibor = input('Введи "да" если начинаем или "нет" если уходишь ').lower()

def draw_hanged_man():
    hanged_man = [r"""
  -----
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
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
  |   |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 /|   |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 /|\  |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 /|\  |
 /    |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 /|\  |
 / \  |
      |
-------
""",
    ]
    return hanged_man
draw_hm = draw_hanged_man()

set_wrong_letter = set()

def search_letter():
    count_letter = 0
    index_drow_hm = 0
    select_word1 = select_word()
    select_word2 = list(select_word1)
    unkown_word = list('_' * len(select_word1))
    while count_letter < 6:
        unkown_word2 = []
        print(draw_hm[index_drow_hm])
        print('Загаданное слово', ''.join(unkown_word))
        letter = input('Введи букву на русском: ').lower()
        if letter in set_wrong_letter:
            print('Эта буква неправильная и ты ее уже вводил')
            print('Список неправильных букв', set_wrong_letter)
        elif len(letter) > 1:
            print('Только одну букву')
        elif letter in 'abcdefghijklmnopqrstuvwxyz1234567890':
            print('На русском, пожалуйста')
        elif letter not in select_word2:
            set_wrong_letter.add(letter)
            count_letter += 1
            index_drow_hm += 1
            print('Неверно! Количество ошибок', count_letter, 'из 6')
            print('Список неправильных букв', set_wrong_letter)
        elif letter in select_word2:
            for i in range(len(select_word2)):
                if letter == select_word2[i]:
                    unkown_word2 += letter
                else:
                    unkown_word2 += unkown_word[i]
            unkown_word = unkown_word2
            print('Верно! Количество ошибок', count_letter, 'из 6')
            print('Загаданное слово:', ''.join(unkown_word))
            print('Список неправильных букв', set_wrong_letter)
            if select_word2 == unkown_word:
                print('Поздравляю с победой!')
                print('Ты угадал слово:', ''.join(select_word2))
                select_word()
                start_game()
    else:
        print(draw_hm[6], 'Покойся с миром')
        print('Загаданное слово:', ''.join(select_word2))
        select_word()
        start_game()

start_game()
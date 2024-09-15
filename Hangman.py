from random import choice


def select_word():
    with open("words.txt", "r", encoding='utf-8') as words:
        word_list = words.readlines()
        new_word = choice(word_list).strip()
    return new_word


def start_game():
    print('Привет, давай сыграем в одну игру. Отгдай слово или умри!. Боишся? - уходи.')
    choice = input('Введи "да" если начинаем или "нет" если уходишь ').lower()
    count_start = 0
    while count_start < 1:
        if choice == 'да':
            search_letter()
            count_start += 1
        elif choice == 'нет':
            print('Пока')
            break
        else:
            print('Введите корректное значение для продолжения')
            choice = input('Введи "да" если начинаем или "нет" если уходишь ').lower()


def draw_hanged_man(error_number):
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
    return hanged_man[error_number]


def search_letter():
    set_use_letter = set()
    count_errors = 0
    error_number = 0
    secret_word = select_word()
    select_word2 = list(secret_word)
    unkown_word = list('_' * len(secret_word))
    while count_errors < 6:
        unkown_word2 = []
        print(draw_hanged_man(error_number))
        print('Загаданное слово', ''.join(unkown_word))
        letter = input('Введи букву на русском: ').lower()
        if letter in set_use_letter:
            print('Эту букву ты уже вводил')
            print('Список использованных букв', set_use_letter)
        elif len(letter) > 1:
            print('Только одну букву')
        elif letter not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('На русском, пожалуйста')
        elif letter not in select_word2:
            set_use_letter.add(letter)
            count_errors += 1
            error_number += 1
            print('Неверно! Количество ошибок', count_errors, 'из 6')
            print('Список использованных букв', set_use_letter)
        elif letter in select_word2:
            set_use_letter.add(letter)
            print('Список использованных букв', set_use_letter)
            for i in range(len(select_word2)):
                if letter == select_word2[i]:
                    unkown_word2 += letter
                else:
                    unkown_word2 += unkown_word[i]
            unkown_word = unkown_word2
            print('Верно! Количество ошибок', count_errors, 'из 6')
            print('Загаданное слово:', ''.join(unkown_word))
            print('Список использованных букв', set_use_letter)
            if select_word2 == unkown_word:
                print('Поздравляю с победой!')
                print('Ты угадал слово:', ''.join(select_word2))
                select_word()
                start_game()
    else:
        print(draw_hanged_man(6), 'Покойся с миром')
        print('Загаданное слово:', ''.join(select_word2))
        select_word()
        start_game()


start_game()

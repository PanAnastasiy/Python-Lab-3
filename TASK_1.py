from ColorLibraryOfLabWork_3 import *
import os

# 1. Создать программный файл F1 в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
# Скопировать в файл F2 только те строки из F1, которые заканчиваются символом «А».


def task_1():
    print('\n' * 100)
    first_task()
    position = add_lines_to_f1()
    check_add_lines_to_f2(position)
    print_lines_of_f2()


def first_task():
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------------'
                                     '--------------------------------------------+')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +
          '  УСЛОВИЕ ЗАДАНИЯ 1:',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          ' Создать программный файл F1 в текстовом формате, записать в него построчно данные,'
          ' вводимые пользователем.\n'
          ' Об окончании ввода данных будет свидетельствовать пустая строка.\n'
          ' Скопировать в файл F2 только те строки из F1, которые заканчиваются символом «А».\n'
          ' Описать функцию triangle, принимающую 1 аргумент — сторону равностороннего треугольника,\n '
          'и возвращающую 2 значения (с помощью кортежа): периметр и площадь треугольника.\n',
          )
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------------'
                                     '--------------------------------------------+')

def add_lines_to_f1():
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '+----------------------------------------+\n' 
                                               '| Осуществляем запись строк в файл F1... |\n'
                                               '+----------------------------------------+\n'
          )
    counter = 1
    with open('F1.txt', 'a', encoding='UTF-8') as file_1:
        pos = file_1.tell()
        while True:
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f'{counter}) Введите строку : ', end='')
            line = input()
            if line == '':
                print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                        'Вами была введена ПУСТАЯ строка!'
                                                        '\U0001f353\U0001f353\U0001f353', end='')
                break
            counter += 1
            file_1.write(line + '\n')
    return pos


def check_add_lines_to_f2(pos):
    check = False
    with open('F1.txt', 'r', encoding='UTF-8') as file_1, open('F2.txt', 'a', encoding='UTF-8') as file_2:
        file_1.seek(pos)
        for line in file_1.readlines():
            line = line.strip()
            if line[-1] in 'AА':
                check = True
                file_2.write(line + '\n')
    if not check:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                "В ведённых вами строках нет заканчивающихся на символ 'A'. "
              "В файле F2 будут содержаться строки заканчивающиеся на символ 'A', добавленные ранее."
                                                '\U0001f353\U0001f353\U0001f353')


def print_lines_of_f2():
    counter = 1
    with open('F2.txt', 'r', encoding='UTF-8') as file_2:
        if os.path.getsize('F2.txt'):
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +
                  "\nВсе строчки заканчивающиеся на символ 'A', скопированные в файл F2 отображены ниже : ")
            print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '+-----+-----------------------------+\n'
                                                     '|  №  |     Содержимое файла F2     |\n'
                                                     '+-----+-----------------------------+')
            for line in file_2.readlines():
                line = line.strip()
                print(Style.BRIGHT + Fore.LIGHTWHITE_EX + '|',
                      Style.BRIGHT + Fore.LIGHTCYAN_EX
                      + f'  {str(counter).ljust(2)} ',
                      Style.BRIGHT + Fore.LIGHTWHITE_EX + '|',
                      Style.BRIGHT + Fore.LIGHTWHITE_EX + f' {str(line[:-1])}', Style.BRIGHT + Fore.LIGHTRED_EX +
                      f'{line[-1].ljust(29 - len(line))}',
                      Style.BRIGHT + Fore.LIGHTCYAN_EX + '|', sep='')
                counter += 1
            print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '+-----+-----------------------------+')
        else:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                    'Увы! Но файл F2 пуст. '
                                                    'В файл один F1 НЕ было записано ни одной строчки,'
                                                    " заканчивающейся на 'A'.\n"
                                                    '\U0001f353\U0001f353\U0001f353')

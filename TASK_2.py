from ColorLibraryOfLabWork_3 import *
import os


# 2. Создать текстовый файл (не программно).
# Построчно записать фамилии студентов и величину их средних баллов за сессию (не менее 10 строк).
# Определить, кто из студентов имеет средний балл от 4 до 6, кто от 6 до 8, а кто выше 8,
# вывести фамилии этих студентов.
# Вывести на экран студента с максимальным средним баллом.
# Пример файла:
# Иванов 4.87
# Петров 8.8


def task_2():
    print('\n' * 100)
    second_task()
    students = read_file()
    while True:
        your_choice = menu_of_task_2()
        match your_choice:
            case '1':
                add_student()
                students = read_file()
            case '2':
                print_student_4_6(students)
            case '3':
                print_student_6_8(students)
            case '4':
                print_student_8(students)
            case '5':
                print_best_student(students)
            case '6':
                print('\n' * 100)
                return 0
        if your_choice not in '123456':
            print('\n' * 100)
            print(Style.BRIGHT + Fore.BLUE +
                  '+---------------------------------------------------------------------------------+')
            print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
                  'Введённый вами номер задачи отсутствует в перечне функций. Повторите свой ввод.',
                  Style.BRIGHT + Fore.BLUE + '|')
            print(Style.BRIGHT + Fore.BLUE +
                  '+---------------------------------------------------------------------------------+')


def second_task():
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------------'
                                     '--------------------------------------------+')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +
          '  УСЛОВИЕ ЗАДАНИЯ 2:',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'Создать текстовый файл (не программно).\n'
                                                ' Построчно записать фамилии студентов и величину их средних'
                                                '  баллов за сессию (не менее 10 строк).\n'
                                                ' Определить, кто из студентов имеет средний балл от 4 до 6, '
                                                ' кто от 6 до 8, а кто выше 8,\n'
                                                ' вывести фамилии этих студентов.\n'
                                                ' Вывести на экран студента с максимальным средним баллом.\n'
                                                ' Пример файла:\n'
                                                ' Иванов 4.87\n'
                                                ' Петров 8.8\n'

          )
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------------'
                                     '--------------------------------------------+')
def read_file():
    with open('students.txt', 'r', encoding='UTF-8') as file:
        data = file.readlines()
    dictionary = dict([data[i].split() for i in range(len(data))])
    return dictionary


def add_student():
    with open('students.txt', 'a', encoding='UTF-8') as file:
        while True:
            try:
                print(Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Введите данные студента согласно формату "Иванов 4.87" :')
                line = input()
                name, point = line.split()
                if float(point) > 10 or float(point) < 0:
                    print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                            'Некорректный ввод данных.'
                                                            '\U0001f353\U0001f353\U0001f353')
                    continue
                break
            except ValueError:
                print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                        'Некорректный ввод данных.'
                                                        '\U0001f353\U0001f353\U0001f353')
        file.write(line + '\n')


def print_student_4_6(data):
    if check_size_of_file():
        table_header_4_6()
        for key, value in data.items():
            if 4 <= float(data[key]) <= 6:
                print(Style.BRIGHT + Fore.LIGHTWHITE_EX + '|',
                      Style.BRIGHT + Fore.LIGHTGREEN_EX +
                      f' {key.ljust(16)}',
                      Style.BRIGHT + Fore.LIGHTWHITE_EX +
                      '|',
                      Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
                      f' {value.ljust(16)}',
                      Style.BRIGHT + Fore.LIGHTWHITE_EX +
                      '|\n'
                      '+---------------------------------------+')
    else:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                'В созданном файле студентов отсутствуют какие-либо сведения.'
                                                '\U0001f353\U0001f353\U0001f353')


def print_student_6_8(data):
    if check_size_of_file():
        table_header_6_8()
        for key, value in data.items():
            if 6 <= float(data[key]) <= 8:
                print(Style.BRIGHT + Fore.LIGHTWHITE_EX + '|',
                      Style.BRIGHT + Fore.LIGHTGREEN_EX +
                      f' {key.ljust(16)}',
                      Style.BRIGHT + Fore.LIGHTWHITE_EX +
                      '|',
                      Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
                      f' {value.ljust(16)}',
                      Style.BRIGHT + Fore.LIGHTWHITE_EX +
                      '|\n'
                      '+---------------------------------------+')
    else:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                'В созданном файле студентов отсутствуют какие-либо сведения.'
                                                '\U0001f353\U0001f353\U0001f353')


def print_student_8(data):
    if check_size_of_file():
        table_header_8()
        for key, value in data.items():
            if 8 <= float(data[key]) <= 10:
                print(Style.BRIGHT + Fore.LIGHTWHITE_EX + '|',
                      Style.BRIGHT + Fore.LIGHTGREEN_EX +
                      f' {key.ljust(16)}',
                      Style.BRIGHT + Fore.LIGHTWHITE_EX +
                      '|',
                      Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
                      f' {value.ljust(16)}',
                      Style.BRIGHT + Fore.LIGHTWHITE_EX +
                      '|\n'
                      '+---------------------------------------+')
    else:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                'В созданном файле студентов отсутствуют какие-либо сведения.'
                                                '\U0001f353\U0001f353\U0001f353')


def print_best_student(data):
    if check_size_of_file():
        table_header_best()
        max_value = max([float(i) for i in data.values()])
        for key in data.keys():
            if float(data[key]) == max_value:
                print(Style.BRIGHT + Fore.LIGHTWHITE_EX + '|',
                      Style.BRIGHT + Fore.LIGHTGREEN_EX +
                      f' {key.ljust(16)}',
                      Style.BRIGHT + Fore.LIGHTWHITE_EX +
                      '|',
                      Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
                      f' {str(max_value).ljust(16)}',
                      Style.BRIGHT + Fore.LIGHTWHITE_EX +
                      '|\n'
                      '+---------------------------------------+')
    else:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                'В созданном файле студентов отсутствуют какие-либо сведения.'
                                                '\U0001f353\U0001f353\U0001f353')


def table_header_4_6():
    print(Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '+---------------------------------------+\n'
          '| Студенты со средним баллом от 4 до 6: |\n'
          '+-------------------+-------------------+\n'
          '|', Style.BRIGHT + Fore.LIGHTGREEN_EX +
          '      СТУДЕНТ      ',
          Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '| ',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          '  СРЕДНИЙ БАЛЛ:   ',
          Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '|\n'
          '+-------------------+-------------------+', sep='')


def table_header_6_8():
    print(Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '+---------------------------------------+\n'
          '| Студенты со средним баллом от 6 до 8: |\n'
          '+-------------------+-------------------+\n'
          '|', Style.BRIGHT + Fore.LIGHTGREEN_EX +
          '      СТУДЕНТ      ',
          Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '| ',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          '  СРЕДНИЙ БАЛЛ:   ',
          Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '|\n'
          '+-------------------+-------------------+', sep='')


def table_header_8():
    print(Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '+---------------------------------------+\n'
          '|   Студенты со средним баллом выше 8   |\n'
          '+-------------------+-------------------+\n'
          '|', Style.BRIGHT + Fore.LIGHTGREEN_EX +
          '      СТУДЕНТ      ',
          Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '| ',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          '  СРЕДНИЙ БАЛЛ:   ',
          Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '|\n'
          '+-------------------+-------------------+', sep='')


def table_header_best():
    print(Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '+---------------------------------------+\n'
          '| Студенты со НАИЛУЧШИМ средним баллом: |\n'
          '+-------------------+-------------------+\n'
          '|', Style.BRIGHT + Fore.LIGHTGREEN_EX +
          '      СТУДЕНТ      ',
          Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '| ',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          '  СРЕДНИЙ БАЛЛ:   ',
          Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '|\n'
          '+-------------------+-------------------+', sep='')


def menu_of_task_2():
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          '                    МЕНЮ ЗАДАНИЯ 2 :                      ',
          Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 1.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Добавить информацию о студенте.                        ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 2.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Информация о студентах со средним баллом (4-6).        ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 3.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Информация о студентах со средним баллом (6-8).        ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 4.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Информация о студентах со средним баллом (8-10).       ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 5.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Информация о студенте(ах) с наивысшим баллом.          ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 6.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Выйти из задания 2.                                    ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          ' Введите номер подзадачи, которую желаете реализовать :   ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    return input()


def check_size_of_file():
    if os.path.getsize('students.txt'):
        return True
    else:
        return False

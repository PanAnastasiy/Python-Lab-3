from ColorLibraryOfLabWork_3 import *

# 3. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести его на экран.
# Примеры строк файла: Информатика:100(л) 50(пр) 20(лаб).
#                                        Физика: 30(л) 10(лаб)
#                                        Физкультура: 30(пр)
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}.


def task_3():
    name_of_subjects = []
    count_of_classes = []
    with open('InfoOfSubjects.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            total = 0
            info = line.strip().split()
            name_of_subjects.append(info[0][:-1])
            for i in range(1, len(info)):
                comma = info[i].index('(')
                total += (int(info[i][: comma]))
            count_of_classes.append(total)
    print_answer(dict(zip(name_of_subjects, count_of_classes)))


def print_answer(dictionary):
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\n+----------------------------------------+\n'
                                               '|  Словарь представлен в виде таблицы :  |\n'
                                               '+----------------------------------------+\n'
          )
    print(Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '+------------------------+\n'
          '|',
          Style.BRIGHT + Fore.LIGHTGREEN_EX +
          '  ПРЕДМЕТ  ',
          Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '|',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          'ЗАНЯТИЯ ',
          Style.BRIGHT + Fore.LIGHTWHITE_EX +
          '|\n'
          '+------------------------+')
    for key, value in dictionary.items():
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + '|',
              Style.BRIGHT + Fore.LIGHTGREEN_EX +
              f'{key.ljust(11)}',
              Style.BRIGHT + Fore.LIGHTWHITE_EX +
              '|',
              Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
              f'   {str(value).ljust(3)}  ',
              Style.BRIGHT + Fore.LIGHTWHITE_EX +
              '|\n'
              '+------------------------+')

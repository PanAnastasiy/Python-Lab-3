from ColorLibraryOfLabWork_3 import *
import json

# 4. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь
# (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста. – 1 балл (задача на оценку 10)


def task_4():
    python_object = []
    result_of_firm = {}
    with open('InfoOfFirms.txt', 'r+', encoding='UTF-8') as file:
        for line in file:
            if line[0] in '+ ':
                break
            line = line.strip().split()
            result_of_firm[line[0]] = int(line[2]) - int(line[3])
        python_object.append(result_of_firm)
        number = [int(i) for i in result_of_firm.values() if int(i) > 0]
        average_profit = round(sum(number) / len(number), 3)
        python_object.append({"average_profit": average_profit})
        file.seek( open('InfoOfFirms.txt').read().find('+') + 3)
        file.write('\n+------------------------------------------------------------------+\nJson-объект имеет вид :\n')
        file.write(json.dumps(python_object, indent=4, ensure_ascii=False))
    print_json_object(python_object)


def print_json_object(obj):
    keys = tuple(obj[0].keys())
    values = tuple(obj[0].values())
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +
          '\n\n+----------------------------------+\n'
          '|     ФИРМА     | ПРИБЫЛЬ / УБЫТКИ |\n'
          '+----------------------------------+')
    for i in range(len(obj[0])):
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + f'| {keys[i].ljust(14)}| {str(values[i]).ljust(16)} |\n'
              '+----------------------------------+')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'\n\nСредняя прибыль всех фирм составляет :  '
                                               f'\033[4m{obj[1]["average_profit"]}\033[0m')

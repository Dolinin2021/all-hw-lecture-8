from pprint import pprint
import os

file_name = 'task_1.txt'
PATH = f'{os.getcwd()}/{file_name}'


def get_data(file_name):

    data = dict()

    with open(file_name, encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            counter = int(file.readline())
            temp_list = []

            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split('|')
                temp_list.append(
                    {'ingredient_name': ingredient_name.strip(), 'measure': measure.strip(), 'quantity': quantity.strip()}
                )
            data[dish_name] = temp_list
            file.readline()

    return data

def get_shop_list_by_dishes(cook_book, dishes, person_count):

    data = dict()

    for key, value in cook_book.items():
        if key in dishes:

            for variable in value:
                name = variable['ingredient_name']
                measure = variable['measure']
                quantity = int(variable['quantity'])
                if name in data.keys():
                    data[name]['quantity'] = data[name]['quantity'] + quantity * person_count
                else:
                    data[name] = {'measure': measure, 'quantity': quantity * person_count}

    return data


pprint(get_data(PATH))
pprint(get_shop_list_by_dishes(get_data(PATH),['Запеченный картофель', 'Омлет'], 2))
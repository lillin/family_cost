import funcfam
import json
from os import path


def build_menu(menu):
    funcfam.pretty_menu(menu)
    while True:
        i = input('Choose menu item \n')
        if i == 'q':
            return

        if not i.isdigit():
            print('Not a number!')
            continue  # go to while loop before user entering number
        i = int(i)
        if i < 0 or i >= len(menu):
            print('Wrong number!')
            continue
        menu[i][1]()
        funcfam.pretty_menu(menu)


def main():
    build_menu(main_menu)


def add_action():
    t = input('Add type of costs').lower().strip()
    s = int(input('Add sum'))
    return funcfam.add_to_dict(data, t, s)


def filter_action():
    build_menu(filter_menu)


def show():
    return funcfam.print_pretty(data)


def filter_():
    return funcfam.filter_by(data, seq=input('Add word or it\'s part to filter by it'))


def sort_():
    return funcfam.sort_by(data)


def chart_action():
    funcfam.chart_action(data)


def import_action():
    """

    import data to json by user's path
    """
    user_path = input('Write a full path to your file\n')  # user write his path
    file_path = path.realpath(user_path)  # refactoring user path
    global data
    file = open(file_path, 'w')
    json.dump(data, file)


def load_action():
    """

    load data from json by user's path
    """
    user_path = input('Write a full path to your file\n')
    file_path = path.realpath(user_path)
    global data
    data = open_file(file_path)


def open_file(name):
    """

    open file by it's name
     :return data from json(dict)
    """
    j = open(name, 'r+')
    return json.load(j)


main_menu = [
    ['Add new', add_action],
    ['Show all, filter or sort', filter_action],
    ['Show chart', chart_action],
    ['Import to...', import_action],
    ['Import from...', load_action]
]

filter_menu = [
    ['Show all', show],
    ['Filter by', filter_],
    ['Sort by ', sort_]
]

data = open_file('data_fam_costs')

if __name__ == '__main__':
    main()
    with open('data_fam_costs', 'r+') as f:
        json.dump(data, f)
    print('Goodbye!')

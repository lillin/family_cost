import operator
import random
import turtle
from collections import OrderedDict


def print_pretty(dictionary):
    """

    :type dictionary: dict
    """
    for key, value in iter(dictionary.items()):
        print(key.capitalize(), sum(value))


def pretty_menu(menu, offset=''):
    for n, item in enumerate(menu):
        print(offset, '{0} {1}'.format(n, item[0]))
    print(offset, '{0} {1}'.format('q', 'Quit'))


def add_new(dictionary, key, value):
    dictionary[key] = [value]
    return print(dict)


def add_to_dict(dictionary, key, value):
    """
    function to add to dict new data
    :param value: 
    :param key: 
    :param dictionary:
    :type dictionary: dict
    """
    if key in dictionary.keys():
        dictionary[key].append(value)
        print(dictionary)

    else:
        add_new(dictionary, key, value)

    return print_pretty(dictionary)


def filter_by(dictionary, seq):
    """

    :type dictionary: dict
    :type seq: str
    """
    new_dict = dict((k, v) for k, v in dictionary.items() if seq in k)
    return print_pretty(new_dict)


def sort_by(dictionary):
    """

    :type dictionary: dict
    """
    data = refactor_values(dictionary)
    asc_desc = input(
        'Press 1 if you want sort ascending \n'
        'Press 2 if you want sort descending \n'
    )
    if asc_desc == '1':
        sorted_data = sorted(data.items(), key=operator.itemgetter(1))
        return pretty_print_for_sort(sorted_data)
    elif asc_desc == '2':
        sorted_data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
        return pretty_print_for_sort(sorted_data)
    else:
        print('You choice is unavailable, please try again')


def refactor_values(dictionary):
    """

    :type dictionary: dict
    :param dictionary:
    :return: new_data
    """

    new_data = {}
    for key, value in iter(dictionary.items()):
        new_data[key] = sum(value)
    return new_data


def pretty_print_for_sort(sorted_data):
    for k, v in sorted_data:
        print('{0} {1}'.format(v, k.capitalize()))


def convert_to_rgb(seq):
    """
    :type seq: list
    :return: str
    """
    rgb = '#'
    for item in seq:
        rgb += hex(item).split('x')[1]
    return rgb


def random_color():
    rgb = [random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)]
    white = [255, 255, 255]

    pastel_color = list(map(lambda x, y: (x + y) // 2, rgb, white))  # [189, 241, 185]

    return convert_to_rgb(pastel_color)


def sum_values(dictionary):
    """

    :type dictionary: dict
    """
    values_sum = 0
    for values in dictionary.values():
        values_sum += values
    return values_sum


def angles(dictionary):
    values_sum = sum_values(dictionary)
    for key, value in dictionary.items():
        dictionary[key] = value / values_sum * 360
    return dictionary


def chart_action(dictionary):

    new_data = refactor_values(dictionary)
    dict_of_angles = OrderedDict(angles(new_data))

    turtle.Screen()
    t = turtle.Turtle()
    # write func to step-by-step proc
    while len(dict_of_angles) != 0:
        try:
            t.left(90)
            t.fd(200)
            t.color(random_color())
            t.begin_fill()
            t.right(90)
            t.circle(-200, dict_of_angles.popitem()[1])  # y-cord - degree of angle
            t.write(list(dict_of_angles.keys())[-1], align='center')
            position = t.pos()  # (40.67,91.35) check cord to return
            t.goto(0, 0)  # return into center of circle
            t.end_fill()
            t.color(random_color())
            t.begin_fill()
            t.goto(position)  # return into cord
            t.circle(-200, dict_of_angles.popitem()[1])
            t.write(list(dict_of_angles.keys())[-1], align='center')
            position = t.pos()
            t.goto(0, 0)
            t.end_fill()
        except IndexError:
            break

    turtle.done()



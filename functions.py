import json
import re
from datetime import datetime


def load_file(link):
    with open(link, 'r', encoding="utf-8") as read_file:
        data = json.load(read_file)
        return data


def format_numbers(var):
    if var is None:
        return None, None
    else:
        number = var.split(sep=" ")[-1]
        name_acc = var.split(sep=" ")[:-1]

        if len(number) == 16:
            new_number = re.sub(r'.{4}', r'\g<0> ', number[0:6] + '*' * 6 + number[12:])[:-1]
            return new_number, ' '.join(name_acc)

        elif len(number) == 20:
            new_number = '*' * 2 + number[16:]
            return new_number, ' '.join(name_acc)


def format_date(date, format='%d.%m.%Y'):
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f').strftime(format)


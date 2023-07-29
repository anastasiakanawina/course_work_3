from functions import load_file
from functions import format_numbers
from functions import format_date
from datetime import datetime

link_oper = 'operations.json'
data = load_file(link_oper)

data = [x for x in data if x and x.get('state', "null") == 'EXECUTED']

transaction = sorted(data, key=lambda x: datetime.strptime(x.get('date'), '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)


for i in transaction[:5]:
    if i.get('state', "null") == 'EXECUTED':
        from_numbers = i.get('from', "null")
        to_numbers = i.get('to', "null")
        for_amount = i.get('operationAmount', "null")
        date_trans = format_date(i.get('date', "null"))
        description = i.get('description', "null")

        print(date_trans, description)

        if from_numbers == "null":
            print(format_numbers(to_numbers)[1], format_numbers(to_numbers)[0])
            print(for_amount.get('amount', "null"), for_amount.get('currency', "null").get('name', "null"))
            print()
        else:
            print(format_numbers(from_numbers)[1], format_numbers(from_numbers)[0], '->',
                  format_numbers(to_numbers)[1], format_numbers(to_numbers)[0])
            print(for_amount.get('amount', "null"), for_amount.get('currency', "null").get('name', "null"))
            print()


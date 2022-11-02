from PyInquirer import prompt
from csv import DictWriter
import csv

field_names = ['amount', 'label', 'spender', 'users']


def get_users():
    file = open('user_report.csv', newline='')
    reader = csv.reader(file)
    data = list(reader)
    file.close()
    users = []
    for user in data[1:]:
        users.append(user[0])
    return users

def get_users_involved(spender):
    file = open('user_report.csv', newline='')
    reader = csv.reader(file)
    data = list(reader)
    file.close()
    users = []
    for user in data[1:]:
        print(user[0] + "   " + spender)
        if user[0] != spender:
            users.append(user[0])
    return users

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message": "New Expense - Spender: ",
        "choices": get_users(),
    },
]


def new_expense(*args):
    infos = prompt(expense_questions)
    spender = infos['spender']
    users = prompt([
    {
        "type":"checkbox",
        "name":"users",
        "message":"New Expense - Select spenders",
        'choices': [{'name': x, 'checked': False} for x in get_users_involved(spender)],
    },
    ])
    infos['users'] = users['users']

    file = open('expense_report.csv', 'a')
    #TODO : divide equally between involved users
    dictwriter_object = DictWriter(file, fieldnames=field_names, lineterminator='\n')
    dictwriter_object.writerow(infos)
    file.close()
    print("Expense Added !")
    return True



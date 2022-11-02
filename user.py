from PyInquirer import prompt
from csv import DictWriter

field_names = ['name']

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"Add User - Name: ",
    },
]

def add_user():
    infos = prompt(user_questions)

    file = open('user_report.csv', 'a')
    dictwriter_object = DictWriter(file, fieldnames=field_names, lineterminator='\n')
    dictwriter_object.writerow(infos)
    file.close()

    print("User Added !")
    return True
import csv
from expense import get_users
import numpy as np
import ast

def get_index(name):
    return get_users().index(name)

def get_name(index):
    return get_users()[index]

def get_status():
    file = open('expense_report.csv', newline='')
    reader = csv.reader(file)
    expenses = list(reader)
    file.close()

    users = get_users()
    len_u = len(users)

    matrix = np.zeros((len_u, len_u))
    
    for expense in expenses[1:]:
        spender_index = get_index(expense[2])
        involved = ast.literal_eval(expense[3])
        for inv in involved:
            index_inv = get_index(inv)
            matrix[spender_index][index_inv] += int(expense[0])
    
    #matrix can be diagonal but I did not had time

    for i in range(0, len_u):
        lign = get_name(i) + " owes "
        for e in range(0, len_u):
            if e == i:
                continue
            sum = matrix[i][e] - matrix[e][i]
            lign += str(sum) + " to " + get_name(e) + "\n" #TO FINISH
    print(lign)
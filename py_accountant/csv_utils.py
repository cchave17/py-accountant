import csv

from py_accountant.modules.expense import Expense

LIABILITIES = './../data/Liabilities.csv'
EXPENSES = './../data/Liabilities.csv'


def get_csv_file_data(FILEPATH):
    """

    """
    expenses = []

    with open(FILEPATH, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            recurring_date = row['Date']
            name = row["Name"]
            amount= row["Amount"]
            cur_exp = Expense(recurring_date,name,amount)
            expenses.append(cur_exp)



get_csv_file_data(EXPENSES)


import csv
import dateutil.parser

import tabulate


from py_accountant.modules.account import set_account
from py_accountant.modules.expense import Expense

# ACCOUNTS = './../data/Accounts.csv'
# EXPENSES = './../data/Expenses.csv'


def get_account_data():
    """
    This functions is a test function
    """
    accounts = []

    with open('./data/Accounts.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # date = row["Date"]
            # name = row["Name"]
            # amount = row["Amount"]
            # amount = float(re.sub('[^0-9.]', '', row["Amount"]))
            # account_type = row["Type"]
            #
            # cur_account = set_account(date, name, amount, account_type)
            # accounts.append(cur_account)
            row["Date"] = dateutil.parser.parse(row["Date"]).date().strftime('%m-%d-%Y')
            accounts.append(row)

    header = accounts[0].keys()
    rows = [x.values() for x in accounts]
    print(tabulate.tabulate(rows, header, tablefmt='grid'))


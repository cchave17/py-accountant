import csv
import tabulate
from py_accountant.modules.expense import Expense

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
            # cur_exp = Expense(recurring_date,name,amount)
            expenses.append(row)

    header = expenses[0].keys()
    rows = [x.values() for x in expenses]
    print(tabulate.tabulate(rows, header, tablefmt='grid'))



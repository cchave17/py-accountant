import csv


LIABILITIES = './../data/Liabilities.csv'
EXPENSES = './../data/Liabilities.csv'


def get_csv_file_data(FILEPATH):

    amount = 0

    with open(FILEPATH, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount += float(row["Amount"])
            # recurring_date = row['Date']
    print(amount)

get_csv_file_data(EXPENSES)


import csv
from py_accountant.modules.schedule_date import Date, get_date_difference
from datetime import datetime

dt1 = Date(13, 12, 2018)
dt2 = Date(25, 3, 2019)

# print(datetime.today().strftime('%m-%d-%Y'))
# print(get_date_difference(dt1,Date(27,6,2022)))

def get_day_month_year():
    today = datetime.today()
    month = today.strftime('%Y')
    print(month)


def get_future_balance(d,m,y):
    today = datetime.today()
    day = today.strftime('%d')
    month = today.strftime('%m')
    year = today.strftime('%Y')
    today = Date(int(day),int(month),int(year))
    future_date = Date(d,m,y)

    amount_of_paychecks = get_date_difference(Date(1,1,2022),future_date)//14
    print(amount_of_paychecks)

    balance = amount_of_paychecks * 2429.61
    print(balance)

get_future_balance(31,12,2022)

# get_day_month_year()
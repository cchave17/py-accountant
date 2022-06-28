from py_accountant.console_ui.main_menu import select_main_menu
from py_accountant.csv_utils import get_csv_file_data

LIABILITIES = './data/Liabilities.csv'
EXPENSES = './data/Liabilities.csv'
def runner_app():
    """
    Run main application
    TESLA = $57,440
    """
    get_csv_file_data(EXPENSES)
    select_main_menu()
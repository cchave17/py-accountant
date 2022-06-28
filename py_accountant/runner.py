from py_accountant.console_ui.main_menu import select_main_menu
from py_accountant.csv_utils import get_account_data


def runner_app():
    """
    Run main application
    TESLA = $57,440
    """
    get_account_data()
    select_main_menu()
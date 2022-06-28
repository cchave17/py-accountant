class Account:
    """
    This class is to create the Account object
    """

    def __init__(self, date, name, amount, account_type):
        """
        Constructor for the Account Object
        :param name: Name of the Account
        :param description: Description for account
        :param account_type: Account type, either 'Debit'/'Credit'
        """
        self.date = date,
        self.name = name,
        self.amount = amount,
        self.account_type = account_type


def set_account(date, name, amount, account_type):
    return {
        "date": date,
        "name": name,
        "amount": amount,
        "account_type": account_type
    }

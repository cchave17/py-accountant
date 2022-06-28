class Expense:
    """
    This class is to create the Account object
    """

    def __init__(self, recurring_date, name, amount):
        """
        Constructor for the Account Object
        :param name: Name of the Account
        :param description: Description for account
        :param account_type: Account type, either 'Debit'/'Credit'
        """
        self.recurring_date = recurring_date,
        self.name = name,
        self.amount = amount

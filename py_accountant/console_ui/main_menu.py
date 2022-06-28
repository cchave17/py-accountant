import sys

def select_main_menu():
    """
    Display Main Menu
    """
    print("\nChoose an option: \n"
          "1: Accounts\n"
          "2: Revenue\n"
          "3: Expenses\n"
          "4: Budget\n"
          "5: Purchase Planner\n"
          "6: Planner schedule\n"
          "7: Quit")

    try:
        main_option =int(input())
    except ValueError:
        print("not a valid entry")
        sys.exit(1)
    return main_option
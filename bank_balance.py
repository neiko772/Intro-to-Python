def checking_balance(user_name, balance, deposits, expense_item, expense_amount):
    """Print a receipt and return the customer's ending balance."""
    ending_balance = balance + deposits - expense_amount

    print("\n--- Account Summary ---")
    print(f"Customer Name: {user_name}")
    print(f"Starting Balance: ${balance:.2f}")
    print(f"Deposits: ${deposits:.2f}")
    print(f"Purchase: {expense_item}")
    print(f"Amount Spent: ${expense_amount:.2f}")
    print(f"Ending Balance: ${ending_balance:.2f}")

    return ending_balance


def main():
    customer_name = input("What is your name?")
    starting_balance = 5000.25
    print(f"Welcome, {customer_name}! Your starting balance is ${starting_balance:.2f}.")

    pay_check = float(input("How much of your paycheck would you like to deposit? $"))
    expenditure_item = input("What did you spend money on? ")
    expenditure = float(input(f"How much did you spend on {expenditure_item}? $"))

    checking_balance(
        customer_name,
        starting_balance,
        pay_check,
        expenditure_item,
        expenditure
    )


if __name__ == "__main__":
    main()
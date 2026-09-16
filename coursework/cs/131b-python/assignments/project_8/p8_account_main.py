'''
p8_main.py
jl-ccsf
07/31/2026
CS-131B, Prof. Ibrahim
Updates bank accounts using superclass p8_account.py and subclasses 
p8_checking.py and p8_savings.py.
'''

# Defines error message
DEFAULT = "(Restored to default value.)"

def main():
    
    # Instantiates invoice class and subclasses using constructor method
    account_1 = Account(name = "Jules L", balance = 1000.0)
    checking_1 = Checking.Account(fee = 1.0)
    savings_1 = Savings.Account(save_balance = 2000.0, rate = 2.0)

    # Stores invoice data in list
    accounts = []
    if isinstance(Account):
        accounts.append()

    # Calls object state to display data for each invoice
    for item in range(len(accounts)):
        print(accounts[item].__str__())
        if (accounts[item].balance < 0.0):
            # Displays default value message
            print(DEFAULT)
        print()

    # Calculates interest and balance for savings
    savings_1.interest = calc_interest(accounts, save_balance, rate)
    savings_1.deposit = Savings.deposit(save_balance, interest)

    # Displays output header
    print("AFTER DEPOSIT:")
    print()

    # Calls object state to display data for each invoice
    for item in range(len(accounts)):
        print(accounts[item].__str__())
        if (balance < 0.0):
            # Displays default value message
            print(DEFAULT)
        print()

'''Calls invoice calculation method'''
def calc_interest(account, balance, rate):
    interest = accounts[item].cal_interest()
    return interest

# Initializes program
if __name__ == "__main__":
    main()

'''
p8_account.py
jl-ccsf
07/31/2026
CS-131B, Prof. Ibrahim
Establishes a class representing a bank account.
'''

class Account:

    # Defines static constants
    DEFAULT_NAME = "No Name"
    DEFAULT_BALANCE = 0.0

    # Defines error messages
    STR = "ERROR: Value must be a string. "
    FLT = "ERROR: Value must be a float. "
    DEFAULT = "Assigned default value."
    ZERO = "ERROR: Amount must be greater than 0. "
    NEG = "ERROR: Insuficient funds. "
    CANCEL = "Transaction canceled."

    # Assigns static variables
    __accounts = []

    '''Defines class for bank account'''
    def __init__ (self, 
                  name,  
                  balance):
        # Validates instance name
        if (type(name) != str):
            # Reverts to "No Name"
            self.__name = Account.DEFAULT_NAME
            # Displays error message
            print(Account.STR + Account.DEFAULT)
        else:
            # Assigns account name
            self.__name = name
        # Validates instance balance
        if (type(balance) != float) or (balance < 0):
            # Reverts to 0.0
            self.__balance = Account.DEFAULT_BALANCE
            # Displays error message
            if (type(balance) != float):
                print(Account.FLT + Account.DEFAULT)
            elif (balance < 0):
                print(Account.NEG + Account.DEFAULT)
        else:
            # Assigns account balance
            self.__balance = balance
        # Appends all instances to list
        Account.__accounts.append(self)

    '''Defines mutators'''
    def set_name(self, name):
        self.__name = name
    def set_balance(self, balance):
        self.__balance = balance

    '''Defines accessors'''
    def get_accounts(Account):
        return Account.__accounts
    def get_name(self):
        return self.__name
    def get_balance(self):
        return self.__balance 
    
    '''Deposits amount and adds to instance balance'''
    def deposit(self, balance, amount):
        if (self.valid_deposit(balance, amount) == False):
            print(f"Your balance is still ${balance:.2f}.") 
            # Your balance is still $0.00.
        else:
            balance += amount
            print(f"${amount:.2f} deposited.")
            print(f"Your new balance is ${balance:.2f}.") 
            # $0.00 deposited. Your new balance is $0.00.
        return balance 

    '''Validates deposits'''
    def valid_deposit(self, amount):
        if (self.deposit(amount) <= 0):
            print(Account.ZERO + Account.CANCEL)
            # ERROR: Amount must be greater than 0. Transaction canceled.
            update = False
        else:
            update = True
        return update

    '''Withdraws amount and subtracts from instance balance'''
    def withdraw(self, balance, amount):
        if (self.valid_withdraw(balance, amount) == False):
            print(f"Your balance is still {Account.format_amount(balance)}.") 
            # Your balance is still $0.00.
        else:
            balance -= amount
            print(f"${amount:.2f} withdrawn.")
            print(f"Your new balance is {Account.format_amount(balance)}.") 
            # $0.00 withdrawn. Your new balance is $0.00.
        return balance
        # 0.0

    '''Validates withdrawals'''
    def valid_withdraw(self, balance, amount):
        if (self.withdraw(amount) <= 0):
            print(Account.ZERO + Account.CANCEL)
            # ERROR: Amount must be greater than 0. Transaction canceled.
            update = False
        else:
            if (self.withdraw(amount) > balance):
                print(Account.NEG + Account.CANCEL)
                # ERROR: Insuficient funds. Transaction canceled.
                update = False
            else: 
                update = True
        return update

    '''Formats float values'''
    def format_amount(amount):
        format = (f"${amount:.2f}")
        return format 
        # $0.00
    
    '''Displays all class objects'''
    def __str__(self):
        acc_str = (f"Account Holder: {self.__name}"
                   f"\nAccount Balance: {Account.format_amount(self.__balance)}"
                   f"\nNumber of Accounts: {len(Account.__accounts)}")
        return acc_str

'''
SAMPLE OUTPUT

Account Holder: No Name
Account Balance: $0.00
Number of Accounts: 1

$0.00 deposited. Your new balance is $0.00.
$0.00 withdrawn. Your new balance is $0.00.
'''

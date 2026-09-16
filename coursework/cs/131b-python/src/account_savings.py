'''
p8_savings.py
jl-ccsf
07/31/2026
CS-131B, Prof. Ibrahim
Establishes a subclass representing a savings account using the superclass 
p8_account.py.
'''

class Savings(Account):

    # Defines static constants
    DEFAULT_RATE = 0.0
    DEFAULT_INTEREST = 0.0

    '''Initializes saving subclass from Account superclass'''
    def __init__(self, name, balance, sav_balance, rate):
        # Initializes superclass attributes
        Account.__init__(self, name, balance)
        # Initializes subclass attributes
        if (type(sav_balance) != float) or (sav_balance < 0):
            # Assigns default value
            self.__sav_balance = Account.DEFAULT_BALANCE
        else:
            # Assigns instance savings balance
            self.__sav_balance = sav_balance
        # Validates instance rate    
        if (type(rate) != float) or (rate < 0):
            # Assigns default value
            self.__rate = Savings.DEFAULT_RATE
        else:
            # Assigns instance rate
            self.__rate = rate

    '''Defines subclass mutators'''
    def set_sav_balance(self, sav_balance):
        self.__sav_balance = sav_balance
    def set_rate(self, rate):
        self.__rate = rate
    def set_interest(self, interest):
        self.__interest = interest

    '''Mutates formatted values'''
    def set_f_sav_bal(self, f_sav_balance):
        self.__f_sav_bal = f_sav_balance
    def set_f_rate(self, f_rate):
        self.__f_rate = f_rate
    def set_f_interest(self, f_interest):
        self.__f_interest = f_interest

    '''Defines subclass accessors'''
    def get_sav_balance(self):
        return self.__sav_balance
    def get_rate(self):
        return self.__rate
    def get_interest(self):
        self.__interest = Savings.calc_interest(self.__sav_balance, self.__rate)
        return self.__interest
    
    '''Accesses formatted values'''
    def get_f_sav_bal(self):
        self.__f_sav_bal = Account.format_amount(self.__sav_bal)
        return self.__f_sav_bal
    def get_f_rate(self):
        self.__f_rate = Account.format_amount(self.__rate)
        return self.__f_rate
    def get_f_interest(self):
        self.__f_interest = Account.format_amount(self.__interest)
        return self.__f_interest
    
    '''Calculates interest from rate'''
    def calc_interest(self, amount, rate):
        interest = float(amount * rate)
        # Validates interest
        if (self.valid_interest(interest) == False):
            print(f"No interest earned.")
            # No interest earned.
        else:
            print(f"${interest:.2f} interest earned.")
            # $0.00 interest earned.
        return interest

    '''Validates interest'''
    def valid_interest(interest):
        if (interest < 0):
            # Reverts interest to 0.0
            interest = Savings.DEFAULT_INTEREST
            # Displays error message
            print(Account.ZERO + Account.DEF)
            valid = False
        else:
            valid = True

    '''Adds deposit and interest to savings account'''
    def deposit(self, sav_balance, amount, interest):
        # Validates deposit amount
        if (Account.valid_deposit(sav_balance, amount) == False):
            # Displays error message
            print(Account.CANCEL)
            # Displays unchanged balance
            print(f"Your balance is still ${sav_balance:.2f}.")
            # Your balance is still $0.00.
        else:
            # Validates interest
            if (self.valid_interest(interest) == False):
                # Omits interest from deposit
                sav_balance += amount
                # Displays deposit and new balance
                print(f"${amount:.2f} deposited. No interest earned.")
                # $0.00 deposited. No interest earned.
                print(f"Your new balance is ${sav_balance:.2f}.")
                # Your new balance is $0.00.
            else:
                # Adds interest to deposit
                deposit = (amount + interest)
                # Updates savings balance
                sav_balance += deposit
                # Displays deposit, interest, and new balance
                print(f"${amount:.2f} deposited. " / 
                      f"{interest:.2f} interest earned.")
                # $0.00 deposited. $0.00 earned.
                print(f"Your new balance is ${sav_balance:.2f}.")
                # Your new balance is $0.00.
        return sav_balance
        # 0.0

    '''Displays all objects in superclass and savings account'''
    def __str__(self):
        # Adds ammends balance and transaction fee to output
        sav_str = (f"\nSavings Balance: {self.__f_sav_bal}\n" \
                   f"\nInterest Rate: {self.__f_rate}\n" \
                   f"\nTotal Interest: {self.__f_interest}\n")
        return (super().__str__() + sav_str)

'''
SAMPLE OUTPUT

Account Name: No Name
Account Balance: $0.00
Number of Accounts: 3
Savings Balance: $0.00
Interest Rate: $0.00
Total Interest: $0.00

$0.00 deposited. $0.00 earned.
Your new balance is $0.00.
'''

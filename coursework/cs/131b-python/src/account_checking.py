'''
p8_checking.py
jl-ccsf
07/31/2026
CS-131B, Prof. Ibrahim
Establishes a subclass representing a checking account using the superclass 
p8_account.py.
'''

class Checking(Account):

    # Defines static constant
    DEFAULT_FEE = 0.0

    '''Initializes Checking subclass from Account superclass'''
    def __init__(self, name, balance, fee):
        # Initializes superclass attributes
        Account.__init__(self, name, balance)
        # Initializes subclass instance attribute 
        if (type(fee) != float) or (fee < 0):
            # Reverts to default value
            self.__fee = Checking.DEFAULT_FEE
            # Displays error message
            if (type(fee) != float):
                print(Account.FLT + Account.DEFAULT)
            elif (fee < 0):
                print(Account.NEG + Account.DEFAULT)
        else:
            # Assigns transaction fee
            self.__fee = fee

    '''Defines subclass mutators'''
    def set_fee(self, fee):
        self.__fee = fee
    def set_f_fee(self, f_fee):
        self.__f_fee = f_fee

    '''Defines subclass accessors'''
    def get_fee(self):
        return self.__fee
    def get_f_fee(self):
        self.__f_fee = Account.format_amount(self.__fee)
        return self.__f_fee

    '''Displays all objects in superclass and Checking'''
    def __str__(self):
        # Adds ammends balance and transaction fee to output
        check_str = (f"\nChecking Balance: {self.__f_balance}"
                     f"\nTransaction Fee: {self.__f_fee}")
        return (super().__str__() + check_str)

'''
SAMPLE OUTPUT

Account Holder: No Name
Account Balance: $0.00
Number of Accounts: 2
Checking Balance: $0.00
Transaction Fee: $0.00

$0.00 deposited. Your new balance is $0.00.
$0.00 withdrawn. Your new balance is $0.00.
'''

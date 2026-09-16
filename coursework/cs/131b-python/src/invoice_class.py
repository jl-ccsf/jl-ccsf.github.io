'''
p7_invoice_class.py
jl-ccsf
07/21/2026
CS-131B, Prof. Ibrahim
Establishes a class representing an invoice for parts sold by an auto shop.
'''

class Invoice:

    '''Defines class for auto parts'''
    def __init__ (self, 
                  num = "0000", 
                  descr = "N/A", 
                  quant = 0, 
                  price = 0.0):
        # Validates instance attributes
        if (type(num) != str) or (not num.isdigit()) or (len(num) != 4):
            # Remains default value
            self.__num = "0"
        else:
            # Assigns part number
            self.__num = num
        if (type(descr) != str) or (len(descr) > 50):
            self.__descr = "N/A"
        else:
            # Assigns part description
            self.__descr = descr
        if (type(quant) != int) or (quant < 0):
            self.__quant = 0
        else:
            # Assigns part quantity
            self.__quant = quant
        # Validates instance price
        if (type(price) != float) or (price < 0):
            self.__price = 0.0
        else:
            # Assigns price per part
            self.__price = price

    '''Defines mutators'''
    def set_num (self, num):
        self.__num = num
    def set_descr (self, descr):
        self.__descr = descr
    def set_quant (self, quant):
        self.__quant = quant
    def set_price (self, price):
        self.__price = price
    def set_total (self, total):
        self._total = total

    '''Defines accessors'''
    def get_num (self):
        return self.__num
    def get_descr (self):
        return self.__descr
    def get_quant (self):
        return self.__quant
    def get_price (self):
        return self.__price

    '''Displays all objects'''
    def __str__(self):
        return (f"Part Number: {self.__num}\n" \
                f"Part Description: {self.__descr}\n" \
                f"Part Quantity: {self.__quant}\n" \
                f"Part Price: {self.__price}")

    '''Calculates invoice total'''
    def calculate_total(self):
        # Multiplies quantity by price
        total = float(self.__quant * self.__price)
        # Validates result
        if total < 0:
            total = 0.0
        return total

    '''Formats invoice total'''
    def format_invoice(self, total):
        format = (f"${total:.2f}")
        return format

'''
SAMPLE OUTPUT

Part Number: "0000"
Part Description: "N/A"
Part Quantity: 0
Part Price: 0.0
Invoice Total: $0.00
'''

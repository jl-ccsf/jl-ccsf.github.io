'''
p7_invoice_main.py
jl-ccsf
07/21/2026
CS-131B, Prof. Ibrahim
Generates invoices for each customer who bought parts from an auto shop using 
the class defined in p7_invoice_class.py.
'''

# Defines error message
DEFAULT = "(Restored to default value.)"

def main():
    
    # Instantiates invoice class using constructor method
    invoice_1 = Invoice(num = "0001", 
                        descr = "Car battery", 
                        quant = 10, 
                        price = 100.0) 
                        # Total: $1000.00
    
    # Instantiates with invalid values (reverts to default)
    invoice_2 = Invoice(num = 2222, 
                        descr = "I have a lot to say about this part and am " \
                        "NOT having a good day, so get ready to read over " \
                        "fifty characters worth of whining", 
                        quant = 127.00,
                        price = 2)
                        # Total: $0.00
    
    # Instantiates with invalid value (negative price)
    invoice_3 = Invoice(num = "0333", 
                        descr = "Returning the three I bought yesterday", 
                        quant = 3, 
                        price = -30.0) 
                        # Total: $0.00
    
    # Instantiates with valid values
    invoice_4 = Invoice(num = "0404", 
                        descr = "Tire set", 
                        quant = 4, 
                        price = 400.0)
                        # Total: $16000.00

    # Stores invoice data in list
    invoices = [invoice_1, invoice_2, invoice_3, invoice_4]

    # Calls object state to display data for each invoice
    for item in range(len(invoices)):
        print(invoices[item].__str__())
        # Retrieves invoice totals
        total = get_total(invoices, item)
        # Formats and displays invoice totals
        print(f"Invoice Total: {invoices[item].format_invoice(total)}")
        if (total == 0.0):
            print(DEFAULT)
        print()

    # Calls mutators to correct values
    invoice_2.set_num("2222")
    invoice_2.set_quant(2)
    invoice_2.set_price(127.00)
    invoice_3.set_price(30.0)

    # Displays output header
    print("UPDATED VERSION:")
    print()

    # Calls accessors to display data for each invoice
    for item in range(len(invoices)):
        print(f"Part Number: {invoices[item].get_num()}")
        print(f"Part Description: {invoices[item].get_descr()}")
        if (invoices[item].get_descr()) == "N/A":
            print(DEFAULT)
        print(f"Part Quantity: {invoices[item].get_quant()}")
        print(f"Part Price: {invoices[item].get_price()}")
        # Retrieves invoice totals
        total = get_total(invoices, item)
        # Formats and displays invoice totals
        print(f"Invoice Total: {invoices[item].format_invoice(total)}")
        print()

'''Calls invoice calculation method'''
def get_total(list, item):
    total = (list[item].calculate_total())
    return total

# Initializes program
if __name__ == "__main__":
    main()

'''
SAMPLE RUN A: ORIGINAL VALUES

Part Number: 0001
Part Description: Car battery
Part Quantity: 10
Part Price: 100.0
Invoice Total: $1000.00

Part Number: 0
Part Description: N/A
Part Quantity: 0
Part Price: 0.0
Invoice Total: $0.00
(Restored to default value.)

Part Number: 0333
Part Description: Returning the three I bought yesterday
Part Quantity: 3
Part Price: 0.0
Invoice Total: $0.00
(Restored to default value.)

Part Number: 0404
Part Description: Tire set
Part Quantity: 4
Part Price: 400.0
Invoice Total: $1600.00

SAMPLE RUN B: UPDATED VALUES

Part Number: 0001
Part Description: Car battery
Part Quantity: 10
Part Price: 100.0
Invoice Total: $1000.00

Part Number: 2222
Part Description: N/A
(Restored to default value.)
Part Quantity: 2
Part Price: 127.0
Invoice Total: $254.00

Part Number: 0333
Part Description: Returning the three I bought yesterday
Part Quantity: 3
Part Price: 30.0
Invoice Total: $90.00

Part Number: 0404
Part Description: Tire set
Part Quantity: 4
Part Price: 400.0
Invoice Total: $1600.00
'''

'''
p3_payroll_report.py
jl-ccsf
06/22/2026
CS-131B, Prof. Ibrahim
Generates a weekly payroll report from on user input. Calculates federal and 
state taxes, FICA withholding, and gross and net pay for each employee. Displays 
combined totals for all employees upon quit.
'''

def main():

    # Defines key variable
    gross_pay = 0

    # Defines counter-variables
    total_gross = 0
    total_fed = 0
    total_state = 0
    total_fica = 0
    total_withheld = 0
    total_net = 0

    # Begins payroll record
    print("Please enter the following:")
    print() # Blank line

    '''INITIALIZATION'''
    # Assigns integer value to employee
    employ_num = int(input("\tEmployee number (0 to quit): "))

    '''VALIDATION'''
    # Checks for negative value in initial input
    while (employ_num < 0):
        # Reports error message
        print("\tERROR: Invalid entry.")
        # Prompts re-entry
        employ_num = int(input("\tRe-enter employee number (0 to quit): "))

    '''MAIN LOOP'''
    while (employ_num > 0):
        
        '''GROSS PAY'''
        # Assigns decimal value to gross pay
        gross_pay = float(input("\tGross pay: $"))
        # Checks for empty or negative values
        while (gross_pay == 0 or gross_pay < 0):
            # Reports error message
            print("\tERROR: Invalid entry.")
            # Prompts re-entry
            gross_pay = float(input("\tRe-enter gross pay: $"))
        # Validates positive decimals if greater than zero 
        if (gross_pay > 0):
            # Updates total gross pay
            total_gross += gross_pay
        
        '''FED TAX'''
        # Assigns decimal value to federal tax
        fed_tax = float(input("\tFederal withholding: $"))
        # Checks for negative value
        while (fed_tax < 0):
            # Reports error message
            print("\tERROR: Invalid entry.")
            # Prompts re-entry
            fed_tax = float(input("\tRe-enter federal withholding: $"))
        # Validates positive decimals if zero or higher
        if (fed_tax >= 0):
            # Updates total federal tax
            total_fed += fed_tax
        
        '''STATE TAX'''
        # Assigns decimal value to state tax
        state_tax = float(input("\tState withholding: $"))
        # Checks for negative value
        while (state_tax < 0):
            # Reports error message
            print("\tERROR: Invalid entry.")
            # Prompts re-entry
            state_tax = float(input("\tRe-enter state withholding: $"))
        # Validates positive decimals if zero or higher
        if (state_tax >= 0):
            # Updates total state tax
            total_state += state_tax
        
        '''FICA'''
        # Assigns decimal value to FICA
        fica = float(input("\tFICA withholding: $"))
        # Checks for negative value
        while (fica < 0):
            # Reports error message
            print("\tERROR: Invalid entry.")
            # Prompts re-entry
            fica = float(input("\tRe-enter FICA withholding: $"))
        # Validates positive decimals if zero or higher
        if (fica >= 0):
            # Updates total FICA
            total_fica += fica
        
        '''WITHHOLDINGS'''
        # Calculates employee's combined withholdings
        withholdings = (fed_tax + state_tax + fica)
        # Checks for invalid or negative results
        if (withholdings > gross_pay) or (withholdings < 0):
            # Reports error message
            print("\tERROR: Invalid withholdings result.")
            print() # Blank line
            # Clears last entry from each total
            total_gross -= gross_pay
            total_fed -= fed_tax
            total_state -= state_tax
            total_fica -= fica
            print("Please try again:")
            print() # Blank line
            # Prompts re-start
            employ_num = int(input("\tRe-enter employee number (0 to quit): "))
            # Checks for negative value within main loop
            while (employ_num < 0):
                # Reports error message
                print("\tERROR: Invalid entry.")
                # Prompts re-entry
                employ_num = int(input("\tRe-enter employee number (0 to quit): "))
        # Validates positive decimals less than or equal to gross
        else:
            # Updates total withholdings
            total_withheld += withholdings
            
            '''NET PAY'''
            # Calculates employee's pay after withholdings
            net_pay = (gross_pay - withholdings)
            # Updates total net pay
            total_net += net_pay
            
            '''RE-ITERATIONS'''
            print() # Blank space
            # Begins next payroll record
            print("Processing next employee:")
            print () # Blank line
            # Proceeds to 2nd stage, prompts re-entry, or terminates
            employ_num = int(input("\tEmployee number (0 to quit): "))

            '''RE-VALIDATION'''
            # Checks for negative value within main loop
            while (employ_num < 0):
                # Reports error message
                print("\tERROR: Invalid entry.")
                # Prompts re-entry
                employ_num = int(input("\tRe-enter employee number (0 to quit): "))

    '''TERMINATION'''
    # Checks for terminal value at any point
    while (employ_num == 0):
        print() # blank line
        # Begins input validation
        print("Creating weekly payroll report:")
        print() #Blank line
        # Checks for missing data
        if (gross_pay == 0):
            # Reports error message
            print("\tERROR: Missing data.")
        # Checks payroll totals for all employees
        else:
            # Reports counter-variable values 
            print(f"\tTotal gross pay: ${total_gross}")
            print(f"\tTotal federal tax: ${total_fed}")
            print(f"\tTotal state tax: ${total_state}")
            print(f"\tTotal FICA: ${total_fica}")
            print(f"\tTotal withholdings: ${total_withheld}")
            print(f"\tTotal net pay: ${total_net}")
        break # Quits loop

main()

'''
SAMPLE RUN A: IMMEDIATE QUIT

Please enter the following:

    Employee number (0 to quit): 0

Creating weekly payroll report:

    ERROR: Missing data.

SAMPLE RUN B: NORMAL MODE

Please enter the following:

    Employee number (0 to quit): 1
    Gross pay: $1000
    Federal withholding: $10
    State withholding: $10
    FICA withholding: $10

Processing next employee:

    Employee number (0 to quit): 2
    Gross pay: $2000
    Federal withholding: $20
    State withholding: $20
    FICA withholding: $20

Processing next employee:

    Employee number (0 to quit): 3
    Gross pay: $3000
    Federal withholding: $30
    State withholding: $30
    FICA withholding: $30

Processing next employee:

    Employee number (0 to quit): 0

Creating weekly payroll report:

    Total gross pay: $6000.0
    Total federal tax: $60.0
    Total state tax: $60.0
    Total FICA: $60.0
    Total withholdings: $180.0
    Total net pay: $5820.0

SAMPLE RUN C: ALL NEGATIVE

Please enter the following:

    Employee number (0 to quit): -1
    ERROR: Invalid entry.
    Re-enter employee number (0 to quit): 1
    Gross pay: $-1000
    ERROR: Invalid entry.
    Re-enter gross pay: $1000
    Federal withholding: $-10
    ERROR: Invalid entry.
    Re-enter federal withholding: $10
    State withholding: $-10
    ERROR: Invalid entry.
    Re-enter state withholding: $10
    FICA withholding: $-10
    ERROR: Invalid entry.
    Re-enter FICA withholding: $10

Processing next employee:

    Employee number (0 to quit): -2
    ERROR: Invalid entry.
    Re-enter employee number (0 to quit): -3
    ERROR: Invalid entry.
    Re-enter employee number (0 to quit): 0

Creating weekly payroll report:

    Total gross pay: $1000.0
    Total federal tax: $10.0
    Total state tax: $10.0
    Total FICA: $10.0
    Total withholdings: $30.0
    Total net pay: $970.0

SAMPLE RUN D: INVALID RESULTS

Please enter the following:

    Employee number (0 to quit): 4
    Gross pay: $8
    Federal withholding: $3
    State withholding: $3
    FICA withholding: $3
    ERROR: Invalid withholdings result.

Please try again:

    Re-enter employee number (0 to quit): 4
    Gross pay: $89
    Federal withholding: $3
    State withholding: $3
    FICA withholding: $3

Processing next employee:

    Employee number (0 to quit): -5
    ERROR: Invalid entry.
    Re-enter employee number (0 to quit): 5
    Gross pay: $890
    Federal withholding: $890
    State withholding: $890
    FICA withholding: $890
    ERROR: Invalid withholdings result.

Please try again:

    Re-enter employee number (0 to quit): 0

Creating weekly payroll report:

    Total gross pay: $89.0
    Total federal tax: $3.0
    Total state tax: $3.0
    Total FICA: $3.0
    Total withholdings: $9.0
    Total net pay: $80.0
'''

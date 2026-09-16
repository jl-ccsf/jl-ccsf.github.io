> Due Monday 11:59pm  
> Available Jun 2 - Jun 26
> 100 points

Write a program that displays a weekly payroll report. **Use a loop to ask the user for the employee number, gross pay, state tax, federal tax, and FICA withholdings.** The loop will **terminate when 0 is entered for the employee number**.

After the data is entered, the program should **display totals for gross pay, state tax, federal tax, FICA withholdings, and net pay.**

Your program file should be called `payroll_report.py`.

# Input

- **Do not accept negative numbers** for any of the items entered.
- **Do not accept values** for state, federal, or FICA **withholdings greater than the gross pay.**
- **If the sum of withholdings** for any employee **is greater than gross pay, print an error message** and **ask the user to re-enter the data** for that employee.

## Pseudocode
1. Prompt user to input `employ_num`, `gross_pay`, `fed_tax`, `state_tax`, and `fica`
2. Loop prompts for next employee pay record(s)
3. Calculate employee `withholdings` (taxes + FICA)
4. Check for positive net pay (gross pay - withholdings >= 0)
5. Produce error messages for negative input and prompt for re-entry
6. Compute `total_gross_pay`, `total_fed_tax`, `total_state_tax`, `total_fica`, and `total_net_pay`
7. Display total results

## Sections
- User Prompt Loop:
	- First employee: `Please enter the following:`
	- Next employee(s): `Processing next employee:`
	- Error messages 1-6: `Please re-enter the data for this employee.`
- Calculations:
	- `withholdings`
	- `net_pay`
	- `total_gross`
	- `total_fed`
	- `total_state`
	- `total_fica`
	- `total_withholdings`
	- `total_net`
- Totals: `Weekly payroll report:`

## User Prompts

```
# USER PROMPTS
# Displays prompt message without input
print("Please enter the following:")
# Prompts user for employee payroll info
employ_num = int(input("Employee Number (0 to quit): ")) # saves employee number as integer to check for negatives
gross_pay = float(input("Gross pay: $")) # saves pay before withholdings as decimal
fed_tax = float(input("Federal withholding: $")) # saves federal taxes withheld as decimal
state_tax = float(input("State withholding: $")) # saves state taxes withheld as decimal
fica = float(input("FICA withholding: $")) # saves FICA withheld as decimal
# Calculates combined withholdings
withholdings = fed_tax + state_tax + fica # negative results in error msg
# Calculates and displays pay after withholdings
net_pay = gross_pay - withholdings # negative results in error msg
print("Net pay: $" str(net_pay)) # converts float to string
```

## Loop

```
# LOOP
# This will be a loop after I finish the lecture
```

## Error Messages

```
# ERROR MESSAGES
# employ_num < 0
print("ERROR: Employee number cannot be less than zero."/n
"Please re-enter the data for this employee.")
# gross_pay < 0
print("ERROR: Gross pay cannot be less than zero."/n
"Please re-enter the data for this employee.")
# fed_tax < 0
print("ERROR: Federal withholding cannot be less than zero."/n
"Please re-enter the data for this employee.")
# state_tax < 0
print("ERROR: State withholding cannot be less than zero."/n
"Please re-enter the data for this employee.")
# fica < 0
print("ERROR: FICA withholding cannot be less than zero."/n
"Please re-enter the data for this employee.")
# withholdings < 0
print("ERROR: Withholdings cannot exceed gross pay."/n
"Please re-enter the data for this employee.")
# net_pay < 0
print("ERROR: Net pay cannot be less than zero."/n
"Please re-enter the data for this employee.")
```

## Calculations

```
# CALCULATIONS
# gross pay of all employees
total_gross =
# federal tax of all employees
total_fed = 
# state tax of all employees
total_state = 
# FICA withholdings of all employees
total_fica = 
# combined withholdings of all employees
total_withholdings = total_fed + total_state + total_fica
# net pay of all employees
total_net = total_gross - total_withholdings
```

## Report
```
# TOTALS
print("Weekly payroll report:")
	print("Total gross pay: $" total_gross)
	print("Total federal tax: $" total_fed)
	print("Total state tax: $" total_state)
	print("Total FICA: $" total_fica)
	print("Total net pay: $" total_net)
```

# Output

## Sample Run A:

```
'''
# SAMPLE RUN A

Please enter the following:
	Employee number (0 to quit): 7643 
	Gross pay: 2000 
	Federal withholding: 500.00 
	State withholding: 350.00 
	FICA withholding: 2000.00 
		ERROR: Withholdings cannot exceed gross pay. 
		Please re-enter the data for this employee. 
	Employee number (0 to quit): 7643 
	Gross pay: -2300.00
		ERROR: Gross pay canot be less than zero.
		Please re-enter the data for this employee.
	Gross pay: 2600.00
	Federal Withholding: 50.00 
	State withholding: -40.00 
		ERROR: State withholding cannot be less than zero.
		Please re-enter the data for this employee.
	State withholding: 40.00 
	FICA withholding: 50.00 

Processing next employee: 
	Employee number (0 to quit): -2345 
		ERROR: Employee number cannot be less than zero.
		Please re-enter the data for this employee.
	Employee number (0 to quit): 2345 
	Gross pay: 4000.00
	Federal withholding: 250.00
	State withholding: 50.00
	FICA withholding: 65.00

Processing next employee:
	Employee number (0 to quit): 0

Weekly payroll report:
	Total gross pay: $6600.00 
	Total federal tax: $300.00
	Total state tax: $90.0
	Total FICA witholding: $115.00 
	Total net pay: $6095.00
'''
```

## Sample Run B:

```
'''
# SAMPLE RUN B

Enter the following information:
	Employee number (0 to quit): 7865
	Gross pay: 4000.00
	Federal withholding: 345.00
	State withholding: 50.00
	FICA withholding: 34.00

Processing next employee:
	Employee Number (0 to quit): -9876
		ERROR: Employee number cannot be less than zero.
		Please re-enter the data for this employee.
	Employee number (0 to quit): 9876
	Gross pay: 2000
	Federal withholding: 500.00
	State withholding: 1000.00
	FICA withholding: 600.0
		ERROR: Withholdings cannot exceed gross pay.
		Please re-enter the data for this employee.
	Employee number (0 to quit): 9876
	Gross pay: 5000.00
	Federal withholding: 400.00
	State withholding: 200.00
	FICA withholding: 75.00

Processing next employee:
	Employee number (0 to quit): 0

Weekly payroll report:
	Total gross pay: $9000.00
	Total federal tax: $745.00
	Total state tax: $250.00
	Total FICA withholding: $109.00
	Total net pay: $7896.00
'''
```

# Documentation

Write a documentation comment at the top of the program which indicates its purpose, your name, and today’s date. For example:

```
'''
PROGRAM: payroll_report.py
PROGRAMMER: Jules Lenzi
COURSE: CS-131B
DATE: 06/22/2026
DESCRIPTION: Displays a total weekly pay report for multiple employees. Produces error messages for negative results and prompts for data re-entry. All amounts are in USD.
'''
```

# Submission

1.  Include the standard program header at the top of your Python file.
2.  Execute the program and copy/paste the output into the bottom of the source code file as a comment. (I will run the programs myself to see the output.)
3.  Make sure the run matches your source. If the run you submit could not have come from the source, it will be graded as if you did not hand in a run.
4.  Submit the `payroll_report.py` file before the due date.
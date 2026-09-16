'''
e1_zoo.py
jl-ccsf
06/12/2026
CS-131B, Prof. Ibrahim
Calculates the total food consumed by polar bears each month in kilograms.
'''

def main():

    # Assigns user input to variables
    number_of_bears = int(input("Enter the number of polar bears: "))
    daily_ration = float(input("Enter the daily food ration per bear: "))

    # Calcultes total food consumed per month
    total_food = number_of_bears * daily_ration * 30

    # Displays result
    print() # Blank line
    print(f"The food consumed is {total_food:,.1f} kg.")

main()

'''
SAMPLE RUN

Enter the number of polar bears: 10
Enter the daily food ration per bear: 40

The food consumed is 12,000.0 kg.
'''

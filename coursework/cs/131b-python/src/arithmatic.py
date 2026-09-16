'''
d1_arithmetic.py
jl-ccsf
06/12/2026
CS-131B, Prof. Ibrahim
Demonstrates basic addition, subtraction, multiplication, and division methods.
'''

def main():

    # Assigns integers to variables
    num_1 = int(input("Enter a large number: "))
    num_2 = int(input("Enter a small number: "))

    # Calculates sum, difference, product, and quotient
    sum = num_1 + num_2
    diff = int(num_1 - num_2)
    prod = num_1 * num_2
    quot = int(num_1 / num_2)

    # Formats and displays results
    print() # Blank line
    print(f"{num_1} + {num_2} = ", sum)
    print(f"{num_1} - {num_2} = ", diff) 
    print(f"{num_1} * {num_2} = ", prod)
    print(f"{num_1} / {num_2} = ", quot)

main()

'''
SAMPLE RUN

Enter a large number: 15
Enter a small number: 4

15 + 4 =  19
15 - 4 =  11
15 * 4 =  60
15 / 4 =  3
'''

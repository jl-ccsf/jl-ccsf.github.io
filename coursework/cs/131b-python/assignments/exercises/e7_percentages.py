'''
e7_percentages.py
jl-ccsf
07/26/2026
CS-131B, Prof. Ibrahim
Reads all file values, calculates their sum, and validates the result.
'''

# Defines constants
ERROR = "ERROR: Sum cannot be <= 0.0"
INVALID = "INVALID: Sum cannot be < 99.9 or > 100.1"

# Imports system module fuctions
import sys

def main():

    # Tests file
    try:
        # Opens input file to read
        election_results = open("percentages.txt", "r")
    except FileNotFoundError:
       # Displays error message
       print("File not found. Program aborted.")
       sys.exit()

    # Displays file contents
    read("percentages.txt")
    # Displays list of line values
    data = process(election_results)

    # Calculates sum
    sum = calculate(data)

    # Validates result
    valid = validate(sum)
    # Assigns result string to variable
    result = f"The sum of all values in {election_results} is {sum}."

    # Displays result and validation message
    if valid == True:
        print(f"{result}\nThis falls within the acceptable range.")
    else:
        print(f"{result}\nThis is not within the acceptable range.")

    # Closes file
    election_results.close()

'''Reads file'''
def read(file):
    contents = file.read()
    file.close()
    # Displays contents
    print(f"Contents of {file}: {contents}")
    return contents

'''Saves line values to list'''
def process(file):
    data = []
    count = 0
    for line in file:
        value = float(file.readline())
        data.append(value)
        count += 1
    # Displays data
    print(f"{count} values found: {data}")
    return data

'''Calculates sum of list values'''
def calculate(data):
    sum = 0.0
    for item in list:
        sum += float(data[item])
    return sum

'''Validates sum'''
def validate(sum):
    if (sum == 0.0) or (sum <= 0.1):
        valid = False
        # Displays error message
        print(ERROR)
    elif (sum >= 0.1):
        if (sum not in range(99.9, 100.1)):
            valid = False
            # Displays error message
            print(INVALID)
        else:
            valid = True
    return valid

main()

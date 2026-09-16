'''
d8_palidrome.py
jl-ccsf
07/31/2026
CS-131B, Prof. Ibrahim
Validates whether user input is a palindrome.
'''

def main():

    # Assigns user values
    min  = int(input("Enter a minimum word limit: "))
    max = int(input("Enter a maximum word limit: "))
    words = input(f"Enter {min} to {max} words: ")

    # Splits words into tuple sequence
    words_tuple = tuple(words.split(" "))

    # Displays results
    print() # Blank line
    print(f"Is \"{words}\" a palindrome?")
    print(is_pal(words_tuple))

'''Determines if tuple is the same read backwards to forwards'''
def is_pal(tuple):
    return is_pal_helper(tuple, 0, (len(tuple) - 1))

'''Determines if tuple length is within the specified range'''
def is_pal_helper(tuple, min, max):
    if max <= min:
        return True
    elif tuple[min] != tuple[max]:
        return False
    else:
        return is_pal_helper(tuple, (min + 1), (max - 1)) 

main()

'''
SAMPLE RUN A: TRUE

Enter a min word limit: 2
Enter a max word limit: 10
Enter 2 to 10 words: eye eye

Is "eye eye" a palindrome?
True

SAMPLE RUN B: FALSE

Enter a min word limit: 2
Enter a max word limit: 10
Enter 2 to 10 words: eye see you

Is "eye see you" a palindrome?
False
'''
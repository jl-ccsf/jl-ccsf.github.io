'''
d2_reverse.py
jl-ccsf
06/12/2026
CS-131B, Prof. Ibrahim
Assigns 3 types of variables from input and displays them in reverse order.
'''

def main():

    # Assigns input without prompting 
    k = int(input())
    d = float(input())
    s = str(input())

    print() # Blank line
    # Displays values in reverse order
    print(s,d,k)
    # Displays values in original order
    print(k,d,s)

main()

'''
SAMPLE RUN A

1
2
3

3 2.0 1
1 2.0 3

SAMPLE RUN B

3
2.5
one

one 2.5 3
3 2.5 one
'''

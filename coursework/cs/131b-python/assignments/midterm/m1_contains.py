'''
m1_contains.py
jl-ccsf
07/10/2026
CS-131B, Prof. Ibrahim
Checks if one list contains iterations of another.
'''

def main():

    # Defines lists to check
    list1 = [1, 6, 2, 1, 4, 1, 2, 1, 8]
    list2 = [1, 2, 1]

    # Displays True/False
    print("Does first list contain second list?")
    print() # Blank line
    print(contains(list1,list2))

'''Determines if first list contains second list'''
def contains(a1, a2):
    # Counts iterations in range
    for i in range(len(a1) - len(a2) + 1):
        # Confirms list 1 contains iterations of list 2
        found = True
        # Counts iterations in range
        for j in range(len(a2)):
            # Checks list 1 index is not list 2's
            if a1[i + j] != a2[j]:
                # Confirms iterations not found in list 1
                found = False
        # Confirms iterations found in list 2
        if found:
            # Found
            return True
    # Not found
    return False

main()

'''
SAMPLE RUN

Does first list contain second list?

True
'''

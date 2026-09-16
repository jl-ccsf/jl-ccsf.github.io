'''
p5_schedule.py
jl-ccsf
07/10/2026
CS-131B, Prof. Ibrahim
Generates a round-robin schedule for a list of participants. Returns a list of 
tuples, each of which contains a pair of names. If the list is odd, one 
participant is paired with a null value.
'''

def main():

    # Demonstrates even and odd sample lists
    even_schedule = generate_schedule(["A", "B", "C", "D", "E", "F", "G", "H"])
    odd_schedule = generate_schedule(["A", "B", "C", "D", "E", "F", "G"])

    # Displays sample schedules
    print(f"SAMPLE RUN A: EVEN\n{even_schedule}")
    print() # Blank line
    print(f"SAMPLE RUN B: ODD\n{odd_schedule}")

'''Generates new rounds and matches'''
def generate_schedule(participants):
    # Establishes starting round's order
    list_copy = get_copy(participants)
    # Checks list for odd items
    if get_even(list_copy) != True:
        # Adds null item to list copy
        list_copy.append("Bye!")
    # Estabishes starting round's pairs
    schedule = [get_matches(list_copy)]
    # Generates subsequent rounds
    for i in range(int(len(list_copy) - 2)):
        # Generates unique order per round
        list_copy = get_round(list_copy)
        # Generates unique pairings per round
        matches = get_matches(list_copy)
        schedule.append(matches)
    return schedule

'''Duplicates list'''
def get_copy(participants):
    copy = list(participants)
    return copy

'''Validates number of list items'''
def get_even(participants):
    # Checks for even length
    if (len(participants) % 2) == 0:
        # Confirms items are even
        even = True
    # Checks for odd length
    else:
        # Confirms items are odd
        even = False
    return even

'''Generates unique order for each subsequent round'''
def get_round(participants):
    index = 0
    round = [participants[index]] + [participants[len(participants) - 1]]
    for i in range(int(len(participants) - 2)):
        index += 1
        middle = participants[index]
        round.append(middle)
    return round

'''Generates unique pairings for each round'''
def get_matches(participants):
    index = 0
    matches = [(participants[index], participants[-(index) - 1])]
    for i in range(int((len(participants) / 2) - 1)):
        index += 1
        pair = (participants[index], participants[-(index) - 1])
        matches.append(pair)
    return matches

main()

'''
SAMPLE RUN A: EVEN

[[('A', 'H'), ('B', 'G'), ('C', 'F'), ('D', 'E')], 
[('A', 'G'), ('H', 'F'), ('B', 'E'), ('C', 'D')], 
[('A', 'F'), ('G', 'E'), ('H', 'D'), ('B', 'C')], 
[('A', 'E'), ('F', 'D'), ('G', 'C'), ('H', 'B')], 
[('A', 'D'), ('E', 'C'), ('F', 'B'), ('G', 'H')], 
[('A', 'C'), ('D', 'B'), ('E', 'H'), ('F', 'G')], 
[('A', 'B'), ('C', 'H'), ('D', 'G'), ('E', 'F')]]

SAMPLE RUN B: ODD

[[('A', 'Bye!'), ('B', 'G'), ('C', 'F'), ('D', 'E')], 
[('A', 'G'), ('Bye!', 'F'), ('B', 'E'), ('C', 'D')], 
[('A', 'F'), ('G', 'E'), ('Bye!', 'D'), ('B', 'C')], 
[('A', 'E'), ('F', 'D'), ('G', 'C'), ('Bye!', 'B')], 
[('A', 'D'), ('E', 'C'), ('F', 'B'), ('G', 'Bye!')], 
[('A', 'C'), ('D', 'B'), ('E', 'Bye!'), ('F', 'G')], 
[('A', 'B'), ('C', 'Bye!'), ('D', 'G'), ('E', 'F')]]
'''

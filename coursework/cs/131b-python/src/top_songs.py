'''
e4_top_songs.py
jl-ccsf
07/01/2026
CS-131B, Prof. Ibrahim
Displays songs and artists from lists using rows and columns format loop.
'''

def main():

    # Defines constants
    ROWS = 5 # songs
    COLS = 2 # artists

    # Creates 2D list
    top_songs = [["Bohemian Rhapsody", "Queen"],
                    ["Stairway to Heaven", "Zeppelin"],
                    ["Imagine", "Lennon"],
                    ["Hotel California", "Eagles"],
                    ["Sounds of Silence", "Simon and Garfunkel"]]

    # Iterates thru rows
    for ROWS in top_songs:
        print()
        # Iterates thru coloumns
        for COLS in ROWS:
            # Displays songs and artists
            print(COLS)

main()

'''
SAMPLE RUN

Bohemian Rhapsody
Queen

Stairway to Heaven
Zeppelin

Imagine
Lennon

Hotel California
Eagles

Sounds of Silence
Simon and Garfunkel
'''

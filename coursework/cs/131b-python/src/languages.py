'''
e6_languages.py
jl-ccsf
07/14/2026
CS-131B, Prof. Ibrahim
Writes programming languages, creators, and IDE to file.
'''

def main():

    # Assigns number of languages
    num = int(input("How many programming languages do you want to learn? "))

    # Opens file to write
    in_file = open("programming_languages.txt", "w")

    # Assigns language, creator, and IDE from input
    for count in range(1, num + 1):
        # Assigns language data
        print(f"Enter data for programming language {count}:")
        lang = input("Language: ")
        creator = input("Creator: ")
        ide = input("IDE: ")
        # Writes language name and newline to file
        in_file.write(f"{lang}\n")
        # Writes creator name and newline to file
        in_file.write(f"{creator}\n")
        # Writes IDE and 2 newlines to file
        in_file.write(f"{ide}\n\n")
        # Displays blank line
        print()  

    # Closes file
    in_file.close()

    # Displays confirmation message
    print("Programming language records written to programming_languages.txt")

main()

'''
SAMPLE RUN

How many programming languages do you want to learn? 2

Enter data for language 1:
Language: Python
Creator: vanRossum
IDE: IDLE

Enter data for language 2:
Language: Java
Creator: Gosling
IDE: GCC


Programming language records written to programming_languages.txt:
Python
vanRossum
IDLE

Java
Gosling
GCC
'''

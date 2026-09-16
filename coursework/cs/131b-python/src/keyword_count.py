'''
e5_keyword_count.py
jl-ccsf
CS-131B, Prof. Ibrahim
07/15/2026
Counts occurences of Python keywords in file.
'''

def main():

    # Stores keywords in set
    keywords = {"and", "del", "from", "not", "while", "as", "elif", "global", 
                "or", "with", "assert", "else", "if", "pass", "yield", "break", 
                "except", "import", "print", "class", "exec", "in", "raise", 
                "continue", "finally", "is", "return", "def", "for", "lambda", 
                "try"}

    # Saves input to file
    file_name = input("Enter Python source code: ").strip()
    # Opens file to read
    input_file = open(file_name, "r")
    # Creates empty dictionary
    word_counts = {}
    # Tests each line in file
    for line in input_file:
        # Converts each line to lowercase
        process_line(line.lower(), word_counts)
    #Closes file
    input_file.close()

    # Retrieves key-value pairs
    pairs = list(word_counts.items())
    # Collects pairs into items
    items = [[count, word] for (word, count) in pairs]
    # Sorts in reverse order
    items.sort(reverse = True)

    # Slices and displays first 10 items
    for count, word in items [ : 10]:
        # Blank space
        print()
        # Formats and displays results
        print(word, count, sep = ":")
        
'''Counts each word in line'''
def process_line(line, word_counts):
    # Replaces punctuation with space
    line = replace_punctuation(line)
    # Splits line into words
    words = line.split()
    # Iterates over each word
    for word in words:
        # Tests for keywords
        if word in word_counts:
            # Increases counter
            word_counts[word] += 1
        else:
            # Adds item to dictionary
            word_counts[word] = 1

'''Replaces punctuation with space'''
def replace_punctuation(line):
    # Iterates over each character
    for ch in line:
        # Identifies punctuation
        if ch in "=:":
            # Replaces symbols with space
            line = line.replace(ch, " ")
    # Saves new line
    return line

main()

'''
SAMPLE RUN

Enter Python source code: if x == 2: while if for else if while for

else: 1
for: 2
if: 3
while: 2
'''

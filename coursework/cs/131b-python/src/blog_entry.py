'''
p4_blog_entry.py
jl-ccsf
CS-131B, Prof. Ibrahim
07/01/2026
Gets user's name, blog entry, and key character. Produces a 10-word summary and 
a masked character string. Validates input against constant character limits.
'''

# Defines character limits
MIN = 1
NAME_MIN = MIN * 2
STRING_MIN = MIN * 100
MAX = MIN * 500

# Defines output messages
INSTRUCTIONS = (f"Please use {NAME_MIN} or more characters for your username.\n\
                Blog entries must be between {STRING_MIN} and {MAX} words.\n\
                Key characters are {MIN} letter and case-sensitive.")
ERROR = (f"ERROR: Invalid input.")

def main():

    # Displays character limits
    print(INSTRUCTIONS)
    print() # blank line

    # Assigns input to username
    username = get_username()
    # Assigns input to text
    text = get_text()
    # Assigns input to key
    key = get_key()
    print() # blank line

    # Assigns first ten words to summary
    summary = get_summary(text)
    # Displays ten-word summary
    print(summary)
    # Replaces key in text with masked character
    mask_text = mask_key(text, key)
    # Displays text with asterisks replacing key
    print(mask_text)
    # Assigns key character count, displays result
    key_count = count_key(text, key)

'''Requests username, validates name character limit'''
def get_username():

    # Assigns input to name
    username = input("Username: ")

    # Checks name for 0 chars or over 500
    while valid_chars(username) == False:
        # Displays error, prompts re-entry
        username = input("Username: ")
    # Checks name for 1 to 500 chars
    while valid_chars(username) == True:
        # Checks name for less than 2 chars
        if (count_chars(username) < NAME_MIN):
            # Confirms name is 1 char
            valid = False
            # Reports invalid input
            print(ERROR)
            # Prompts re-entry
            username = input("Username: ")
        else:
            # Confirms name is 2 to 500 chars
            valid = True
            # Saves string value to username
            return username
        
'''Validates input against minimum and maximum character limits'''
def valid_chars(string):
    # Checks string for less than 1 or more than 500 chars
    if (count_chars(string) < MIN) or (count_chars(string) > MAX):
        # Confirms string exceeds limits
        valid = False 
        # Reports invalid input
        print(ERROR)
    else:
        # Declares string is more than 1 and less than 500 chars
        (count_chars(string) > MIN) and (count_chars(string) < MAX)
        # Confirms string meets limits
        valid = True
    # Saves Boolean value
    return valid

'''Counts characters and returns result'''
def count_chars(string):
    # Stores string length
    char_count = len(string)
    # Saves integer value
    return char_count 

'''Requests blog entry, validates string character limits'''
def get_text():

    # Assigns input to string
    string = input("Blog entry: ")

    # Confirms string is 0 chars or over 500
    while valid_chars(string) == False:
        # Displays error, prompts re-entry
        string = input("Blog entry: ") 
    # Confirms string is 1 to 500 chars
    while valid_chars(string) == True:
        # Checks string for less than 100 chars
        if (count_chars(string) < STRING_MIN):
            # Confirms string fails limit
            valid = False
            # Reports invalid input
            print(ERROR)
            # Prompts re-entry
            string = input("Blog entry: ")
        else:
            # Confirms string is 100-500 chars
            valid = True
            # Saves string value to text
            return string

'''Requests key characters, validates key character limit'''
def get_key():

    # Assigns input to char
    char = input("Key character: ")

    # Checks char against limit
    while count_chars(char) != MIN:
        # Confirms char is not 1 char
        valid = False
        # Reports invalid input
        print(ERROR)
        # Prompts re-entry
        char = input("Key character: ")
    # Checks char meets limit
    if count_chars(char) == MIN:
        # Confirms char is 1 char
        valid = True
        # Saves string value to key
        return char

'''Pulls first ten words from string'''
def get_summary(string):
    # Splits string into space-deliniated list
    word_list = string.split()
    # Combines items into space-seperated string
    first_ten_words = " ".join(word_list[slice(10)])
    # Assigns string value to summary
    return first_ten_words

'''Replaces each instance of char in string with asterisk'''
def mask_key(string, char):
    # Assigns modified string to variable
    mask_string = string.replace(char,"*")
    # Saves string value to mask_text
    return mask_string

'''Counts each instance of char in string'''
def count_key(string, char):

    # Sets counter variable
    char_count = 0
    # Searches string for instances
    for ch in string:
        # Identifies variable to count
        if ch == char:
            # Adds each instance to counter
            char_count += 1

    # Displays result
    print(f"{char} appears {char_count} times.")

    # Saves integer value to key_count
    return char_count

main()

'''
SAMPLE RUN A: VALID INPUT

Please use 2 or more characters for your username. 
Blog entries must be between 100 and 500 words. 
Key characters are 1 letter and case-sensitive.

Username: jl-ccsf
Blog entry: Here are the first ten words of the blog entry. 
Here are the first twenty words of the blog entry. 
Here are the first thirty words ofthe blog entry. 
Here are the first forty words of the blog entry. 
Here arethe first fifty words of the blog entry. 
Here are the first sixty words ofthe blog entry. 
Here are the first seventy words of the blog entry. 
Here are the first eighty words of the blog entry. 
Here are the first ninety words of the blog entry.
Key character: e

Here are the first ten words of the blog entry.
H*r* ar* th* first t*n words of th* blog *ntry. 
H*r* ar* th* first tw*nty words of th* blog *ntry. 
H*r* ar* th* first thirty words ofth* blog *ntry. 
H*r* ar* th* first forty words of th* blog *ntry. 
H*r* ar*th* first fifty words of th* blog *ntry. 
H*r* ar* th* first sixty words ofth* blog *ntry. 
H*r* ar* th* first s*v*nty words of th* blog *ntry. 
H*r* ar* th* first *ighty words of th* blog *ntry. 
H*r* ar* th* first nin*ty words of th* blog *ntry.
e appears 60 times.

SAMPLE RUN B: INVALID INPUT

Please use 2 or more characters for your username. 
Blog entries must be between 100 and 500 words. 
Key characters are 1 letter and case-sensitive.

Username: j
ERROR: Invalid input.
Username: jl
Blog entry: Here are the first ten words of the blog entry. 
Here are the first twenty words of the blog entry. 
Here are the first thirty words ofthe blog entry. 
Here are the first forty words of the blog entry. 
Here arethe first fifty words of the blog entry. 
Here are the first sixty words ofthe blog entry. 
Here are the first seventy words of the blog entry. 
Here are the first eighty words of the blog entry. 
Here are the first ninety words of the blog entry. 
Here are the first hundred words of the blog entry, 
which put it at over 500 characters.
ERROR: Invalid input.
Blog entry: Here are the first ten words of the blog entry. 
Here are the first twenty words of the blog entry. 
Here are the first thirty words ofthe blog entry. 
Here are the first forty words of the blog entry. 
Here arethe first fifty words of the blog entry. 
Here are the first sixty words ofthe blog entry. 
Here are the first seventy words of the blog entry. 
Here are the first eighty words of the blog entry. 
Here are the first ninety words of the blog entry.                            
Key character: ee
ERROR: Invalid input.
Key character: e

Here are the first ten words of the blog entry.
H*r* ar* th* first t*n words of th* blog *ntry. 
H*r* ar* th* first tw*nty words of th* blog *ntry. 
H*r* ar* th* first thirty words ofth* blog *ntry. 
H*r* ar* th* first forty words of th* blog *ntry. 
H*r* ar*th* first fifty words of th* blog *ntry. 
H*r* ar* th* first sixty words ofth* blog *ntry. 
H*r* ar* th* first s*v*nty words of th* blog *ntry. 
H*r* ar* th* first *ighty words of th* blog *ntry. 
H*r* ar* th* first nin*ty words of th* blog *ntry.
e appears 60 times.
'''

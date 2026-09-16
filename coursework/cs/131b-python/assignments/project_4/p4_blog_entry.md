> Due June 29

Write a program called `blog_entry` that could be used to store a blog entry for a Web log. The program has variables to store the poster’s username and text of the blog entry.

In this project, you will write a function that returns the first 10 words from the text (or the entire text if it is less than 10 words).

You must write the functions below from scratch. Do not rely on any other built-in or pre-existing functions that appear to provide any of this functionality for you.

```
# Function formula
def name (parameters):  
    statements  
    return something # optional
```

# Instructions

## Step 1 - Define Function `get_user_name()`

Create a function called: `get_user_name()`

This function requests the `user_name` from the user and continues to ask for it until the user gets it right. This function will test to make sure the user only types a string that has at least 2 characters. Make this minimum size a constant, and use that symbolic constant, not the literal (2) wherever it is needed. This function will take no parameter and return a `user_name.`

## Step 2 - Define Function `get_text()`

Create a function called: `get_text()`

This function has no parameters and return a new string that has the blog entry. This function requests a string from the user and continues to ask for it until the user gets it right. Also, this function will test to make sure the user only types a string that has at least 100 characters and less than 500 characters. Make this minimum size a constant, and use that symbolic constant, not the literal (100 or 500) wherever it is needed.

## Step 3 - Define Function `get_key_character()`

Create a function called: `get_key_character()`

This function requests a single character from the user and continues to ask for it until the user gets it right. Also, this function will test to make sure the user only types one single character; 0, 2, 3 or more characters will be flagged as an error and the function will keep prompting the user until just one character is typed.

## Step 4 - Define Function `first_ten_words(the_string)`

Create a function called: `first_ten_words(the_string)`

The function will return the first ten words of the `blog_entry`. It works by using the index of a space and it remembers where the previous space was located to extract the text between the previous space and the current space (i.e. the current word). This is repeated ten times. This function will take `the_string` as a parameter and return a new string that is at most the first ten words of `the_string`.

## Step 5 - Define Function `mask_character(the_string, key_character)`

Create a function called: `mask_character(the_string, key_character)`

This function will take both a string and a character as parameters and return a new string that has each occurrence of the key character replaced by an asterisk (`*`).

## Step 6 - Define Function `count_Key(the_string, key_character)`

Create a function called: `count_key(the_string, key_character)`

This function will take both a string and a character as parameters and return the number of key characters that appear in the string (case-sensitive).

## Step 7 - Define Function `main()`

Create a function called: `main()`

This function does the following sequentially:

1.  Calls `get_user_name()` and stores the return value in the variable `user_name`.
2.  Calls `get_text()` and stores the return value in the variable `the_text`.
3.  Calls `get_key_character()` and stores the return value in the variable `key_character`.
4.  Calls `first_ten_words(the_string)` with the parameter `the_text` and stores the return value in the variable `text_summary`.
5.  Calls `mask_character(the_string, key_character)` with the parameters `the_text` and `key_character` and stores the return value in the variable `new_string`.
6.  Calls `count_key()` and stores the return value in the variable `num_keys`.

## Step 8 - Call `main()` Function

Now, call the `main()` function.

### Input Errors

Whenever the user makes an input error, continue prompting the user until they submit a correct input. Do not return from an input function until you have acquired a legal value.

### Test Run Requirements

Submit at least **two runs.** In at least one of the two runs, intentionally commit input errors to demonstrate both kinds of illegal input described above.

Your program should be called `blog_entry.py`

### Sample Run

Here is an example of what running your program might look like (text entered by the user is in bold):

```
'''
Enter username >= 2 characters: H  
Please enter username >= 2 characters: Hanan
Please enter a text >= 100 and <= 500 characters: sdff 
Please enter a text or sentence >= 100 and <= 500 characters: Whether computer science is one of your college courses or just something of casual interest. 
Please enter a text or sentence >= 100 and <= 500 characters: Whether computer science is one of your college courses or just something of casual interest, this blog post is dedicated to you. Detailing 30 of the best computer science blogs, this list is a place to start; continue your own education and find enriching, intriguing topics related to this rapidly changing discipline, no matter your level of experience or your background.
Please enter a SINGLE character to act as key: c 
The first ten words of the blog_entry as a summary of the entry:  
Whether computer science is one of your college courses or  
String with key character, 'c' masked:  
Whether *omputer s*ien*e is one of your *ollege *ourses or just something of *asual interest, this blog post is dedi*ated to you. Detailing 30 of the best *omputer s*ien*e blogs, this list is a pla*e to start; *ontinue your own edu*ation and find enri*hing, intriguing topi*s related to this rapidly *hanging dis*ipline, no matter your level of experien*e or your ba*kground.  
# of occurrences of key character, 'c': 19
'''
```

# Submission Instructions

1.  Include the standard program header at the top of your Python files.
2.  Execute the program and copy/paste the output that is produced by your program into the bottom of the source code file, making it into a comment. (I will run the programs myself to see the output.)
3.  Make sure the run "matches" your source. If the run you submit could not have come from the source you submit, it will be graded as if you did not hand in a run.
4.  Submit the `blog_entry.py` file.
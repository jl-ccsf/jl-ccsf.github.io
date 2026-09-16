> Due **July 6**

This can be applied to a number of scenarios:

- Say you are organizing an academic conference, and you want to schedule each attendee to have a one-on-one meeting with each other attendee.
- Or, say you are organizing a sports tournament, and you need to schedule games such that each participant plays each other participant exactly once.
- Or, say you are teaching a writing class, and you'd like each student to review each other student's draft exactly once during the semester.

The function you write will have one parameter - a list of strings, each of which is a name - and will return a list of tuples, where each tuple is a pair of names.

# Instructions

## Step 1 - Make your function

Write a function that has one parameter. The function **must** be called:

`generate_round_robin_schedule()`

The first thing you should do in your function is create a new list that is a copy of your parameter. If your parameter is called `name_list`, you can make a new list called `list_copy` by doing the following:

`list_copy = list(name_list)`

It might seem a little silly that we are converting a list into a list, but this also has the effect of making a (shallow) copy of the list. 

(Note that this does **not** duplicate the names themselves - it just creates another list of references to the original names. More on that later in the course!)

```
'''
Program: schedule.py
Programmer: Jules Lenzi
Date: 7/4/2026
Course: CS-131B
Description: _.
'''
# CS 131B Project 6

# Copies name list and checks if items are odd
def generate_round_robin_schedule():
    list_copy = list(name_list)
    # Counts list items
    length = len(list_copy)
    # Checks for odd number
    if length = odd:
         # Confirms not even
         even = False
         # Displays message
         Print("Bye!")

def main():
# Calls name list
generate_round_robin_schedule()
# Produces each round after the first
list_copy = \[list_copy\[0\]\] +
# rounds = length - 1
# matches = length / 2
```

## Step 2 - Add a "bye" if necessary

In a situation where there is an odd number of participants in a round robin schedule, one participant gets a "bye" each round (they are not matched with anyone). 

We can simulate this by first checking if the length of our list copy is odd, and then, if it is, adding the new name "bye" to the list copy. Each round, whoever gets paired with "bye" doesn't match with anyone that round.

Write some code in your function to: 

1) check if the length of the list copy is odd
2) add the name "bye" if so

## Step 3 - Make a list of pairs

This is the step that is a lot of work!

### Producing new rounds

Let's say that after step 2, you have N items in your list. This means there will be N - 1 rounds, and each round will have N / 2 matches.

To produce each round after the first, you'll have to modify your list copy in the following way:

- The 0th item stays where it is.
- Everything from `index_1` to `index_N-2` moves up by one.
- The last item (at `index_N-1`) moves to `index_1.`

To accomplish this, I would recommend recreating your list copy at the end of each round using a patchwork quilt approach. 

Piece together the 0th item, the last item, and all the middle items, in that order.

Note that in order to concatenate an individual item (like the 0th item) to a list, you have to convince Python that the individual item is *also* a list. You can just surround it in square brackets to do this, like so:

`list_copy = \[list_copy\[0\]\] + ...`

See how `list_copy\[0\]` is surrounded by another set of square brackets to indicate that it is a partial list.

### Generating pairs for a round

Once you have modified the list for a subsequent round, you can generate the matches using negative indexes, like this:  the item at `index_Q` should match with the item at `index_-Q-1`. That means:

- The item at `index_0` should match with the item at `index_-0-1 = -1`
- The item at `index_1` should match with the item at `index_-1-1 = -2`

Each pair should be represented as a tuple with two strings. Each time you generate a pair (regardless of what round it is), you should append the tuple representing that pair to a new list. That list should initially be empty, and at the end, it should contain all the tuples you made **in the order in which you made them**.

To accomplish this, I'd recommend writing an **inner** for the loop that goes only halfway through your list copy.

To do this, you can divide the length of your list copy by 2, and then give the result to the range function.

However, there is a catch: you'll need to convert the result of the division operation to an integer before giving it to range! 

Dividing something by 2 implicitly creates a float, and the range function doesn't like floats. You can do something like this:

```
for i in range(int(len(list_copy) / 2)):  
\# ...
```

### Example - list with 8 names

Let's say that after step 2, you have 8 names in your list (conveniently named after the letters "A" through "H"). This means you'll have 7 rounds with 4 matches per round.

For the first round, you don't need to change your list copy. Just generate the pairs for that round using the algorithm with negative indexes described above.

Below is an illustration showing what your list copy should look like, along with which pairs you should make. Below each element are its non-negative and negative indexes.

![round_1.png](https://ccsf.instructure.com/courses/72599/files/15668117/preview)

For each of the next six rounds, you should perform the new round production algorithm described above, where you shuffle everything starting at `index_1` to the right and then move the very last item to `index_1`.

The illustration below shows what your list copy should look like once you have performed this algorithm once (for round 2), along with which pairs you should generate.

![round_2.png](../_resources/preview.comcourses72599files)

For round 3, your list copy and pairs should look like this:

![round_3.png](../_resources/preview-2.comcourses72599files)

For the last round (round 7), your list copy and pairs should look like this:

![round_7.png](../_resources/preview-1.comcourses72599files)

The difficult part of this is generalizing so that your function works with a list of **any size**. I highly recommend that you work through this part with paper and a pencil first.

I also recommend that you think not in terms of 8 items, 7 rounds, and 4 pairs per round, but in terms of N items, N - 1 rounds, and N / 2 pairs per round!

# Step 4 - Return your list of pairs and test your function

Once you have gone through the requisite number of rounds above and have appended the appropriate number of tuples per round to your final result list, return your list of tuples. To verify that your function is working correctly, call your function and print what it returns. For the above example, the function might have been called like this:

```
pairs = generate_round_robin_schedule(\['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'\])
```

The returned list of tuples should be as follows:

```
\[('A', 'H'), ('B', 'G'), ('C', 'F'), ('D', 'E'), ('A', 'G'), ('H', 'F'), ('B', 'E'),  
('C', 'D'), ('A', 'F'), ('G', 'E'), ('H', 'D'), ('B', 'C'), ('A', 'E'), ('F', 'D'),  
('G', 'C'), ('H', 'B'), ('A', 'D'), ('E', 'C'), ('F', 'B'), ('G', 'H'), ('A', 'C'),  
('D', 'B'), ('E', 'H'), ('F', 'G'), ('A', 'B'), ('C', 'H'), ('D', 'G'), ('E', 'F')\]
```

# Step 5 - Add comments

Add a comment to the top of your program that contains "CS 131B Project 6".

Then, add a comment near the top of your `generate_round_robin_schedule` (just below the def line) that explains what the function does. It should explain the types and purposes of the parameter and the return value. At minimum, it must contain: "round robin", "parameter", "return value", and "list".

# Step 6 - Create the main function

Add code in the main part of your program to test your function.

# Grading

This assignment is worth 100 points, which will be divided as follows:

|     |     |
| --- | --- |
| **Correctly declares generate_round_robin_schedule** | **10 pts** |
| \- accepts one argument | 5 pts |
| \- returns a list | 5 pts |
|     |     |
| **Makes a copy of the parameter list** | **10 pts** |
|     |     |
| **Adds a "bye" element to the list when appropriate** | **10 pts** |
|     |     |
| **Correctly generates a list of pairs** | **60 pts** |
| \- return value contains pairs for first round | 15 pts |
| \- return value contains pairs for all rounds | 15 pts |
| \- return value contains the correct number of pairs | 10 pts |
| \- return value contains all pairs in the correct order, assuming no bye | 10 pts |
| \- return value contains all pairs in the correct order, with bye | 10 pts |
|     |     |
| **Comments** | **10 pts** |
| \- has a comment at the top that contains "CS 131B Project 8" | 5 pts |
| \- has a comment at the top of the function that contains "round robin", "parameter", "return value", and "list" |     |

# Submission Instructions

1.  Include the standard program header at the top of your Python files.
2.  Execute the program and copy/paste the output that is produced by your program into the bottom of the source code file, making it into a comment. (I will run the programs myself to see the output.)
3.  Make sure the run "matches" your source. If the run you submit could not have come from the source you submit, it will be graded as if you did not hand in a run.
4.  Submit the `schedule.py` file.
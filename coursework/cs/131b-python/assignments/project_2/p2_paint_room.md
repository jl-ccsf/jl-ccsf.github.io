# Programming Project #2
> Due Monday by 11:59pm, 100 points
> Available Jun 2 at 6am - Jun 19 at 11:59pm

Write a program that calculates the amount of paint needed to paint the walls of a room with the given length and width. It assumes that the paint covers 350 square feet per gallon.

Suppose the room has doors and windows that don't need painting. Ask the user to enter the number of doors and number of windows in the room, and adjust the total square feet to be painted accordingly. Assume that each door is 20 square feet and each window is 15 square feet.

## Step 1: Input

1) Declare constants:

    ```
    coverage = 350  # 350 sq ft/gal
    door_area = 20 # 20 sq ft
    window_area = 15 # 15 sq ft
    ```

2) Prompt the user to enter the **length**, **width**, and **height** of the room as well as the number of **doors** and number of **windows**. Store each value in a variable. 

    ```
    length = int(input("Enter the length of the room: "))
    width = int(input("Enter the width of the room: "))
    height = int(input("Enter the height of the room: "))
    num_doors = int(input("How many doors are in the room? "))
    num_windows = int(input("How many windows are in the room? "))
    ```

The length of the room must be stored as an `int` in a variable called "length". The width of the room must be stored as an `int` in a variable called "width". The height of the room must be stored as an `int` in a variable called "height." The number of doors must be stored as an `int` in a variable called "num_doors". The number of windows must be stored as an `int` in a variable called  "num_windows".

## Step 2: Calculation

1) Compute the total square feet to be painted:

	`total_sqft = 2 * width * height + 2 * length * height`

2) Subtract the area of the windows and doors:

	`total_sqft  = total_sqft - num_doors * door_area - num_windows * window_area`

3) Compute the amount of paint needed:

	`paint_needed = total_sqft  / coverage`


## Step 3: Print

Print the input (room dimensions and features) and the number of gallons of paint needed.

```
print("{paint_needed} gallons of paint are needed to cover a room {width} feet wide by {length} feet long by {height} feet high with {num_doors} door(s) and {num_window} window(s).")
```

## Step 4: Comment

1)  Write a documentation comment at the top of the program which indicates the purpose of the program, your name, and today’s date. Save this file as `paint_room.py`. For example:

	```
	'''
	Program: paint_room.py
	Programmer: Jules Lenzi
	Course: CS-131B
	Date: 06/15/2026
	Description: Calculates the amount of paint needed to cover a room based on its dimensions, given a
	rate of 350 square feet per gallon. Assumes an area of 20 sqft for doors and 15 sqft for windows.
	'''
	```

2) Add comment lines after each variable declaration indicating what each represents.

3) Add comment lines for each section of the program indicating what is done in that section.

4) Add a comment line indicating the purpose of the calculation.

## Step 5: Submit

1) Include the standard program header at the top of your Python files.
2) Execute the program and copy/paste the output produced into the bottom of the source code file, making it into a comment. (I will run the programs myself to see the output.)
3) Make sure the run matches your source. (If the run you submit could not have come from the source you submit, it will be graded as if you did not hand in a run.)

	```
	'''
	RUN
	
	Enter the length of the room: 15
	Enter the width of the room: 12
	Enter the height of the room: 8
	How many doors are in the room? 1
	How many windows are in the room? 2
	
	1.0914285714285714 gallons of paint are needed to cover a room
	12 feet wide by 15 feet long by 8 feet high
	with 1 door(s) and 2 window(s).
	'''
	```

5) Submit the `paint_room.py` file before the deadline.
'''
p2_paint_room.py
jl-ccsf
06/15/2026
CS-131B, Prof. Ibrahim
Calculates the amount of paint needed to cover a room based on its dimensions 
given a rate of 350 square feet per gallon. Assumes an area of 20 sqft for doors 
and 15 sqft for windows. Only accepts whole number values.
'''

def main():

      # Defines constants
      COVERAGE = 350 # sqft/gal
      DOOR_AREA = 20 # sqft
      WINDOW_AREA = 15 # sqft

      # Assigns user input to variables as integer values
      length = int(input("Enter the length of the room: ")) # ft
      width = int(input("Enter the width of the room: ")) # ft
      height = int(input("Enter the height of the room: ")) # ft
      num_doors = int(input("How many doors are in the room? "))
      num_windows = int(input("How many windows are in the room? "))

      # Calculates total square footage and gallons of paint
      room_area = (2 * width * height + 2) * 2
      total_sqft  = (room_area - num_doors) * (DOOR_AREA - num_windows) * WINDOW_AREA 
      paint_needed = total_sqft / COVERAGE

      #Displays result in gallons per 350 sqft
      print() # Blank line
      print(paint_needed,"gallons of paint are needed to cover a room\n",width,
            "feet wide by",length,"feet long by",height,"feet high\nwith",
            num_doors,"door(s) and",num_windows,"window(s).")

main()

'''
SAMPLE RUN

Enter the length of the room: 150
Enter the width of the room: 120
Enter the height of the room: 80
How many doors are in the room? 10
How many windows are in the room? 20

122.0 gallons of paint are needed to cover a room 
120 feet wide by 150 feet long by 80 feet high 
with 10 door(s) and 20 window(s).
'''

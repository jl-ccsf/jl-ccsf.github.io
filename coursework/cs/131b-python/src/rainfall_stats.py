'''
m2_rainfall_stats.py
jl-ccsf
07/10/2026
CS-131B, Prof. Ibrahim
Calculates.
'''

def main():
    
    # Defines variables
    total = 0.0
    average = 0.0
    highest = 0.0
    lowest = 0.0
    month_lowest = ''
    month_highest = ''

    # Creates empty list
    month_rain = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                  0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    # Creates list of months
    month_list = ["January", "February", "March",
                  "April", "May", "June", "July",
                  "August", "September", "October",
                  "November", "December"]

    # Gets monthly rainfall amounts
    for i in range(12):
        month_rain[i] = float(input("Enter the rainfall for " + month_list[i] + 
                                    ": "))

    # Calculates annual rainfall
    total = sum(month_rain)
    
    # Calculates average rainfall
    average = total / 12.0
    
    # Calculates maximum rainfall
    highest = max(month_rain)

    # Gets index of month with highest rainfall
    month_highest = month_rain.index(highest)

    # Calculates minimum rainfall
    lowest = min(month_rain)

    # Gets index of month with lowest rainfall
    month_lowest = month_rain.index(lowest) 

    # Displays results
    print() # Blank line
    print(f"Annual rainfall: {total:.2f}")
    print(f"Average rainfall: {average:.2f}")
    print(f"Highest rainfall: {month_list[month_highest]}")
    print(f"Lowest rainfall: {month_list[month_lowest]}")

main()

'''
SAMPLE RUN

Enter the rainfall for January: 1.0
Enter the rainfall for February: 2.0
Enter the rainfall for March: 3.0
Enter the rainfall for April: 4.0
Enter the rainfall for May: 5.0
Enter the rainfall for June: 6.0
Enter the rainfall for July: 7.0
Enter the rainfall for August: 8.0 
Enter the rainfall for September: 9.0
Enter the rainfall for October: 10.0
Enter the rainfall for November: 11.0
Enter the rainfall for December: 12.0

Annual rainfall: 78.00
Average rainfall: 6.50
Highest rainfall: December
Lowest rainfall: January
'''

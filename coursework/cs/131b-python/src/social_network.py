'''
e3_social_network.py
jl-ccsf
06/26/2026
CS-131B, Prof. Ibrahim
Calculates possible connections based on degrees of seperation and average 
number of friends.
'''

def main():

   # Defines contstants
   ERROR = "ERROR: Must be non-negative integer."

   # Assigns integer value to degree
   degree = int(input("Enter the degree of seperation: "))
   while degree < 0:
      print(ERROR)
      degree = int(input("Enter the degree of seperation: "))

   # Assigns integer value to average friends
   avg_friends = int(input("Enter the average friends per user: "))
   while avg_friends < 0:
      print(ERROR)
      avg_friends = int(input("Enter the average friends per user: "))

   # Assignss reachable people to total friends
   total_friends = reachable(degree, avg_friends)
   print(f"{0} people are reachable."
         .format(total_friends))

# Calucates number of connections
def reachable(degree, avg_friends):
   for level in range(0, degree+1):
        friends_level = avg_friends ** level
        total_friends += friends_level
   return total_friends

main()

'''
SAMPLE RUN

Enter the degree of speration: 2
Enter the average friends per user: 15
241 people are reachable.
'''

#Sum of factors:
arr = [20,11]
def sumOfFactors(arr):
    # Write your code here.
    ans = []
    for x in arr:
        sum = 0
        for i in range(1,x+1):
            if(x%i==0):
                sum+=i
        ans.append(sum)
    return ans

print(sumOfFactors(arr))
'''Write a Python script to greet guests at an event based on the time of their arrival and their personal greeting preference.
Your script should include a function that takes three parameters:
the guest's name
their arrival time in a 24-hour format
whether they prefer a 'formal' or 'informal' greeting.
Depending on the time of day (morning before noon, afternoon before 18:00, evening after 18:00) and the guest's preference, the function should print a customized greeting message. Include a list of guests with their names, arrival times, and preferences, and ensure your script can greet each guest appropriately when run.
Provide a function to loop through a list of guests and apply the greeting function to each.

Ensure your script correctly handles the time-based greeting logic and guest preferences and prints the appropriate message for each guest based on the provided data.


Use the following guest data for testing:
> James arrives at 11 and prefers a formal greeting.

> Jacob arrives at 11 and prefers a formal greeting.

> Benjamin arrives at 14 and prefers an informal greeting.

> William arrives at 19 and prefers a formal greeting.

> Alexander arrives at 20 and prefers an informal greeting.



Answer'''
def greet_guest(name,arrival_time,preference):
  if arrival_time<12:
    time_greeting = "Good Morning"
  elif arrival_time<18:
    time_greeting = "Good Afternoon"
  else:
    time_greeting = "Good Evening"
  if preference.lower() =="formal":
    print(f"{time_greeting}, Mr./Ms. {name}.Welcome to the event!")
  else:
    print(f"{time_greeting}, {name}.Welcome to the event!")
guest = [("James",11,"formal"),("Jacob",11,"formal"),("Benjamin",14,"informal"),("William",19,"formal"),("Alexander",20,"informal")]
def greet_all_guests(guests_list):
  for gi in guest:
    greet_guest(gi[0],gi[1],gi[2])
    
greet_all_guests(guest)

"""You have a Python function designed to convert a temperature from Celsius to Fahrenheit. However, the function is not returning the expected results. Your task is to debug and correct the function.

def convert_to_fahrenheit(celsius):
    fahrenheit = celsuis * 9/5 + 32
    return farenheit

# Test the function with a known value
print("The temperature in Fahrenheit:", convert_to_fahrenheit(0))

Answer:"""

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# Test the function with a known value
print("The temperature in Fahrenheit:", convert_to_fahrenheit(0))

"""Create a simple function that takes the base cost of the meal, the tax rate, and the tip percentage as inputs, and returns the total cost of the meal.

Answer: """
def calculate_total_cost(base_cost, tax_rate, tip_percentage):
    tax_amount = base_cost * tax_rate
    tip_amount = base_cost * tip_percentage / 100
    total_cost = base_cost + tax_amount + tip_amount
    return total_cost

"""How do functions help in writing readable and maintainable code?"""

"""Imagine you're an assistant managing an event guest list. You have a string containing names and email addresses separated by semicolons, as shown below:"

guests = "Alice Smith<alice@example.com>; Bob Stone<bob@example.com>; Cara Wins<cara@example.com>"

Can you extract and print each guest's name separately from their email?

Look for the patterns in the string and think about how you might use string methods like split() to isolate the information you need. Write a Python script that parses the guests string and outputs each name and email on a new line in a friendly format.

For example:
Name: Alice Smith, Email: alice@example.com
Name: Bob Stone, Email: bob@example.com
Name: Cara Wins, Email: cara@example.com

Answer:"""
guests = "Alice Smith<alice@example.com>; Bob Stone<bob@example.com>; Cara Wins<cara@example.com>"

for guest in guests.split("; "):
    name = guest.split("<")[0]
    email = guest.split("<")[1].rstrip(">")
    print(f"Name: {name}, Email: {email}")
    
"""Develop a Python script that converts a date from "MM/DD/YYYY" format to "DD MonthName YYYY" format.
For example: 
Input: "05/21/2023"
Output: 21 May 2023

Answer:"""
date = "05/21/2023"
month, day, year = date.split("/")

month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

print(f"{day} {month_names[int(month) - 1]} {year}")

"""Write a Python program to extract the initials from each student's name and create a new list of initials?(e.g., A.S for Alice Smith).

Answer:"""
# List of student names
students = ["Alice Smith", "John Doe", "Emma Watson", "Michael Johnson"]

# Extract initials
initials = []

for name in students:
    parts = name.split()          # Split the name into words
    initial = parts[0][0] + "." + parts[1][0]
    initials.append(initial)

# Display the result
print("Student Names:", students)
print("Initials:", initials)

"""Write a program that uses an IF statement to print "Good morning" if the time is between 5 and 12 hours in a 24-hour format.
Example: 2:00 PM will be 14 in 24-hour format.

Answer:"""
time = int(input("Enter the time in 24-hour format (e.g., 14 for 2:00 PM): "))

if 5 <= time < 12:
    print("Good morning")


"""Create a "Magic Number Guessing" game. 
Your code randomly generates a whole number between 0 to 20, example: 7 and does not disclose that number to you!
You have to guess the number your code generated. 
It asks you to find that number. If your guess matches your code's number then the While loop stops, and code says: "Congratulations!". Else, the code asks you to guess again. 
Write code using a while loop.

Answer:"""


magic_number = random.randint(0, 20)
guess = None

while guess != magic_number:
    guess = int(input("Guess the magic number (0-20): "))
    if guess < magic_number:
        print("Too low!")
    elif guess > magic_number:
        print("Too high!")
    else:
        print("Congratulations!")
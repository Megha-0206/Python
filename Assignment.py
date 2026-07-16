#1 Program - A company wants to identify whether an employee is eligible for a bonus based on their attendance percentage and performance rating.
'''Attendence = float(input("Enter Attendence percentage:"))
Performance_Rating= float(input("Enter Performance Rating:"))
if(Attendence>=80 and Performance_Rating >= 4):
    print("Employee is Eligible for bonus")
else:
    print("Employee is not Eligible for bonus")'''

#2 Program
'''from operator import index

Correct_Username = "Megha00"
Correct_Password = "Megha123"
def login():
    Input_Username = input("Enter Username: ")
    Input_Password = input("Enter Password: ")
    if(Input_Username==Correct_Username and Input_Password==Correct_Password):
        print("Access Granted: login Successful!!!")
    else:
        print("Access Denied: Invalid Username or Password...")
    if __name__ == "__main__":
        login()
#basic( this program is not a part of assignment)
def my__function():
    return ["apple", "banana", "cherry"]
print(my__function()[0])
print(my__function()[1])
print(my__function()[2])

#3 Program 
Speed_limit = 50
Current_Speed = float(input("Enter Current Speed: "))
if(Current_Speed>Speed_limit):
    print("FINE ISSUED:You are Over Speeding")
else:
    print("You are within the speed limit")

#4 Program
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time in Years: "))
SI = (P*R*T)/100
print("Simple Interest is:",SI)

#5 Program
age = int(input("Enter your age: "))
if(age<10):
    print("ticket price is $5 for kids under 10")
elif(age<=18):
    print("ticket price is $10 for child under 18")
else:
    print("ticket price is $15 for Adults")
    
#6 Program
Sales1 = float(input("Enter Sales for Product 1: "))
Sales2 = float(input("Enter Sales for Product 2: "))
Sales3 = float(input("Enter Sales for Product 3: "))
if(Sales1>= Sales2 and Sales1>= Sales3):
    print("Sales1 has the highest sales")
elif(Sales2>= Sales1 and Sales2>= Sales3):
    print("Sales2 has the highest sales")
else:
ength = len(l)
for i in range(length):
    for j in range(i+1,length-1):
        if(l[i]==l[j]):
            l.remove(l[j])
print(l)    print("Sales3 has the highest sales")'''

"""#7 Program - school wants to calculate grades for students based on marks obtained in 5 subjects.
marks = []
for i in range(1,6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
average = sum(marks)/5
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Average marks: {average}")
print(f"Grade: {grade}")

#8 program - Create a login attempt system that allows the user a maximum of 3 attempts using a while loop.
Correct_Username = "Megha00"
Correct_Password = "Megha123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    Input_Username = input("Enter Username: ")
    Input_Password = input("Enter Password: ")
    if(Input_Username==Correct_Username and Input_Password==Correct_Password):
        print("Access Granted: login Successful!!!")
        break
    else:
        print("Access Denied: Invalid Username or Password...")
        attempts += 1
else:
    print("Maximum login attempts exceeded.")
    
#9 program - A food delivery app wants to display menu items repeatedly until the user selects exit.
choice = ''
while choice.lower() != 'exit':
    print("Menu:")
    print("1. Pizza")
    print("2. Burger")
    print("3. Pasta")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        print("You selected Pizza.")
    elif choice == '2':
        print("You selected Burger.")
    elif choice == '3':
        print("You selected Pasta.")
    elif choice == '4':
        print("Exiting the menu.")
        break
    else:
        print("Invalid choice. Please try again.")"""
 
'''       
#Q11.Write a program to print all even numbers between 1 and 100 using a for loop.
print("Even numbers between 1 and 100: ", [i for i in range(1, 100) if i % 2 == 0] )

#Q12. A library system wants to count how many overdue books exist in a list of borrowed books.

overdue_books = [True, False, True, True, False, False, True]

count = 0

for book in overdue_books:
    if book:
        count += 1

print("Number of overdue books:", count)'''

#Q16. A teacher wants to store marks of students in a list and display the average marks.
"""
marks = []
for i in range(1,6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
average = sum(marks)/5
print(f"Average marks: {average}")

#Q17. Remove Duplicate Product IDs.
product_ids = [101, 102, 103, 102, 104, 103, 105]
unique_product_ids = list(set(product_ids))
print("Unique Product IDs:", unique_product_ids)"""

#Q18. Travel Cities

cities = ("Delhi", "Mumbai", "Jaipur", "Goa", "Shimla")

print("Cities visited by the customer:")
for city in cities:
    print(city)

#Q19. Character Frequency Counter.

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character Frequency:")
for key, value in frequency.items():
    print(key, ":", value)
    
#Q20. Student Record Management.

students = {
    101: "Aman",
    102: "Riya",
    103: "Rahul"
}

print("Student Records:")
for roll, name in students.items():
    print("Roll No:", roll, "Name:", name)

search = int(input("Enter Roll Number to search: "))

if search in students:
    print("Student Name:", students[search])
else:
    print("Student not found.")
    
#Q21.Book Search.

books = ["Python", "Java", "C", "C++", "HTML"]

book = input("Enter the book name to search: ")

if book in books:
    print("Book is available.")
else:
    print("Book is not available.")
    
#Q22.Reverse Words.
sentence = input("Enter a sentence: ")

words = sentence.split()

print("Reversed Words:")

for word in words:
    print(word[::-1], end=" ")
    
#Q23.Sort Player Names.

players = ["Rohit", "Virat", "Dhoni", "Hardik", "Gill"]

players.sort()

print("Player Names in Alphabetical Order:")
for player in players:
    print(player)
    
#Q24.Merge Employee IDs.
employee_ids1 = [101, 102, 103, 104]
employee_ids2 = [103, 104, 105, 106]

merged_ids = list(set(employee_ids1 + employee_ids2))

print("Merged Employee IDs:")
print(merged_ids)

#Q25. Common Elements in Sets.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

common = set1.intersection(set2)

print("Common Elements:")
print(common)


'''
#CHECK if two strings are rotation of each other(program not in assissment):
s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
if len(s1)==len(s2):
    s1 = s1+s2
    if (s2 in s1):
        print("True")
else:
    print("Rotation is not possible")
    
#Remove Duplicate without using set function(program not in assissment):
l = [1,2,2,3,3,3,4]
result =[]
for i in l:
    if i not in result:
        result.append(i)
print(result)'''
        
#Group words by length(program not in assissment):
"""s = "He is Superman"
l = s.split(" ")
print(l)
d = dict()
for i in l:
    if len(i) not in d:
        d[len(i)] = []
        print(d)
    d[len(i)].append(i)
    print(d)
print(d)"""

# bank account class
"""class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")"""
            
"""class Bank:
    def withdraw(self):
        print("Withdraw")
        
class SavingsAccount(Bank):
    def withdraw(self):
        print("Withdraw from savings account")

class CurrentAccount(Bank):
    def withdraw(self):
        print("Withdraw from current account")    

s = SavingsAccount()
c = CurrentAccount()
s.withdraw()
c.withdraw()"""    
 






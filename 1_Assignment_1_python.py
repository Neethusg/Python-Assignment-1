ASSIGNMENT 1

# EXERCISE 1
# Write Python code that prints your name, student number and email address
name = "Bob"
student_number = "ST1001"
email = "bob@gmail.com"

print('Name of the student is:', name)
print('Student number is:', student_number)
print('email is:', email)

# EXERCISE 2
# Write Python code that prints your name, student number and email address using escape sequences
print("Name:\tBob\nStudent Number:\tST1001\nEmail:\tbob@gmail.com")

# EXERCISE 3
# Write Python code that add, subtract, multiply and divide the two numbers
# Defining two variables

x = 14
y = 7

a = x+y
b = x-y
c = x*y
d = x/y

print('The sum of x and y is:', a)
print('The subtraction of x and y is:', b)
print('The product of x and y is:', c)
print('The division of x and y is:', d)

# EXERCISE 4
# Write Python code that displays the numbers from 1 to 5 as steps.

for i in range (1,6):
    print(i)

# EXERCISE 5
# Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen:

print(""" "SDK" stands for "Software Development Kit", whereas
"IDE" stands for "Integrated Development Environment". """)

# EXERCISE 6
# Practice and check the output

print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

# EXERCISE 7
# Defining variables
num = 23
textnum = "57"
decimal = 98.3

print( 'The type of number is:', type(num))
print('The type of text number is:', type(textnum))
print("The type of decimal number is:", type(decimal))

sum_result = num + int(textnum) + decimal
print('The sum of variables is:', sum_result)

print('The type of sum of the variables is:', type(sum_result))

# EXERCISE 8
# Defining variables

days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60

total_minutes_in_year = days_in_year * hours_in_day * minutes_in_hour

print('Number of days in a year:', days_in_year)
print('Hours in a day:',hours_in_day )
print('Minutes in hour:', minutes_in_hour)
print('The number of minutes in a year:', total_minutes_in_year)

# EXERCISE 9

name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")

# Exercise 10

Exchange_rate = 1.25   # 1 pound = 1.25 dollar
pounds = float(input("Please enter amount in pounds: "))
dollars = pounds * Exchange_rate

print(f"£ {pounds} are $ {dollars}")


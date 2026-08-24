'''Scenario 1 - Write a program that accepts marks for 3 subjects and calculates:
• Total marks
• Average marks
• Whether the student passed or failed'''
# Accept marks for 3 subjects

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# Calculate total and average
total = mark1 + mark2 + mark3
average = total / 3

# Check pass or fail
if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    result = "Passed"
else:
    result = "Failed"

# Display result
print("Total Marks:", total)
print("Average Marks:", average)
print("Result:", result)

'''Scenario 2- Write a program to determine whether a given number is Even or Odd.'''
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

'''Scenario 3 - Write a program to check whether a given number is
• Positive
• Negative
• Zero'''
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

'''Scenario 4 - Largest of Two Numbers
Write a program to find the largest among two numbers.'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Largest number:", num1)
elif num2 > num1:
    print("Largest number:", num2)
else:
    print("Both numbers are equal")

'''Scenario 5 - Largest of Three Numbers
Difficulty: Easy–Intermediate
Write a program to find the largest among three numbers.'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number:", num2)
else:
    print("Largest number:", num3)

'''Scenario 6 - Student Grade Calculator
Write a program to assign a grade based on marks.
Also validate that marks are between 0 and 100.
'''
marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter marks between 0 and 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

'''Scenario -7 - Simple Calculator
   Write a calculator program that accepts two numbers and an operator (+, -, *, /).
'''
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")

#Scenario 8 - Voting Eligibility Checker
'''Write a program to check whether a person is eligible to vote.
Condition: Age must be 18 or above.'''

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#Scenario 9 - Simple Login Validation
'''Create a simple login validation program.
The program should accept:
• Username
• Password
Check whether both match the predefined username and password.'''

username = input("Enter username: ")
password = input("Enter password: ")

correct_username = "admin"
correct_password = "12345"

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")

#Scenario 10 - Electricity Bill Calculator
'''Write a program to calculate an electricity bill based on units consumed'''
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 2

elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)

elif units <= 300:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

else:
    bill = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

print("Electricity Bill: ₹", bill)

#Scenario 11 - Salary Calculation
'''Write a program that accepts an employee's basic salary and calculates:
• HRA = 20% of basic salary
• DA = 10% of basic salary
• Gross Salary = Basic + HRA + DA
'''

basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 0.20
da = basic_salary * 0.10
gross_salary = basic_salary + hra + da

print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross_salary)

#Scenario 12 - Discount Calculator
'''A shopping application gives discounts based on purchase amount.
Purchase Amount      Discount
₹10,000 or above     20%
₹5,000–₹9,999        10%
Below ₹5,000         No discount
Write a program to calculate the final amount.'''
amount = float(input("Enter purchase amount: "))

if amount >= 10000:
    discount = amount * 0.20

elif amount >= 5000:
    discount = amount * 0.10

else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final Amount:", final_amount)

#Scenario 13 - Three-Digit Number Digit Operations
'''
Accept a three-digit number and calculate:
• First digit
• Middle digit
• Last digit
• Sum of all digits
'''
num = int(input("Enter a three-digit number: "))

first_digit = num // 100
middle_digit = (num // 10) % 10
last_digit = num % 10

sum_digits = first_digit + middle_digit + last_digit

print("First digit:", first_digit)
print("Middle digit:", middle_digit)
print("Last digit:", last_digit)
print("Sum of digits:", sum_digits)

#Scenario 14 - Employee Bonus Eligibility
'''An employee receives a bonus if:
• Experience is 5 years or more, AND
• Salary is less than ₹50,000
Write a program to check whether the employee is eligible.'''

experience = int(input("Enter experience in years: "))
salary = float(input("Enter salary: "))

if experience >= 5 and salary < 50000:
    print("Employee is eligible for bonus")
else:
    print("Employee is not eligible for bonus")

#Scenario 15 - ATM Withdrawal Validation
'''Write a program to simulate an ATM withdrawal.
Given:
• Account balance
• Withdrawal amount
The withdrawal should be successful only when:
1. Withdrawal amount is greater than 0
2. Withdrawal amount is less than or equal to account balance
3. Withdrawal amount must be a multiple of 100
Otherwise, display an appropriate message.
'''

balance = float(input("Enter account balance: "))
amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Withdrawal amount must be greater than 0")

elif amount > balance:
    print("Insufficient balance")

elif amount % 100 != 0:
    print("Withdrawal amount must be a multiple of 100")

else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)
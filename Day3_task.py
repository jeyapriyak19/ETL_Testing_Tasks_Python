'''Task 1 – Student Marks Processing
Problem Statement
A teacher wants to process the marks of 5 students. You are given the marks of each student one
by one.
For every mark:
• If the mark is greater than or equal to 40, print "Pass".
• Otherwise, print "Fail".'''
count = 1

while count <= 5:
    marks = int(input("Enter marks: "))

    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

    count += 1
    
'''Task 2 – ATM PIN Validation
Problem Statement
An ATM allows a user to enter a PIN until the correct PIN is entered.
The correct PIN is 1234.
Keep asking the user to enter the PIN.
• If the PIN is correct, print "Access Granted" and stop.
• If the PIN is incorrect, continue asking.
'''
correct_pin = 1234

while True:
    pin = int(input("Enter PIN: "))

    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN. Try again.")

'''Task 3 – Process Only Valid Transactions
Problem Statement
A banking system receives a list of transaction amounts.
Negative amounts represent invalid transactions.
Process only the valid transactions.
For every negative amount, skip the transaction.
For every positive amount, print:
Processing: amount
'''
transactions = [1000, -500, 2500, -200, 1500]

for amount in transactions:
    if amount < 0:
        continue

    print("Processing:", amount)
'''
Task 4 - Find the First Failed Login
Problem Statement
A security system checks login attempts.
You are given a sequence of login results:
success
success
success
failed
success
success
The system should process the attempts until the first failed login is found.
Once "failed" is encountered:
• Print "Security Alert"
• Stop processing further attempts.
'''
login_attempts = ["success", "success", "success", "failed", "success", "success"]

for result in login_attempts:
    if result == "failed":
        print("Security Alert")
        break

    print("Login successful")

'''Task 5 – Calculate Total Sales
Problem Statement
A shop records sales for 7 days.
You are given the sales amount for each day.
Calculate the total sales for the week
'''
sales = [1000, 1500, 800, 1200, 2000, 1750, 900]

total = 0

for amount in sales:
    total = total + amount

print("Total sales:", total)

'''Task 6 – Reverse a Number
Problem Statement
A system receives a number and needs to reverse it.
Write a program to reverse the given number using a while loop.
'''
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)

'''Task 7 – Generate Multiplication Table
Problem Statement
A student enters a number.
Generate its multiplication table from 1 to 10.'''
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

'''Task 8 – Employee Department Processing
Problem Statement
A company has multiple departments, and each department has multiple employees.
'''
departments = {
 "IT": ["Arun", "Priya"],
 "HR": ["Rahul", "Divya"],
 "Sales": ["Kumar", "Anitha"]
}


for department, employees in departments.items():
    print("Department:", department)

    for employee in employees:
        print("Employee:", employee)

'''Task 9 – Generate Number Pattern
Difficulty: Medium
Topics: Nested for, range()
Problem Statement
A company wants to generate a number pattern for a report.
Print the following pattern:
1
12
123
1234
12345'''
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")

    print()

'''Task 10 – Employee Salary Processing
System
Difficulty: Medium–Hard
Topics: for, continue, break, accumulator
Problem Statement
A company wants to process employee salaries.
Given:
salaries = [25000, 35000, -5000, 45000, 60000, 70000, 30000]
Process the salaries using the following rules:
1. If the salary is negative, skip it.
2. If the salary is greater than 60000, stop processing completely.
3. Otherwise, print the salary.
4. Calculate the total of all processed valid salaries before the loop stops.'''
salaries = [25000, 35000, -5000, 45000, 60000, 70000, 30000]

total = 0

for salary in salaries:

    if salary < 0:
        continue

    if salary > 60000:
        break

    print("Salary:", salary)
    total = total + salary

print("Total:", total)
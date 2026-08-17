#Task 1 – Source and Target Record Count Validation
'''Scenario
An ETL Tester needs to verify whether all records extracted from the source have been
successfully loaded into the target.
You are given the source record count and target record count.
Calculate whether the source and target record counts are equal.'''

source_count = 1000
target_count = 1000

if source_count == target_count:
    print("PASS - Source and Target record counts are equal")
else:
    print("FAIL - Source and Target record counts are not equal")

#task2 - Identify Missing Records
'''
Scenario
An ETL process extracted 15,000 records from the source, but only 14,850 records were loaded
into the target.
Calculate the number of records missing from the target.
'''
source_count = 15000
target_count = 14850

missing_records = source_count - target_count

print("Missing records:", missing_records)

#Task 3 – ETL Validation PASS or FAIL
'''Scenario 
An ETL Tester wants to automatically determine whether a test case has passed.
The test should PASS only when:
• Source count equals target count.
Otherwise, it should FAIL.'''
source_count = 15000
target_count = 15000

if source_count == target_count:
    print("PASS")
else:
    print("FAIL")

#Task 4 – Multiple ETL Validation Conditions
'''
Scenario
An ETL Tester validates a daily load using three conditions:
• Source count must equal target count.
• Duplicate count must be 0.
• NULL count must be 0.
The validation should return True only when all three conditions are satisfied.
'''
source_count = 15000
target_count = 15000
duplicate_count = 0
null_count = 0

result = (
    source_count == target_count
    and duplicate_count == 0
    and null_count == 0
)

print(result)

#Task 5 – Identify Failed Validation
#Scenario An ETL validation should pass only when the source and target counts are equal.
source_count = 8500
target_count = 8200

result = source_count == target_count

print(result)

#Task 6 – Required Column Validation
'''Scenario
The target table must contain the following columns:
customer_id
customer_name
email
salary
Check whether the required column customer_id exists in the list of target columns.'''

target_columns = ["customer_id", "customer_name", "email", "salary"]

result = "customer_id" in target_columns

print(result)
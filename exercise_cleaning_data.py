from datetime import datetime, date

print(datetime.now())

"""
We have a list of data employees pulled from some CSV file
(Actually generated from chatGPT)
and we want to clean this date
What is wrong with the data? (I'm asking myself questions here lol)
1. It is complete no null values or stuff like that (So that is right)
2. But the value types are issues
   - The date is of type string
   - The job_skills is of type string where we would like it to be a list of skills

so those are the changes we are going to need to make here.
"""
# List of Dictionaries
employees = [
    {'name': 'Mike', 'age': 22, 'job_skills': "['Python', 'SQL', 'PowerBI']", 'hired_date': "2023-05-12"},
    {'name': 'Jenna', 'age': 29, 'job_skills': "['Java', 'Spring', 'Hibernate']", 'hired_date': "2022-11-03"},
    {'name': 'Anele', 'age': 24, 'job_skills': "['Python', 'Tableau', 'Excel']", 'hired_date': "2023-01-17"},
    {'name': 'Sibongile', 'age': 26, 'job_skills': "['C++', 'SQL', 'Linux']", 'hired_date': "2021-09-30"},
    {'name': 'Kopano', 'age': 31, 'job_skills': "['JavaScript', 'React', 'Node.js']", 'hired_date': "2023-07-22"},
    {'name': 'Thando', 'age': 27, 'job_skills': "['Python', 'Pandas', 'NumPy']", 'hired_date': "2022-05-14"},
    {'name': 'Zanele', 'age': 25, 'job_skills': "['SQL', 'PowerBI', 'Excel']", 'hired_date': "2024-03-05"},
    {'name': 'Jason', 'age': 30, 'job_skills': "['C#', '.NET', 'Azure']", 'hired_date': "2023-08-10"},
    {'name': 'Liam', 'age': 28, 'job_skills': "['Python', 'R', 'Jupyter']", 'hired_date': "2022-12-01"},
    {'name': 'Nomsa', 'age': 23, 'job_skills': "['HTML', 'CSS', 'JavaScript']", 'hired_date': "2023-06-28"},
]

print(employees[0])
print(employees[0]['hired_date'])

print(type(employees[0]['hired_date']))
# As we can see the type returned is String, often the case especially when importing from a CSV file
# Now lets convert it to the date format
# Parse Str to DateTime
#

temp_date = employees[0]['hired_date']
# Str parse time
datetime.strptime(temp_date, '%Y-%m-%d')
# Now in the format: 2023-05-12 00:00:00
# To remove the times import date
import ast

for employee in employees:
    employee['hired_date'] = datetime.strptime(employee['hired_date'], '%Y-%m-%d')
    employee['job_skills'] = ast.literal_eval(employee['job_skills'])


def displayAll():
    for i in employees:
        print(i)


displayAll()

# Converting skills to list from string (refer to line 49)

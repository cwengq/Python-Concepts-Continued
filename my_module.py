my_skills = ['Python', 'SQL', 'PowerBI']


# Mostly used for holding functions to be used in other
# e.g.
def skill(skill_name):
    return f'{skill_name} is my favourite skill'


# Since we have the specific function imported
from analyzer import calc_deposit

# We can just call the function without analyzer.calc_deposit=
calc_deposit(6150, 1.5)

# Standard Libraries
salary_list = [9000, 10000, 15000, 97000]

# import statistics *
# With the * we don't want to always import the entire library as they can be large
# So for this case we should stick to importing those functions we need
# Also NB! if we define some variable or method with a clashing naming from the one in the import we will have issues
#import statistics
#or
from statistics import mean, mode

#print(statistics.mean(salary_list))
print(mean(salary_list))

# Name: Jamar Hill
# Date: 11/3/2020
# Description: Assignment 6.c

class Person:
    def __init__(self, name, age):
        """Person is represented by self by data member name and age"""
        self.name = name
        self.age = age

def std_dev(person_list):
    age_val = 0
    """represent ages values in the list"""
    for person in person_list:
        """establishes individual value of each age"""
        age_val += person.age
    age_val /= len(person_list)
    """Calulates and mean age value"""
    n_total = 0
    for person in person_list:
        """subtracts the age value from the mean age value and squares the result"""
        """adds each value in the list together for = total"""
        n_total += (person.age - age_val)**2
        """divides total by the amount of entries in the list then calculates for the square root"""
    return (n_total / (len(person_list)))** 0.5

"""Assigns a variable to person 1"""
p1 = Person("Kyoungmin", 73)
"""Assigns a variable to person 2"""
p2 = Person("Mercedes", 24)
"""Assigns a variable to person 3"""
p3 = Person("Beatrice", 48)
person_list = [p1, p2, p3]
print(std_dev(person_list))


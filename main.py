# variables
age: int = 27
height: float = 6.1
name: str = 'Cwenga'
male: bool = True

# Collections
friends: list = ['Bob', 'Anna', 'Sam']  # ArrayList
friends_id: set = {1, 2, 3}  # HashSet
friends_heights: tuple = (6.0, 5.3, 6.0)  # No Java Equivalent

car: dict = {  # Map
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964,
    'engine': 2.4,
    'sold': False,
    'colours': ["red", "blue", "black"]
}

# region List Info
#   [Lists]
#     - Ordered
#     - Mutable
#     - Mixed variable types allowed
#     - list(("apple", "banana", "orange")) creates list

#   (Tuple)
#     - Ordered
#     - Immutable
#     - Allows Duplicates & Mixed Variable types

#   {Sets}
#     - Unordered
#     - Immutable
#     - No Duplicates, duplicates ignored

#   {Dict : ionaries}
#     - Key, Value pairs
#     - Mutable
#     - Duplicates not allowed (will be overwritten)
#     - dict(name = "John", age = 36, ..) creates a dictionary

# endregion

# region Collection Functions

# List Functions
friends[1]  # Indexing first item
friends[-1]  # Indexing last item
# Slicing: list[start:end:steps]
friends[2:4]  # Slices 2nd -> 3rd item
friends[1] = 'Ann'
# friends.insert(position, value)
# friends.append(value)
# friends.extend(any iterable Collection)
# friends.remove(value) Removes first occurence & changes indexes
# friends.pop(index)
# del friends (Deletes entire list)
# friends.clear()
# friends.sort()
# friedns.sort(reverse = True) Descending order

# Tuple Functions
this_tuple = ("A", "B", "C", "D")
this_tuple[1]
# Slicing: tuple[start:end:steps]
this_tuple[2:5]  # slicing

# In order to UPDATE tuple, convert it into a list first
x = ("apple", "banana", "cherry")  # Original Tuple
print(x, ": Tuple")
y = list(x)  # New List = Tuple
print(y, ": List")
# region Changes made
y[1] = "kiwi"
y.append("orange")
y.remove("cherry")
# endregion
print("Changes made!")
print(x, ": Before Changes implemented")
x = tuple(y)  # Assign Original Tuple to List (Casted as Tuple)
print(x, ": After Changes implemented")

# Unpacking: Assigning each value in Tuple to variable
(green, yellow, red) = x;
print(green)

# Sets Functions
this_set = {"A", "B", "C", "D"}
temp_list = list(this_set)
temp_list.pop()
this_set = set(temp_list)
this_set.add("E")


# this.update(any Iterable)
# this_set.discard("csf") will not throw error if not found

# Joining Sets (UNION() |, UPDATE(), INTERSECTION() &, DIFFERENCE(), SYMMETRIC_DIFFERENCE()
# new_set = this_set.union(set2, set3)
# set3 = set1.intersection(set2) Keeps only the duplicates
# set1.intersection_update(set2) Changes set 1 instead of returning a new set
# set1.difference(set2) OUTTER JOIN

# Dictionaries

# endregion

#List Comprehension
numbers = [x for x in range(10)]
#[x ~ define x, then for loop to iterate in range of 100]

# region Functions
def greet(name: str):  # Parameter with explicit type
    print(f'Hello, {name}!')


def add(a: float, b: float) -> float:  # Function returning float type
    return a + b


def add(a, b):
    return a + b


# endregion

# region Class & Methods
class Car:  # Classes create objects? (sort of)
    # def __init__(self, brand, model, year, engine, sold, colours):
    def __init__(self, brand: str, model: str, year: int, engine: float, sold: bool,
                 colours: set()):  # Initialiser = Constructor
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine
        self.sold = sold
        self.colours = colours

    # Method
    def displayCar(self):
        print(f'{self.year} {self.brand}...')

    def getBrand(self) -> str:
        return self.brand

    def setBrand(self, var: int):
        print(var)
        self.brand = input("Enter brand name: ")


vw: Car = Car('VW', 'GTI', 2023, 2.5, False, ['Blue', 'Black', 'Red']) #Instantiating vw
print(vw.year)

# endregion



# Function with default arguments
def power(number, pow=1):
    """Raise number to the power of pow."""
    result = number ** pow
    return result
print(power(4))
print(power(4,3))
three_pow_three = power(3,3)
print(three_pow_three * 2)
print("\n")

# flexible arguments: can be used when the number of arguments isn't known
# Example 1
def add_all (*addt): #this turns all the arguments passed into a tuple 
    """Sum all the values in *args together."""

    # Initialize sum
    sum_all = 0

    #Accumulate the sum
    for num in addt:
        sum_all += num

    return sum_all
print(add_all(2,3,5,1,4))
print("\n")

# Example 2
def list_it(*digits):
    """List all the arguments in order"""
    sum1 = digits * 2
    return sum1
print(list_it(2,3,4,5))
print("\n")


# Functions with keyword argument: arguments preceeded by identifiers, like a dictionary
#Example 1
def print_all(**person):
    "Print out the key_value pairs in **person"""

    for key, value in person.items():
        dict= key + ": "+value

    return person
person1= print_all(name="hameed", role="MD", branch="Lagos", salary="150k")
person2=print_all(name="Saheed", role="GM", branch="Lagos", salary="200k")

print(person1)
print(person1["name"].upper() + ": " + person1["salary"])
print(person2)
print(person2["name"].upper() + ": " + person1["salary"])
print("\n")


# LAMBDA functions
raise_to_power = lambda x,y : x**y
print(raise_to_power(3,3))

square_or_power = lambda x,y=2 : x**y
print(square_or_power(3))

people = lambda **details: details
print(people(name="hameed", role="MD", branch="Lagos", salary="150k"))

twice= lambda *num: num *2
print(twice(1,2,3,4))
print("\n")

# Immediately invoking a lambda function
print((lambda x,y : x*y)(5,7))
print("\n")

# nested lambda functions
high_order = lambda x,y, lmbfunc: (2*x) + lmbfunc(x,y)

new_func = high_order(10,3, lambda x,y : y*x)
print(new_func)
print("\n")

# LAMBDA functions with map()
# map() takes two args: a func and a sequence, it applies the func to all elements in d seq

seq = [2,5,1,7]

double_seq = map(lambda x: x*2, seq)
print(double_seq)
print(list(double_seq))
print("\n")

# LAMBDA functions with filter()
# filter() is used to filter a seq using another function dat defines d filtering logic

mylist = [2,3,4,5,6,7,8,9,10]
list_new  = list(filter(lambda x : (x%2==0), mylist))
print(list_new)

# LAMBDA functions with reduce()
# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)

# Print the result
print(result)








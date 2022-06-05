import pandas as pd

raw_dict =\
{
	"name": [],
	"age": [],
	"color": [],
	"salary": []
}

raw_list = []
class User:

    min_salary = 20000 #This is a class attribute
    def __init__ (self, name, age, best_color, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.best_color = best_color
        raw_dict["name"].append(name)
        raw_dict["age"].append(age)
        raw_dict["color"].append(best_color)
        raw_dict["salary"].append(salary)
        raw_list.append({"name": name, "age": age, "color": best_color, "salary": salary})

    def salary_raise(self, raise_amount):
        self.salary= self.salary + raise_amount

    # using class methods as alternative constructor (another way of creating our objects)
    # assuming we have this kind of use cases (input from user): first-last-pay
    # we want to create the employee object from it as shown below

    @classmethod 
    def new_user (cls, details):
        name, age, best_color, salary = details.split('-')
        return cls(name, age, best_color, salary)

        
        
user1 = User("Saheed", 23, "blue", 20000)
user2 = User("Habeeb", 25, "green", 750000)
user3 = User("Sodiq", 24, "yellow", 150000)

user4 = User.new_user("Uthman-22-White-10000") # Alternative construction

user2.salary_raise(100000)
print(user2.salary)



df = pd.DataFrame(raw_dict)
df2 = pd.DataFrame(raw_list)

user4 = User.new_user("Uthman-22-White-10000")


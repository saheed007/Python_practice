##using a while loop
number = input("Type your number here: ")
product =1
current =1

while current <= int(number):
    product *= current
    current += 1
print(f"The factorial of {number} is {product}")

##using for loop

number = input("Type your number here: ")
product =1
current =1

for i in range(2,(int(number))+1):
    product *= i
print(f"The factorial of {number} is {product}")    

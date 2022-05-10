check_prime = [26, 39, 51, 53, 57, 79, 85]

##num = int(input("your number: "))

result=""
for num in check_prime:
    for x in range(2, num):
        if num%x == 0:
            result=f"{num} is not a prime number because {x} is a factor of {num}"
            break
        if num%x != 0:
            result=f"{num} is a prime number"
    print(result)        

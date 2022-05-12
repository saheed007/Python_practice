sqrt = lambda x: x**(1/2)
print(sqrt(4))
#print(sqrt("hey")) """gives an error, we have to give a useful error message to the
#                      user in cases like this"""

# we use the try-except clause to catch exceptions
try:
    lambda x: x**(1/2)
    print(sqrt(9))
    print(sqrt(2.5))
    print(sqrt("h"))
    
except:
    print("x should be a number")

print("\n")
# can also specify the kind of error we want to catch e.g TypeError
try:
    lambda x: x**(1/2)
    print(sqrt(9))
    print(sqrt(2.5))
    print(sqrt("h"))
    
except TypeError:
    print("x should be a number")

    
# RAISING AN ERROR

def sqrt(x):
    """Return the square root of a positive number(x)"""
    
    if x < 0:
            raise ValueError("x must be non-negative")
    try:
        return x **0.5
    
    except TypeError:
        print("x should be a number")
        
print(sqrt(9))
print(sqrt(2.5))
print(sqrt(-10))
print(sqrt("h"))

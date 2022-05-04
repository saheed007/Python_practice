#Strings are created using either single quotes (' ') or double (" ").
#Multi-line strings are made using triple double quotes("""  """)

print('This string uses single quotes')
print("This one uses double quotes")
print("""This is multi-line
string that
uses triple double quotes""")

# Practicing escape sequences \newline, \\, \’, \" \a \b, \f, \n ,\r ,\t, \uhhhh, \v, \ooo, \xhh

print("I love python. \\\n\tit\'s  \bthe best")


# Selecting individual characters from a string
String1 = "Hello World"
String2 = "Python is Fun!"
print(String1[0])
print(String1[0:5])
print(String1[:5])
print(String1[6:])
String3 = String1[:6] + String2[:6]
print(String3)
print(String2[:7]*5)

# How to convert names to initials
first_name=input("Enter your first name: ")
middle_name=input("Enter your last name: ")
last_name=input("Enter your last name: ")

print("You are "+ first_name[0] + ". "+ middle_name[0]+ " "+ last_name)
#The use of the + sign to combine two strings is called concatenation
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    print(cities[index].title().replace(" ","_"))
print("\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#USING FOR LOOPS TO CREATE A LIST

list=[]
for x in range(0,10, 2):
    list.append(x)
print(list)
print("\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#ANOTHER EXAMPLE

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
cities_cap=[]
for city in cities:
    cities_cap.append(city.upper()) #CREATES ANOTHER LIST OF ALL THE CITIES IN UPPER CASE
print(cities_cap)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# THIS SHOWS HOW TO USE A FOR LOOP TO COUNT

strg = "this test tries it"
count=0

for x in strg:
    if (x == "t"):
        count+=1
print(count)
print("\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)
print("\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#USING FOR LOOP TO BUILD A DICTIONARY FROM LISTS
"""we can create a dictionary, word_counter, that keeps track of the
total count of each word in a string."""

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}   #create an empty dictioinary
count=1
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1 #places each value into the dict
    count+=1
print(word_counter)
print("\n")

"""the for loop iterates through the list as we saw earlier.
The for loop feeds 'great' to the next statement in the body of the for loop.
In this line: word_counter[word] = word_counter.get(word,0) + 1,
since the key 'great' doesn't yet exist in the dictionary,
get() will return the value 0 and word_counter[word] will be set to 1.
Once it encounters a word that already exists in word_counter
(e.g. the second appearance of 'the'), the value for that key is incremented by 1.
On the second appearance of 'the', the key's value would add 1 again, resulting in 2.
Once the for loop finishes iterating through the list, the for loop is complete."""

# another method

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_count = {}   #create an empty dictioinary

for word in book_title:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
print(word_count)
print("\n")

"""The for loop iterates through each element in the list.
For the first iteration, word takes the value 'great'.
Next, the if statement checks if word is in the word_counter dictionary.
Since it doesn't yet, the statement word_counter[word] = 1 adds great as a key
to the dictionary with a value of 1.
Then, it leaves the if else statement and moves on to the next iteration of the for loop.
word now takes the value expectations and repeats the process.
When the if condition is not met, it is because thatword already exists in the word_counter dictionary,
and the statement word_counter[word] = word_counter[word] + 1 increases the count of that word by 1.
Once the for loop finishes iterating through the list, the for loop is complete."""


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#Iterating Through Dictionaries with For Loops

#using the keys only
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
for key in cast:
    print(key)

#using the keys and the values together
for key, value in cast.items():
    print("Actor: {}  --  Role: {}".format(key, value))

#items is an awesome method that returns tuples of key, value pairs,
#    which you can use to iterate over dictionaries in for loops.


# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for x in basket_items:
#if the key is in the list of fruits, add the value (number of fruits) to result
    if x in fruits:
        result += basket_items[x]

print(result)




















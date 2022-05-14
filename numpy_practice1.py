# Import numpy
import numpy as np

# Creating an array in numpy
list1 = [1,2,3,4,5]
array1 = np.array(list1)
print(list1, "\n", array1)
print(list1*2, "\n", array1*2)
print("\n")

def trial2():
    list2 = [a,b,c,d]
    array2=np.array(list2)
try:
    print(list2, "\n", array2)
except NameError:
    print("Array can't work on list of strings")
print("\n")

list3 = [7,6,2,1,5]
array3 = np.array(list3)
print((array1/array3)) # Lists can't do this
print(array1 **3) # Lists can't do this
print("\n")
print(array3 <= 3)  # Lists can't do this
print(array3[array3 <= 3])  # Lists can't do this
print("\n")

# Creating a 2d array
array_2d = np.array([list1,list3])
print(array_2d)
print("array_2d shape:", array_2d.shape) #(2,5) 2 rows, 5 colunms
print("\n")

print(array_2d[1])
print(array_2d[0][2]) 
print(array_2d[0,2]) #Same result as above
print("\n")
print(array_2d[:, 2:4])
print("\n")

# basic statistics
print(np.mean(array_2d[0]))
print(np.mean(array_2d[1]))
print("\n")
print(np.median(array_2d[0]))
print(np.median(array_2d[1]))
print("\n")

# other are: np.corrcoef(), np.std(), sum(), sort()
print(np.sort(array_2d))

#Building numpy arrays from scratch
# 1
print(np.zeros((2,3))) # generates an array of zeroes, 2 rows, 3 columns in shape
#2
print(np.random.random((4,5)))
#3
print(np.arange(-3,4)) # creates an array of numbers using the tuple as a range
print(np.arange(4))
print(np.arange(-2,7,2))
# np.arange is useful for plotting in matplotlib



















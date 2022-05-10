dic = {1: "me", 2:"you", 3:"we", 4: "us"}

for i, item in zip(dic.keys(), dic.values()):
    print(i,"is", item)

print("\n")

#enumerate
for i, item in enumerate(dic):
    print(i,"/", item)

print("\n")

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

for l,x,y,z in zip(labels, x_coord, y_coord,z_coord):
    print(l,x,y,z)

print("\n")

#zipping into a dictionary
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
cast = dict(zip(cast_names, cast_heights))
print(cast)

print("\n")

#Unzipping
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
names, heights = zip(*cast)

print(names)
print(heights)

print("\n")


#enumerate

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, c in enumerate(heights):
    cast[i] = cast[i] + " " + str(c)

print(cast)























from bs4 import BeautifulSoup
with open("modrosah_website.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
# printingthe whole page
print(doc.prettify())

# priting a particular tag (prints the first tag in the html)
p_tag= doc.p
print(p_tag)
print("\n")

#printing only the content in the tag
print(p_tag.string)

#changing the content of a tag
p_tag.string = "Welcome to Modrosah's site"
print(p_tag.string)
print("\n")

# priting all of a particular tag
p_tags= doc.find_all('p')
print(p_tags) # prints all in a single list
print("\n")

for x, tag in enumerate(p_tags):
    print(x, ':', tag)
    print("\n")
print(p_tags[3]) # selects the fourth p-tag
print(p_tags[3].a) # selects the a-tag nested in the fourth p-tag

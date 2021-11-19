# Read in a plural word, and print out its singular form. For example, "boxes" would become "box". 

# "camel case" identifier format
numberOfStudents = 38
# Varible names can contain letters, digits, and _ characters, but CANNOT begin with a didgit! They're also case-sensitive: Students is a different varible than students

numberOfStudents = "Twenty-five"

plural_word = input("Please enter a plural word to process: ")

if plural_word.endswith("es"):
    single_form = plural_word[:-2] # remove the "es" at the end
elif plural_word.endswith("s"):
    single_form = plural_word[:-1]
else:
    single_form = plural_word

print("The singluar form of", plural_word, "is", single_form)

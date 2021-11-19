# Get a name from the user in either "first last" format or "last, first" format and print both parts of the name

fullname = input("Please enter a full name: ")

# Remove any leading and trailing spaces
# strip() works from both ends of the string inward, stopping when it encounters a character that is NOT in the list to remove
fullname = fullname.strip(' ')


comma_loc = fullname.find(',')

if comma_loc == -1: # No comma, so "first last"
    space_loc = fullname.find(' ') # Find a space
    firstname = fullname[:space_loc] # all before space
    lastname = fullname[space_loc+1:] # all after space
else:
    lastname = fullname[:comma_loc] # all before comma
    firstname = fullname[comma_loc+2] # all after comma and following space

print("Your first name is", firstname)
print("Your last name is", lastname)
print() # print a blank line when we're done

    

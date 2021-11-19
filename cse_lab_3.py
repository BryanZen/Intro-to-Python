string = "Alan Turing"
odd_string = string[::2]
even_string = string[1::2]
new_string = odd_string + even_string
print(new_string)


string_1 = "Editing source code involves testing, analyzing, refining, and sometimes coordinating with other programmers on a jointly developed program."
string_2 = string_1.replace("ing", "")
ing = string_1.count("ing")
string_ing = ing * "ing"
string_end = string_2 + string_ing
print(string_end)

directory = input("String input: ")
name = directory.split()
name_is = name[-1] + " is a "

if directory[0] == "d":
    name_is += "directory"
else:
    name_is += "file"
print(name_is)

if directory[1:4] == "rwx":
    owner = "Owner has read, write, and execute permissions"
    print(owner)
if directory[1:4] == "rw-":
    owner = "Owner has read and write permissions"
    print(owner)
if directory[1:4] == "r--":
    owner = "Owner has read permission"
    print(owner)
if directory[1:4] == "r-x":
    owner = "Owner has read and execute permissionsprint(owner)"
    
if directory[4:7] == "rwx":
    group = "Group members have read, write, and execute permissions"
    print(group)
if directory[4:7] == "rw-":
    group = "Group members have read and write permissions"
    print(group)
if directory[4:7] == "r--":
    group = "Group members have read permission"
    print(group)
if directory[4:7] == "r-x":
    group = "Group members have read and execute permissions"
    print(group)

if directory[7:10] == "rwx":
    world = "World users have read, write, and execute permissions"
    print(world)
if directory[7:10] == "rw-":
    world = "World users have read and write permissions"
    print(world)
if directory[7:10] == "r--":
    world = "World users have read permission"
    print(world)
if directory[7:10] == "r-x":
    world = "World users have read and execute permissions"
    print(world)
print() 

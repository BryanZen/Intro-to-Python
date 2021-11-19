# Read two strings from the user. Remove the *last* occurance of each letter in the second string from the first string.
#
# For example, given "The Avengers" and "Thor", we would get "e Avengers" (We removed "T", "h", and "r" -- "o" wasn't present)

main_string = input("Please enter some text: ")
to_remove = input("Enter a string to extract: ")

index = 0 # current position in to_remove

while index < len(to_remove):
    target_char = to_remove[index]
    position = main_string.rfind(target_char)
    if position != -1:
        # target_char is present in main_string
        main_string = main_string[:position] + main_string[position = 1:]
    index = index + 1 # move to next index

print(main_string)

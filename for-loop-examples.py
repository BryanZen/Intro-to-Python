# Use for loop to print out the characters of a string, with each one multiplied by its index value + 1 (i.e., 1st character appears once, 2nd character twice, and 3rd thrice, etc.)

text = input("Please enter some text to process: ")

# Count up through the indices of the 'text' varible
for idx in range(len(text)):
    # idx is the index of the current character
    multiplied = text[idx] * (idx + 1) # Create (idx + 1) copies of the character at position idx (e.g., if idx is 0, we create a string with 1 copy of the character at index/ position 0 in the 'text')

    print (multiplied)

print ("----")

message = input("Enter a string to extend: ")

# For loops don't run longer if their sequence increases in size as they execute
for letter in message:
    print (letter)
    message = message + " Bruh"

print("message is now:", message)

print()
# However, they *do* have problemd if the sequence gets shorter while the loop is in progress

m = "Hello, world!"

print("Original string:", m)

for character in m:
    print(character)
    m = m[0:-1] # Remove the last character of m

print("m is now:", m)
print()

# Reset to use index values
m = "Hello, world!"

print("Original string:", m)

for i in range(len(m)):
    print(m[i])
    m = m[0:-1] # Remove the last character of m
    print("i is",i," and len(m) is", len(m))

print("m is now:", m)
print()

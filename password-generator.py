# Generate a semi-random password based on the following rules:
# 1. Start with a sentence or phrase.
# 2. The password begins with a random integer.
# 3. The password ends with a random symbol.
# 4. The middle of the password is made up of the first letter of each word from the sentence.
# 5. The password has a minimum required length and must contain both uppercase and lowercase letters. We can also optionally "ban" certain symbols.

import random, string

# Parenthesis like ( and ) are used to indicate a function ( or a tuple )
# Square brackets like [ and ] are used to surround a list
# Curly braces like { and } are used to surround a dictionary

# Get a list of words based on a user-entered phrase
def get_words():
    pieces = [] # Create an empty list. This forces our input loop to execute at least one time

    while len(pieces) < 2: # We need at least a 2-word phrase
        phrase = input("Please enter a starting sentence or phrase: ")
        pieces = phrase.split() # Produces a list of all the words in 'phrase'

    return pieces

# Create a string based on the first letter of each string in a list
def get_first_letters(words):
    result = ""

    for item in words:
        result += item[0]

    return result

# The Caesar cipher (named after Julius Caesar) is a simple substitution cipher; each letter in the plaintext (original message) is replaced with the letter 3 positions ahead of it in the alphabet (we "wrap around" when we go past "z"). For example, "a becomes "d", and "y" becomes "b".
# The Vigenere cipher extends this by shifting each character by a different amount, based on a secrete key (every possible key letter represents a different shift amount).

import string

plaintext = input("Please enter the message to encipher: ")
shift = int(input("What's the shift amount? "))

ciphertext = ""

# plaintext = plaintext.upper() # normalize by making every letter uppercase
# plaintext = plaintext.lower() # normalize by making every letter lowercase

for character in plaintext:
    if character in string.ascii_uppercase: # Only apply shift to letters
        old_code = ord(character) # Get character code
        new_code = old_code + shift
        # Check to see if we need to "wrap around"
        if shift > 0 and new_code > ord("Z"):
            new_code = new_code - 26 # Subtracting 26 restarts at "A"
        elif shift < 0 and new_code < ord("A"): # We shifted too far left
            new_code = new_code + 26 # Restart from "Z"
        ciphertext = ciphertext + chr(new_code)
    elif character in string.ascii_lowercase: # Only apply shift to letters
        old_code = ord(character) # Get character code
        new_code = old_code + shift
        # Check to see if we need to "Wrap around"
        if shift > 0 and new_code > ord("z"): # Too far right
            new_code = new_code + 26 # Restart at "a"
        elif shift < 0 and new_code > ord("a"): # Too far left
            new_code = new_code + 26 # Restart at "z"
        ciphertext = ciphertext + chr(new_code)
    else: # Deal with non-letter characters
        ciphertext = ciphertext + character # Just add the character as-is

print("The enciphered message is", ciphertext)

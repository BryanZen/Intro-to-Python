# DNA strings consist of 4 bases: A, C, G, T, each of which pairs to a "complememtary" base: A and T pair together, and C and G pair together.

# The complement of a DNA strand is another base sequence where each base in the original strand has been replaced by its complementary partner (e.g., all the A's from the original strand are T's in the complement). For example, the complement of ATTGC is TAACG

# The reverse complement of a DNA strand is just its complement, but with its order reversed. For example, the reverse complement of ATTGC is GCAAT

# Strategy: use 'placeholder' characters to temporarily substitute for bases while we replace them with their complements.

dna = input("Enter the original DNA sequence: ")
dna = dna.upper() # convert to all uppercase

# Generate the compliment, using W, X, Y, and Z as substitutes for A, C, G, and T, respectively. Then we can switch them back.

complement = dna.replace('A','W')
complement = complement.replace('T','Z')
# restore the As and Ts
complement = complement.replace ('W','T')
complement = complement.replace ('Z','A')

complement = complement.replace('C','X')
complement = complement.replace('G','Y')
# restoration step
complement = complement.replace('X','G')
complement = complement.replace('Y','C')

print("Original:          ", dna)
print("Complement:        ", complement)
print("Reverse complement:", complement[::-1])
print() # Add blank line at the end


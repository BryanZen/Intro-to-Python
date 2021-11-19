words = input("Please enter some words: ")
word_list = words.split()
l_word = ""

for word in word_list:
    if len(word) > len(l_word):
        l_word = word        
print(l_word)

print()

joke = input("Please enter old Unix ^H joke: ")
pre = ""
suf = ""
n = joke.count("^H")

while n != 0:
    cut_here = joke.find("^H")
    pre = joke[:cut_here - 1]
    suf = joke[cut_here + 2:]
    joke = pre + suf
    n -= 1
    if n == 0:
        break
    
print(joke)
        
    

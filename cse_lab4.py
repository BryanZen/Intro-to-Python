a = int(input("Input a positive integer: "))
print("The input value", a , "should produce the following output: ")

for b in range (1, a + 1):
    if a % b == 0:
        print(int(a / b))

num = input("Input a positive integer: ")
c = int(num)
d = [c]

print()

while c != 1:
    if c % 2 == 1:
        c = (3 * c) + 1
        d.append(c)
    else:
        c = c/2
        d.append(c)
     
e = len(d)
print('The starting value', num  ,'produces the output', e ,'(internally, it generates the sequence', list(d), ').')

print()

lower = int(input("Input a positive non-zero integer: "))
upper = int(input("Input a positive non-zero integer greater than the last one: "))
number_string = ""

x = range(lower, upper + 1)
for n in x:
    if str(n).find("7") >= 0:
        number_string += str(n) + " "

print(number_string)

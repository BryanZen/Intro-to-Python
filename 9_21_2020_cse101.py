Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> "This is a string"
'This is a string'
>>> a = 'This is a string'
>>> type(a)
<class 'str'>
>>> This is a string
SyntaxError: invalid syntax
>>> items = "spam, eggs, spam, spam, spam, spam"
>>> "spam" in items
True
>>> "Spam" in items
False
>>> "pancakes" in items
False
>>> "a" in items
True
>>> len(items)
34
>>> test = "a b c"
>>> len(test)
5
>>> test.count('a')
1
>>> items.count('spam')
5
>>> items.len()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    items.len()
AttributeError: 'str' object has no attribute 'len'
>>> if len(items) > 10:
	print("You entered too many characters!")

	
You entered too many characters!
>>> "Hello, " + "world!"
'Hello, world!'
>>> name = input("Hi! What's your name? ")
Hi! What's your name? Bryan
>>> 
>>> print("How's it going, " + name + "?")
How's it going, Bryan?
>>> print("How's it going,", name, "?")
How's it going, Bryan ?
>>> name * 3
'BryanBryanBryan'
>>> text = input("Enter some text: ")
Enter some text: Yo Mum
>>> if len(text) < 40:
	difference = 40 - len(text)
	padding = ' ' * difference
	text = padding + text

	
>>> Print(text)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    Print(text)
NameError: name 'Print' is not defined
>>> print(text)
                                  Yo Mum
>>> padding
'                                  '
>>> sample = "Hi my name is Bryan Zen, I am a freshman in Dual Language"
>>> sample[-60]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    sample[-60]
IndexError: string index out of range
>>> sample[0]
'H'
>>> sample[-1]
'e'
>>> len(sample)
57
>>> sample[58]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    sample[58]
IndexError: string index out of range
>>> sample[57]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    sample[57]
IndexError: string index out of range
>>> sample[56]
'e'
>>> sample[-57]
'H'
>>> sample[0:56]
'Hi my name is Bryan Zen, I am a freshman in Dual Languag'
>>> sample[0:57]
'Hi my name is Bryan Zen, I am a freshman in Dual Language'
>>> sample.find("Bryan")
14
>>> sample[14]
'B'
>>> sample[14:18]
'Brya'
>>> sample[14:19]
'Bryan'

>>> sample.find('a', sample.find('a'))
7
>>> sample.find('a', sample.find('a') + 1)
17
>>>  first_a = sample.find('a')
 
SyntaxError: unexpected indent
>>> first_a = sample.find('a')
>>> first_a
7
>>> second_a = sample.find('a', first_a +1)
>>> second_a
17
>>> 'tweet'.find('t','tweet'.find('e'))
4
>>> sample
'Hi my name is Bryan Zen, I am a freshman in Dual Language'
>>> a = sample.find('a')
>>> a
7
>>> sample2 = sample[a+1]
>>> sample2
'm'
>>> e2 = sample2.find('a')
>>> e2
-1
>>> a2 = sample2.find('a')
>>> a2
-1
>>> sample[:7]
'Hi my n'
>>> sample[:]
'Hi my name is Bryan Zen, I am a freshman in Dual Language'
>>> sample[0:30:2]
'H ynm sBynZn  m'
>>> sample.rfind['a']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    sample.rfind['a']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> sample.rfind('a')
54
>>> 
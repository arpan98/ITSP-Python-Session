# Basic Python Commands

## imports
`import <name_of_library>` - Imports the *entire* library named `name_of_library` <br>
`from <library> import <module>` - Imports *only* the module `module` from `library`.

## Input from the user

### Python 2.x
`raw_input()` - Takes input from the user in the form of a string. <br>
`input()` - Evaluates the input

	>>> x = input()
	"hello"

	>>> y = input()
	x + " world"

	>>> print y
	hello world

### Python 3.x
`raw_input()` has been removed and `input()` serves the purpose of `raw_input()`, that is, it takes input as a string.

## print
`print "Some text"` - Prints "Some text". <br>
`print("Some text")` - Prints "Some text".

## Comments
`# Some comment` - `#` is used to denote a comment.

	'''
	This is a big multiline comment
	Written in today's python session.
	'''
Three single-quotes(`'`) can be enclosed around a *block* comment.

## if...elif...else
	if <condition>:
		statements...
	elif (<condition2> and <condition3>):
		statements...
	else:
		pass

`elif` is not necessary. <br>
`pass` is used to continue to the next iteration. <br>
Note the colon(`:`) used to denote an indentation block.

## Loops
	for x in range(0, 9):	#Iterates from 0 through 8
		print x
`range(10)` is equivalent to `range(0, 10)`
	
	count = 1
	while count < 20:
		print "Iteration " + str(count)
		count = count + 1

## Multiline statements
	print "For men may come \
		and men may go \
		but I'll go on forever"

Backslash(`\`) is used to tell the Python compiler the line has not yet ended.

## String processing	
	>>> string = 'Alice,Bob,Candice,Darwin,Elvis'
	>>> print string.split(",")
	['Alice', 'Bob', 'Candice', 'Darwin', 'Elvis']
`str.split(str1)` returns a *list* after splitting the string by `str1`.

	>>> string = 'Hello'
	>>> print string.replace('l', 's')
	Hesso
`str.replace(str1, str2)` returns a string with all occurences of `str1` replaced by `str2`.

	>>> string = '0123456789'
	>>> print string[1:3]
	12

	>>> print string[:5]
	01234

	>>> print string[7:]
	789
`string[start:end]` returns the substring from index `start` to `end`. <br>
By default `start` and `end` are taken to be first and last character indices.

## File Handling
	
	filename = 'myfile.txt'
	with open(filename, 'r') as f:		#'r' signifies read-mode
		for line in f:
			print line
`line` is an inbuilt iterator in Python that iterates over the lines of a file.

	filename = 'myfile.txt'
	with open(filename, 'r') as f:
		data = f.readlines()
		print data
`data` will be a list of all the lines in the file.

	filename = 'myfile.txt'
	with open(filename, 'w') as f:
		f.write("Hello world")


## Miscellaneous

#### len
	>>> print len([1,2,3])
	3

	>>> print len("Hello")
	5

#### try...except
`try...except` is used to catch an exception when we know some piece of code might malfunction.
	
	try:
		x = int(raw_input("Enter a number - "))
		print x
	except ValueError:
		print "That was not a valid number!"

#### Running simple terminal commands
	
	import os
	os.system("echo 'Hello World'")


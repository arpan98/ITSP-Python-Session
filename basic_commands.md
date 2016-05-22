# Basic Python Commands

## imports
`import <name_of_library>` - Imports the *entire* library named `name_of_library` <br>
`from <library> import <module>` - Imports *only* the module `module` from `library`.

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

## For loop
	for x in range(0, 9):	#Iterates from 0 through 8
		print x

## Multiline statements
	print "For men may come \
		and men may go \
		but I'll go on forever"

Backslash(`\`) is used to tell the Python compiler the line has not yet ended.

## String processing	
	$ string = 'Alice,Bob,Candice,Darwin,Elvis'
	$ print string.split(",")
	['Alice', 'Bob', 'Candice', 'Darwin', 'Elvis']
`str.split(str1)` returns a *list* after splitting the string by `str1`.

	$ string = 'Hello'
	$ print string.replace('l', 's')
	Hesso
`str.replace(str1, str2)` returns a string with all occurences of `str1` replaced by `str2`.

	$ string = '0123456789'
	$ print string[1:3]
	12

	$ print string[:5]
	01234

	$ print string[7:]
	789
`string[start:end]` returns the substring from index `start` to `end`. <br>
By default `start` and `end` are taken to be first and last character indices.

## Miscellaneous
#### len
	$ print len([1,2,3])
	3

	$ print len("Hello")
	5
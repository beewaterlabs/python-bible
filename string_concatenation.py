#string_concatenation

A = "part one"
B = "part two"
A + B
'part onepart two'
A* 3
'part onepart onepart one'
"=" *20
'===================='
print("TITLE")
TITLE
"=" *20
'===================='

A = "part
SyntaxError: unterminated string literal (detected at line 1)
A = "part"
B = 1
A + B
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    A + B
TypeError: can only concatenate str (not "int") to str
A + str(B)
'part1'

# concatenation without using str /\, using the format function

"{} - {}".format(A,B)
'part - 1'
"{1} - {0}".format(A,B)
'1 - part'




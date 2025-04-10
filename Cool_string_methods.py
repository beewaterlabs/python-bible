# Cool string methods:

"hello".count("e")
1
test = "happy birthday"
text = "happy birthday"
text.count("a")
2
text.count("day")
1
x = "Happy Birthday"
x.lower()
'happy birthday'
x.upper()
'HAPPY BIRTHDAY'
x
'Happy Birthday'
x = x.upper()
x
'HAPPY BIRTHDAY'
x.lower()
'happy birthday'
x = x.lower()
x
'happy birthday'
'happy birthday'
'happy birthday'
x.capitalize()
'Happy birthday'
x
'happy birthday'


x.title()
'Happy Birthday'
x = x.title()
x
'Happy Birthday'

x.islower()
False
x.upper()
'HAPPY BIRTHDAY'
x.isupper()
False
x.istitle()
True
x.isdiget()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x.isdiget()
AttributeError: 'str' object has no attribute 'isdiget'. Did you mean: 'isdigit'?
x.isdigit()
False
"123".isdigit()
True
y = "happybirthday123"
y.isalnum()
True
y = "happybirthday!123"
y.isalnum()
False
x.isalpha()
False
x
'Happy Birthday'
"abcd".isalpha()
True

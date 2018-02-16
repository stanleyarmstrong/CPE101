# Lecture Notes Friday Week 6

As always the more in depth notes will be linked [here](https://polylearn.calpoly.edu/AY_2017-2018/pluginfile.php/526808/mod_resource/content/1/csc101stud_chap6Strings.pdf).

If you missed last class like I did my good friend helped us out by taking notes last class and those notes will be linked [here](https://github.com/eric-newcomer/cpe101notes/blob/master/notes/week6day2.md)

## Chapter 6 Strings

### Chapt 6.1.1: How does a computer store characters?

Each character corresponds to a unique number and vice versa

There is mapping between numbers and characters: ASCII, Extended ASCII, and Unicode (Python)

There is no easy way to specify vowels

Way to check vowels:

```Python
vowels = 'aeiouAEIOU'
if c in vowels


count = 0
for c in my_str:
    if c in vowels:
        count+=1
print(1)
```
The difference between uppercase and lowercase is always 32. So if you need to convert from upper to lower case you either add or subtract 32 to change the character.

```Python
delta = ord('a') - ord('A')
ustr = ''
for c in mystr:
    if ord('a') <= ord(c) <= ord('z'):
        ustr = ustr + chr(ord(c) - 32) #always a new string is created
    else:
        ustr = ustr + c #always a new string is created
print(ustr)

```

Better solution
```Python
clist = []
for c in mystr:
    if ord('a') <= ord(c) <= ord('z'):
        c.list(chr(c) - 32)
    else:
        clist.append(c)
ustr=''.join(clist) #String method, takes in a sequence for a parameter
```

### 6.3 String function - Methods

1. '@' contained in my_str

```Python
found = '@' in my_str
found = my_str.find('@') #returns the index of the first occurence of in my_str
```
.find() - return the lowest index in the string where substring sub is found within the slice

.index() - return error when the substring sub is not found

.isupper() - Return True if all cased characters are upper case

.isdigit() - checks to see if a string has a digit int

```python
for i in my_str

```

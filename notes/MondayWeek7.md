# Monday Week 7

Things to note: Midterm coming up this **Friday** and Project 4 due next **Monday**

As always for more in depth notes they will be [here](https://polylearn.calpoly.edu/AY_2017-2018/pluginfile.php/526808/mod_resource/content/1/csc101stud_chap6Strings.pdf)

That's a good enough introduction so let's just jump into it.

## Chapter 6

### Chapter 6.3.6: String Functions

Function split example:

```Python
str1 = '21-85-731-2'
strList = str1.split('-') #['21', '85', '731', '2']
```

.split('-') returns a list of strings using '-' as a delimiter

.split() delimiter is any whitespace and empty strings are removed

### Chapter 6.4: Formatted Output

Old Way
```python
str1 = '%6d%9d'%(k, m) #format specifiers and a tuple of values

```

A different method should be used

Replacement fields

Example

```python
str1 = 'The sum of {0} and {1} is {2}'.format(3, 4, 7) #a, b, c

#Output
#str1 = 'The sum of 3 and 4 is 7'
```

Field with Decimals, Alignment

{0: 6.2f}
6 is field width

.2 decimals

f indicates floating point value

Special Cases:
- alignment

 '>' right

< left

-integer values
x : hexadecimal
b : binary
-fill spaces

### 6.5: Command Line Arguments

Module sys provides a variable argv - a variable of type list that contains the command line arguments as string

Variable sys.argv

len(sys.argv) >= 1

The first element is the script name

```python

import sys
print('Program: ', sys.argv[0])
mysum = 0
for k in range(1, len(sys.argv)):
    sum += float(sys.argv[k])
if len(sys.argv) == 1:
    print('No numbers')
else:
    print('Sum' , mysum)
```

```python
first = True
for element in sys.argv:
    if first:
        first = false
    else:
        mysum += float(element)

```

3rd solution

```Python
for element in sys.arg[1: ]:
    mysum += float(element)

```

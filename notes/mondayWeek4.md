# Notes Monday Week 4

First midterm is on Friday 2/2 may vary if you are in a different section of CPE101

Things included in the midterm are linux-commands, Python: functions, if-else, and loops, and TestCases

Also as always the more in depth notes will be linked [here](https://polylearn.calpoly.edu/AY_2017-2018/pluginfile.php/508641/mod_resource/content/1/csc101stud_chap4_Loops.pdf

Another great resource for information formatting strings will be located [here](https://pyformat.info/)

## 4.2 Formatted Output
```python
print(k , k2, k3)
```
numbers are printed and are separated by one space

table is not right aligned because numbers become larger

```Python
print('%3d%5d%6d' % (k , k2 , k3))

```
First part: formats the string

Second part: string format operator

Third pard: a tuple of numbers

%3d: format specifier that creates a string for an int and use 3 columns and write right-aligned it ends with d,e,f,s

## 4.3 for-loop

```python
for k in range(1,6):
    statement

```

k is the variable name

for and in are Python keywords

range is a built in function

returns an object that produces a list of numbers

range(start, end)

start, start+1, start+2, ... <end

each number of the sequence is assigned to k and then the body is executed

raange(start, end , step)

body of loop is executed for each number that is returned by range

only integer values for loop the step modifier

can also decrement values in the range

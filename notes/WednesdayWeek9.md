# Wednesday Week 9

Hello everybody, as you may know the notes were not taken on Monday as I was in the process of changing my major from Computer Engineering to Computer Science. Now since that is finished, I am back taking notes. Since you are missing the notes from Monday, I'll be linking the notes from my friend [Eric Newcomer](https://github.com/eric-newcomer/) located  [here](https://github.com/eric-newcomer/cpe101notes/blob/master/notes/week9day1.md).

So let's just jump into this!

## Chapter 10: Sorting

Problem:

A list of elements is given
```Python
l  = [e1, e2, e3, e4, ...]

```
Sort the elements in ascending or descending order

To do this, it must be possible to compare two elements with each other.

#### Two Types of Solutions

1) the elements within the list are reordered and no new list is created

```Python
l.sort()
l.sort(reverse = True)
```

2) a new list is created where the elements of the 'old' list are ordered, the original list is not modified

```Python
newl = sorted(l)
newl = sorted(l, reverse = True)
```

### 10.1 Sorting Strings

String are sorted alphabetically using the ASCII-Code

```python
l = ['A', 'B', '3', 'a']
l.sort()
# Result
l = ['3', 'A', 'B', 'a']
```

#### Examples:

1)
```python

l = ['A', 'Ab', 'Z', 'Aa', '1a']
l.sort()
# result
l = ['1a', 'A', 'Aa', 'Ab', 'Z']
```
Take the first character, if the first characters are the same, take the second character

2)
```Python
l = ['100', '2', '80', '500', '1', '10']
l.sort()
# Result
l = ['1', '10', '100', '2', '500', '80']
```

### 10.2 Sorting - Parameter Key

sort string ignoring case

- 'A', 'a' are the same
- 'B', 'a' : 'a' < 'B'

```python
l = ['A', 'B', '3', 'a']
l.sort(key = str.lower)
```
do not compare elements using e1 < e2, but str.lower(e1) < str.lower(e2)

#### Example

Sort a list of strings according to the length of the strings

```python
l.sort(key = len)
```
- sort a list of int-strings by value

```Python
c = ['100', '2', '80', '500', '1', '10']
c.sort(key = int)
# The function int must be applicable to all elements in the list
```

### 10.3 List of Lists and Structured Data Types

```Python

l = [[3,4,7] , [1,5,4]]
#sort using the value at a given index of the inner list

l = [e1, e2, e3, ..., en]
#all elements are of type Point, Earthquake, Rectangles

```
Use a certain attribute for comparison all elements must have this attribute

Module: operator

attrgetter(name of an attribute)
itemgetter(index)

```Python
l.sort(key = attrgett('x'))
l.sort(key = itemgetter(1))
```

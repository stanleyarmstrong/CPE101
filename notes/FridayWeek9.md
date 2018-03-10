# Friday Week 9

Little bit of an intro. Project 5 is due **Sunday at 11:59:59pm**. That's all you need to know. I'll be linking the more in-depth notes soon. So check on that if you check the repo regularly. So let's just jump into this. For other notes check out my friend [Eric Newcomer's](https://github.com/eric-newcomer/) [notes](https://github.com/eric-newcomer/cpe101notes/blob/master/notes/week9day1.md).

## Chapter 10: Sorting

### 10.4: Sorting Algorithms

Write a function that sorts the elements of a list of integer values

Example :

 ```Python
 l1 = [7, 9, 3, 6, 8]

 ```

 Selection Sort

 Step 1:

 Find the smallest element and swap it with the first element

 ```Python
 min_index = 0, 2
 min_value = 7, 3
 ```

 Step 2:

 Find the smallest element starting with element number 2 and swap with the second element

 ```Python
 min_index = 3
 min_value = 6
 ```

 Step 3:

 The actual algorithm:

 ```Python
 def selection_sort(l1)
    for m in range(len(list - 1)):
        min_index = m
        for n in range(m+1, len(l1)):
            if l1[n] < l1[min_index]:
                min_index = n
                #find minimum in a sublist
        temp = l1[m]
        l1[m] = l1[min_index]
        l1[min_index] = temp

 ```

 Shortcut for swap

 a,b = b,a

 ```python
 def selection_sort(l1)
    for m in range(len(list - 1)):
        min_index = m
        for n in range(m+1, len(l1)):
            if l1[n] < l1[min_index]:
                min_index = n
                #find minimum in a sublist
        l1f[m], l1[min_index] = l1[min_index], l1[m]
    return l1
 ```

 Questions:
 - What happens for lists with zero elements?

### 10.5 Performance

2 approaches

-theoretical:

    count the number of comparisons for a list N elements

-comparison:

    Sort a list with 1000 and 2000 elements and calculate the cpu_time

l = [0] * 1000

Generate a list with random number

Module Random

Creat a list of int_values

```python
import random

m = [0]
for k in range(1000)
    m.append(random.randint(0,1000))
#for list
```

Improvements:

experiments with

    10, 100, 1000, 10000, ...
    100, 200, 400, 800, ...

### Project 5

1) Dictionary

A list is a sequence of elements, the elements are accessible by indices

A dictionary is a container where elements are accessible via keys; a dictionary contains key-value pairs

```Python
d = {'Bob': 1231, 'Joe': 1257, 'Eve': 2357}
```

d is a dictionary with 3 elements to get Joe telephone numbers

```python
d['Joe'] = 1257
```

Keys must be unique

A dictionary is like a list where the indices may be any object

A dictionary is a map

'Bob' -> 1231

'Joe' -> 1257

```Python
d = dict()
d = {} #does the same thing as above line

d['Bob'] = 1231
d['Joe'] = 1257
d['Eve'] = 2357
```

Earthquake:

A dictionary with the following keys

    -'Type'
    -'meter-data'
    -'features' the value of element with key feature is a list of dictionaries each dictionary describes an earthquake
    -'bbox'

Feature is a dictionary that describes an earthquake that has the following keys

    type
    properties - contains mag, place, and time
    geometry - contains latitude and longitude

    If f is a feature

    f['properties']['mag'] -> mag
    f['geometry']['coordinates'] -> [0] longitude [1] latitude

```Python

def add_new_quakes(quakes, newquakes_dict):
    new_quakes = False
    list_of_earthquakes = newquakes_dict['features']
    for f in list_of_earthquakes:
        quake = quake_from_feature(f)
        if not in quakes:
            new_quakes = True
            quakes.append(quake)
    return new_quakes
    
```

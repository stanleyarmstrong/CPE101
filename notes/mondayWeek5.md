# Monday Week 5

As always more in depth notes will be linked here [ for and while loops](https://polylearn.calpoly.edu/AY_2017-2018/pluginfile.php/508641/mod_resource/content/1/csc101stud_chap4_Loops.pdf) and here [for lists](https://docs.python.org/3/tutorial/datastructures.html). The link for list will be updated when the link is available on Poly Learn.

## Chapter 5 List

### Built In Data Type list

**list** is a built-in data type to store a **sequence** of values of any type

A **sequence** is an **ordered** (there is a first element, second element, ..) collection of items

List operator **[]**

Zero based indexing

### 5.2 List Operations and Functions

#### 5.2.1 Creating Lists

```python
colors = ['green' , 'blue' , 'red'] #list operator

```
Creates a list with 3 elements

```Python
colors = []
colors.append('green')
colors.append('blue')

```
Colors is the name of a list

['green' , 'blue']

.append() adds an element at the end of the list

create a list with many elements

```Python
squares = []
for k in range(1, 101):
    square.append(k**k)
```
Squares elements : [1 , 4 , 9, ..., 10000]

Get the number of elements

```Python
len(squares) #Built in function that takes in the list named Squares

```

####5.2.2 Access all elements of a List

a) print all elements of Squares

```Python
for k in (len(squares)):
    print(squares[k])

```
b) use the in keyword
```python
for item in squares:
    print(item)

```
Meaning of B

    assign first element of the list to item and execute the body
    then assign the second element of the list to item and execute the body

b)write a function to calculate the mean of a list of floats
```python
def mean(times):
    tsum = 0
    for item in times:
        tsum += items
    tmean = tsum / len(times)
    return tsum


```

Call function mean

```Python
meanvalue = mean(times)

def mean(times):
    if len(times) == 0:
        return None
    else:
        return sum(times) / len(times)

```
Sum is a built-in function

c) access the last elements

```Python
times[-1] #last element
times[-2] #second to last element
```

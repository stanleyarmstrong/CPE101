# Notes Monday Week 6

As always more in depth notes will linked [here for lists]() and [here for strings]()

## 5.4 Map-Filter-Pattern List Comprehension

Map Pattern:

    a list is given
    apply an operation (expression) on each element of the list - get a new
    value for each element of the given list
    put all new values into a new list

```Python
#Without List Comprehension
def map_f2c(fList):
    cList = []

    for fItem in fList:
        cItem = f2c(fItem)
        cList.append(cItem)
    return cList

#With List Comprehension
cList = [ f2c(x) for x in fList]

```

List Comprehension = [expression for <item> in <list>]

List Comprehension Filter Pattern:

[expression for <item> in <list> if <condition>]


```Python
sq = [x**2 for x in range(1 , 101)]

```

Filter Pattern:

    a list is given
    apply a Boolean expression on each element of the list
    put all elements for which the boolean expression is True into a new list

List Comprehension Filter Pattern:

[expression for <item> in <list> if <condition>]

Get all values between 10 and 20
```python
positive = [x for x in myList if 10 < x < 20]

```
Get all square values between 10 and 20
```python
sq = [x ** 2 for x in myList if 10 < x < 20]

```
## 5.5 Tuples

Tuples are similar to lists however once created they cannot be modified

Tuples are **immutable**

```python
t = (1,2,3)
t = 1,2,3
x = t[2]
t[2] = 14 #Error
```

Note:

To make a Tuple with only one value you have to t = 5, or t = (5,)

Example:

ax^2+ bx + c

```Python
def solve(a, b, c):
    d = math.sqrt(b*b - 4*a*c)
    x1 = 0.5 * (-b + d)/a
    x2 = 0.5 * (-b - d)/a
    return x1 , x2

s = solve(3,4,5) #s is a tuple

s1,s2 = solve(3,4,5) #s1 is assigned to x1 and s2 is assigned to x2
```

Application:

```Python
def assertListAlmostEqual(l1 ,l2):
    for el1, el2 in zip(l1 , l2):

```

## Chapter 6

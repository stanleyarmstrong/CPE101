# Wednesday Week 3: Conditionals continued (Lecture) and (Lab)

As always for more more in depth notes check [here](https://polylearn.calpoly.edu/AY_2017-2018/pluginfile.php/502379/mod_resource/content/1/csc101stud_chap3.pdf)

## 3.2 - 4 Conditionals - Problems

Problem 1:

    Write a function named a max2 that returns a maximum of two numbers

    def max2(a , b):
        if a >= b:
            max = a
        else:
            max = b
        return max
Problem 2:

    Write a function named max3 that returns the maximum of three numbers

    Solution 1:

    def max3(a, b, c):
        if a > b:
            if a > c:
                max = a
            else:
                max = c
        else:
            if b > c:
                max = b
            else:
                max = c
        return max
    Solution 2:
        def max3(a , b ,c):
            if a > b:
                max = a
            else:
                max = b
            if c > max:
                max = c
            return max

    Solution 3:
    def max3(a , b, c):
        max = max2(a, b)
        max = max2(max , c)
        return max

    Solution 4:
    def max3(a , b ,c):
        return max2(max2(a , b) , c)

    Solution 5:
    def max3(a, b , c):
        if (a >= b) and (a >= c):
            max = a
        elif (b >= a) and (b >= c):
            max = b
        else:
            max = c
        return max
## 3.3 Chained Conditionals

```python
if cond-1:
    block-1
elif cond-2:
    block-2
else:
    block
```
Conditions are checked one after another. The **order** of conditions is important

## 3.4 Range Checking

Check whether a number is between 10 and 20

Assume the boundaries are included

```python
if( x >= 10) and (x <= 20):
    block
#python exclusive
if (10 <= x <=20):
    block
if not((x < 10) or (x > 20)):
```

## 3.5.1: Check for Equality

Two values of type int are equal if they have identical values

Two values of type str are equal if they have exactly the same values

### Check for Equality - Data Type Float

In many cases the result of floats can not be predicted. Therefore don't do it

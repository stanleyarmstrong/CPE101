# Wednesday Week 8

Welcome back guys! If you have been following us, you might know that we didn't take notes last class. If you need those
notes the link will be [here](https://github.com/eric-newcomer/cpe101notes/blob/master/notes/week8day1.md). And as always the more in-depth notes will be located [here](https://polylearn.calpoly.edu/AY_2017-2018/pluginfile.php/539896/mod_resource/content/1/csc101stud_chap7StructuredDataTypes.pdf).

Final is **March 19th, 7:10-10pm**

I think that's a good enough intro so let's just jump into this.

## Chapter 7

### 7.4 Unit Tests for Structured Data Types

Test the initialization method works correctly

### 7.5 Functions using Structured Data Types

Calculate distance between two points p1 and p2

```Python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p2.y
    distance = math.sqrt(dx**2 + dy**2)
    return distance
```
### 7.6-1 Equality for Structured Data Types

id(obj) - Return the identity ( a kind of serial number) of an object

This is guaranteed to be unique among simultaneously existing objects. (CPython uses the object's memory address)

This is the default for equality

To modify the default meaning of p1 == p2
for objects of type Point add a method __eq__
which comare two objects of type Point with each other
Method __eq__ should return True or false
If methos __eq__ is not implemented standard behavior is carried out

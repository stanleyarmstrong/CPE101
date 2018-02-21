# Wednesday Week 7

Things to note for the 2nd Midterm:

loops

lists

lists and 2d array (list of lists)

strings (chr() ord())

Remember the 2nd Midterm is this **Friday**

As always the more in-depth notes of this lecture will be located [here](https://polylearn.calpoly.edu/AY_2017-2018/pluginfile.php/526808/mod_resource/content/1/csc101stud_chap6Strings.pdf)

That's a good enough intro to me so let's just jump into it.

## Chapter 6

### Chapter 6.6.1: Converting a String into List and vice versa
Common to Strings and Lists

    they are sequences

    iterate over all elements

    slice operator

    many common Methods

    index, find

String is immutable all elements are Strings

String to a List

```Python
my_list = list('Hello') #Converts a string to a list

```

List to Strings

```Python
my_str = ''.join(my_list) #Coverts a list to a string
my_str = '--'.join(my_list) #my_str = 'H--E--L--L--O'
```

Reverse a String

My Solution
```Python
def reverse_str(my_str):
    my_list = list(my_str)
    new_list = []
    for i in range(len(my_list)):
         new_list.append(my_list[len(my_list)- 1 - i])
    new_str = ''.join(new_list)
    return new_str

hello = reverse_str('hello')
print('Hello')
print(hello)
```

Method reverse:

applicable to list

l1.reverse() reverses the elements of the list, no return value

```Python
l1 = ['1' ,'2']
l1.reverse() #l1 is ['2' , '1']


```

Simple Solution for reverse String
```Python
def reverse_str(str):
    lst = list(str)
    lst.reverse()
    return ''.join(lst)
```

## Chapter 7: Structured Data Types (Programmer Defined Data Types)

Create variables that describe

     a point in 2d, 3d, n-d
     a car
     a state in the US
     a student

Each of these items has many properties, that belong together

Need a variable/data type to store these variables

### 7.1: A Point in 2D

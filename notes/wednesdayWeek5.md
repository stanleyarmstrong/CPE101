# Notes Wednesday Week 5

As always more in depth notes will be available [here](https://polylearn.calpoly.edu/AY_2017-2018/pluginfile.php/520751/mod_resource/content/1/csc101stud_chap5Lists.pdf) and a really good resource relating to the content will be available [here](https://docs.python.org/3/tutorial/datastructures.html)

## Chapter 5: Lists

### 5.2.3 Removing an element

method pop(index): removes an element at position index from the list

```Python
nbrs = [10 , 20 , 30]
x = nbrs.pop(1) #[10, 30]
nbrs.pop(1) #[10]
nbrs.pop(1) #error
```
method pop(): removes the last element in the list

###5.2.4 Inserting an element
```python
colors = ['red' , 'green']
colors.insert(1, 'blue' ) #['red' , 'blue' , 'green']
colors.insert(1, 'yellow') # ['red' , 'yellow', 'blue' , 'green']
colors.insert(len(colors) , 'some-color') #appends at the end
```
### 5.2.3 List Reference and Copying List

1) nbrs = [10, 20, 30] State: nbrs -> [10, 20, 30]

2) mynbrs =  nbrs   State: mynbrs and nbrs -> [10,20,30]

3) mynbrs.append(40) State: mynbrs and nbrs -> [10,20,30,40]

There is only one list. Variables nbrs and mynbrs refer to the **same** list

Function list creates a copy of a list

Code referring to built-in function

```Python
nbrs = [10, 20 ,30] #State: nbrs -> [10, 20, 30]
mynbrs = list(nbrs) #State: mynbrs and nbrs -> [10, 20 , 30]
mynbrs.append(40) #State: mynbrs -> [10, 20 ,30 ,40] nbrs -> [10, 20 ,30]
```
Code referring to what happens in the built-in function list(list1)

```Python
def copylist(l1):
    l2 = []
    for element in l1:
        l2.append(element)
    return l2
```
### 5.2.4 Finding Elements

Questions: Is 10 in the list? Get the first index of value 10? How often is 10 in the list? Get all indices with value 10

```Python
l1 = [2, 10, 3 , 5, 10, 7]
if 10 in l1: #is value in list_name returns a boolean true or false
    print('10 is in list')
else:
    print('10 is not in list')
i1 = l1.index(10) #i1 is stored as the index of the value of 10 in list, if it's not in the list it returns an error if the value is not in the not in the list
if 10 in l1:
    n = l1.index(10)
else:
    n = None
```

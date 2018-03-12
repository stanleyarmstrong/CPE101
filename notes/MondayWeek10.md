# Monday Week 10

Some important things to note, **Final is next Monday at 7:10-10** and **Project 6 is due on Friday at Midnight**

## Chapter 9: Exception Handling

Handle program errors- not programming errors

The program is correct, but sometimes errors occur when the program is executed

Example

Earthquake

    webserver is down
    no internet connection

Access to a file
    wrong file name
    file does not exist
    no permission

### 9.1 try-except-mechanism

General Statement

    a rule or an assumption
    ex. every line contains a number
    exceptions to the rule
    some lines are empty or do not contain valid number

Exception Handling provides a flexible mechanism to **detect** an error
and deal with an error at another place

Implementation

```Python
try:
    #block 1
    '''
    code according to rule
    '''
except:
    #block 2
    '''
    code to handle the error
    '''
```

When no errors occur only block 1 is executed

If an error occurs in block 1, the block is immediately left and the program continues with block 2 which must handle the problem.  

### 9.2 Opening a File

```Python

filename = 'numbers.txt'

while True:
    try:
        fin = open(filename, 'r')
        break
    except:
        print('cannot open' + filename)
        filename = input('Enter a file').strip()
```

The finally statement is always executed- whether an error occurred or not

All errors are covered by except statements

```Python

except FileNotFoundError: #covers only the FileNotFoundError

```

### 9.3 Raising Exception

We can not own Exception, but we can create built-in exception

```Python

def calculate(a, b):
    if b == 0:
        raise ZeroDeivisionError()
    if b == 1.0:
        raise ValueError()
    c = a + 1/b
    if c > 100:
        raise OverflowError()
    else:
        return c
    #restrictions: b != 0, b != 1, and the value of c must be <= 100
    #b = 0: ZeroDeivisionError
    #b = 1: ValueError
    #c > 100: OverflowError


```

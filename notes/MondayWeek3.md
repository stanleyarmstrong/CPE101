# CPE 101 Monday Week3 Lecture and Lab

Link to More In Depth Lecture notes: [State Diagrams](https://polylearn.calpoly.edu/AY_2017-2018/pluginfile.php/497467/mod_resource/content/5/csc101stud.pdf) and [Boolean Logic and Conditionals](https://polylearn.calpoly.edu/AY_2017-2018/pluginfile.php/502379/mod_resource/content/1/csc101stud_chap3.pdf)

## Local variables

### State Diagram

used to visualize the state of a program

#### First Program

L7: main- x->2

after:

    x -> 2

    a -> 2

    b -> 4

#### Second Program

After Line 3:

    x -> 2

    a -> 3

    b -> 4

    c -> 12

After Line 8:

    x -> 2

    y -> 12

## Boolean Logic and Conditionals

Arithmetic

          x = 5.0 numbers, infinite

          y = 7.0 operators +, -, *, /, //, %, **

          z = x + y Arithmetic calculation

### 3.1 Boolean Algebra

There are only two values:

    True 1 y

    False 0 n

Relational Operators to assign boolean values: (Example)

    x = 3

    y = 5

    a = (x == y) Test for equality

Relational Operators:
    x > y Greater Than

    x >= y Greater or equal

    x < y Less Than

    x <= y Less Than or equal

    x != y Not equal

    x == y equals

### 3.2 Boolean Operators

3 basic operators:

    logical AND: and 2 operands

    logical OR: or 2 operands

    negation NOT: not 1 operand

Truth Table:

        a    b    (a and b) (a or b) (not a)

        True True   True    True   False

        True False  False   True   False

        False True  False   True   True

        False False False   False  True

#### Conditionals

if condition - Do this if it passes this case

elif condition - Do this if the if statement did not work

else- [Worst Case Scenario](https://www.youtube.com/watch?v=pjosIqtGZKM)

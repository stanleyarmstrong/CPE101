# Notes Wednesday Week 4


**Reminder Midterm is on Friday**

As always more in depth notes will be linked [here](https://polylearn.calpoly.edu/AY_2017-2018/pluginfile.php/508641/mod_resource/content/1/csc101stud_chap4_Loops.pdf)

## Chapter 4.4-1 Nested Loops

A table is printed row by row

Each row is printed from left to right

Pseudocode:

    for all rows r:
        for all columns in row r:c
            print column c
        create a new line

```Python
rows =
cols =

for r in range(rows):
    for c in range(cols):
        print('%3d' % c)

```
### Problem 2

3 nested loops

```python
for h in range(24)
    for m in range(60)
        for s in range(60):
            print('%02d:%02d:%02d' % (h,m,s) )
```
Single Loop

```Python
s= 0
m = 0
h = 0

for k in range(86400):
    s = s+1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h+=1
    print('%02d:%02d:%02d' % (h,m,s) )
```
## Chapter 4.5

Problem: Calculate the square root for a given number x

Iteration:
    xn+1 = 1/2 * (xn + x/xn) (Heron's Method)

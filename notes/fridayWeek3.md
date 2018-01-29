# Friday Week 3 Notes Lecture and lab
**Disclaimer: I was not taking great notes during the lecture**

That being said, as always I'll include the link to the pdf of the notes [here for boolean logic](https://polylearn.calpoly.edu/AY_2017-2018/pluginfile.php/502379/mod_resource/content/1/csc101stud_chap3.pdf) and [here for loops](https://polylearn.calpoly.edu/AY_2017-2018/pluginfile.php/508641/mod_resource/content/1/csc101stud_chap4_Loops.pdf)

## 3.6 Calculations with Boolean Variables

Rules for boolean variables:

    1) not(not a) = -a
    2) not( a and b) = (not a) or (not b) Demorgan's rules(laws)
    3) not(a or b) = (not a) and (not b)

## Chapter 4: Iterations and Loops

While statement

while k is true do these steps until k is false

Once k is false go to the next line after those inside the while loop

### Flow Diagram

Used to visualize a program

### Chapter 4-2: Iterations and Loops

Problem 2:
```python
count = 0
while True:
    k = int(input('Number'))
    if k < 1:
        break #break out of the surrounding while or for loop
        #note break is often used in an if state ment, but the program will jump out of the surrounding while statement
    sq = k * k
    count +=1
print('Processed',count,'number')
```
Problem 3:

Write a program that asks the user to enter a number between 50 and 100 (including boundaries). If the number is not within the range the user is asked again until they input a valid input.

```python
k = -1
while k < 50 or k >100:
    k = int(input('Number: '))

```

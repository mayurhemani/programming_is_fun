## Day 2 Problems for if/elif/else, while/for and lists

Try to solve at least one problem in a day.

### Problem 1
A number is called a *punctured number* if it is divisible by 3, 5, 7 and 9. Write a program to take a number from a user as input, and print if it is a punctured number or not.

*Examples:*

input: 315
output: yes

input: 225
output: no


### Problem 2
German people use the prefix "Frau" for married women and "Fraulein" for unmarried women. We will assume for the sake of this problem that all women above the age of 30 are married. Ask the name and age of a woman in your program as input. And print the name of the person as they are to be addressed.

*Examples*

name: Emily Schenkel
age: 31
output: Frau Emily Schenkel

name: Juta Hammersmark
age: 25
output: Fraulein Juta Hammersmark

### Problem 3
A number can be constructed by repeated multiplication by 10 and adding digits. For example, 0\*10+9 is 9, 9\*10+2 is 92, 92\*10+0 is 920, and 920\*10+1 is 9201.

Also see that the last digit of a number can be obtained by using the mod operator (%) with respect to 10. For example, 1029%10 is 9, which is the last digit. 

Using these two ideas, write a program that reverses the digits of a positive number.

*Examples*
input: 1029
output: 9201

input: 531
output: 135

### Problem 4
Write a program that inputs a list of numbers, creates a new list where the items are reversed and prints the new list.
To take the list of numbers as input, take the first input as the number of numbers (n). After that take the n numbers as input.

*Examples*
input:
5
1
2
3
4
5
output:
[5 4 3 2 1]

input:
3
20
12
43
output:
[43 12 20]

### Problem 5
Take a list of numbers as input and print the sum and average of the numbers. Again, for the list input, take the number of numbers as the first input.

*Examples*

input:
5
1
2
3
4
5
output:
7.5

input:
3
10
20
30
output:
20

### Problem 6
Write a program to take a list of words as input and print them as a sentence with one space between words. Again take the first input to be the number of words. Bonus points if your sentence does not end with a space.

*Example*
input:
5
this
is
a
good
world

output:
this is a good world

input:
3
what
a
world

output:
what a world

### Problem 7
Write a program to take two numbers _a_ and _b_ as input. Print _a_ lines of _b_ stars each.

*Examples*

input:
4
5

output:
\*\*\*\*\*
\*\*\*\*\*
\*\*\*\*\*
\*\*\*\*\*

input:
2
2

output:
\*\*
\*\*


### Problem 8
Consider the following list:
```
alist = ["a", "b", "c", "d", "e", "f"]
```
The *prefixes* that can be created using this list include:
```
a
ab
abc
abcd
abcde
abcdef
```
Write a program to take a list of characters as input (again use the first input as the number of characters). Then print all the prefixes created using that list.

*Examples*

input:
5
x
y
z
w
u
output:
x
xy
xyz
xyzw
xyzwu

input:
3
a
b
c
output:
a
ab
abc



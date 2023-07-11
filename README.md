The point of this program is to demonstrate how a list comprehension program is created and run. It is quite simple and elegant at the same time. I will define what a list comprehension is and why it is used in python programming. 

What is List Comprehension?

It is an alternate way to create a list using methods that allow for a list to be created, such as the use of the range() or a way to extract information or the use of conditional statements, to filter out values from another data set. For example, one can take a full list of names and filter it down to the odd numbers. This can be done via list comprehension. Here is how:

list_ex1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
def list_comp(list_ex1):
    comp_ex1 = [num in num for list_ex1 if num%2 != 0]
    return comp_ex1

Result: [1,3,5,7,9,11,13,15,17.19]

The format for list comprehension is:

var_1 = [var in var for iterable, [optional conditional statement(s)]]

As in both examples, the use of a for loop is applied to the list comprehension due to the nature of how list comprehension works. The neccessity of the for loop is to be able to iterate into the list and create the list at the same time. When compared to the use of appending to a list, it is often cited as one line code that creates results and very well preferred.

In this simple practice coding, I am using a range function to build a list out of a list comprehension code. The point of this coding is to simply ensure that the code works in two ways. The function that it calls from works and that it is filtered into the main function by filtering the name of this file into the main function, by which all functions would be called by the main function. 

Why do we call from the main() function?

It is so that when we call all of our functions, without the use of classes, we are able to get the main function to utilize a file that is called through the main program, in this case, list_comp.py. 
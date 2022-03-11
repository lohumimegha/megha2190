#!/usr/bin/env python
# coding: utf-8

# 1) Why are functions advantageous to have in your programs?
# ANS: Use of functions enhances the readability of a program. A big code is always difficult to read. Breaking the code in smaller Functions keeps the program organized, easy to understand and makes it reusable and easier to update. Functions reduce the need for duplicate code.
# 
# 2) When does the code in a function run: when it's specified or when it is called?
# ANS: Functions are "self contained" modules of code that accomplish a specific task. Functions usually "take in" data, process it, and "return" a result. Once a function is written, it can be used over and over and over again. Functions can be "called" from the inside of other functions.
# 
# 3) What statement creates a function?
# ANS: The “def” keyword is a statement for defining a function in Python. You start a function with the def keyword, specify a name followed by a colon (:) sign. The “def” call creates the function object and assigns it to the name given. You can further re-assign the same function object to other names.
# 
# 4) What is the difference between a function and a function call?
# ANS: Using a function to do a particular task any point in program is called as function call. So the difference between the function and function call is, A function is procedure to achieve a particular result while function call is using this function to achive that task.
# 
# 5) How many global scopes are there in a Python program? How many local scopes?
# ANS: There's only one global Python scope per program execution. This scope remains in existence until the program terminates and all its names are forgotten. 
# Local scope is a characteristic of variables that makes them local (i.e., the variable name is only bound to its value within a scope which is not the global scope).
# 
# 6) What happens to variables in a local scope when the function call returns?
# ANS: When the execution of the function terminates (returns), the local variables are destroyed. A local variable retains its value until the next time the function is called. A local variable becomes undefined after the function call completes The local variable can be used outside the function any time after the function call completes.
# 
# 7) What is the concept of a return value? Is it possible to have a return value in an expression?
# ANS: A return statement is used to end the execution of the function call and “returns” the result (value of the expression following the return keyword) to the caller. The statements after the return statements are not executed. If the return statement is without any expression, then the special value None is returned.
# 
# 8) If a function does not have a return statement, what is the return value of a call to that function?
# ANS: If a function doesn't specify a return value, it returns None . In an if/then conditional statement, None evaluates to False.
# 
# 9) How do you make a function variable refer to the global variable?
# ANS: If you want to refer to a global variable in a function, you can use the global keyword to declare which variables are global.
# 
# 10) What is the data type of None?
# ANS: In Python, None keyword is an object, and it is a data type of the class NoneType . We can assign None to any variable, but you can not create other NoneType objects. 
# 
# 11) What does the sentence import areallyourpetsnamederic do?
# ANS: 
# 
# 12) If you had a bacon() feature in a spam module, what would you call it after importing spam?
# ANS: This function can be called with spam. bacon()
# 
# 13) What can you do to save a programme from crashing if it encounters an error?
# ANS When it encounters an error, the control is passed to the except block, skipping the code in between. Try running the program and it should throw an error message instead of crashing the program.
# 
# 14) What is the purpose of the try clause? What is the purpose of the except clause?
# 
# Except statement catches an exception. It is used to test code for an error which is written in the “try” statement. If an error is encountered, the contents of the “except” block are run.
# The try block lets you test a block of code for errors. The except block lets you handle the error.
# 
# 
# 
# 

# In[ ]:






### Python Basics

### Variables

Variables are often described as containers where you store values. Variables can be used to store anything from simple data types (like integers and strings) to more complex data structures (like lists and dictionaries). You can think of them as labels you attach to values to keep track of them. You can also say that a variable references a certain value.

Let’s try using a variable in `hello_world.py`. Add a new line at the beginning of the file, and modify the second line:

```
message = "Hello Python!"
print(message)
```

Run this program to see what happens. You should see the same output you saw previously:

```
C:\> python hello_world.py
Hello Python!
```

We’ve added a variable named `message`. Every variable is connected to a value, which is the information associated with that variable. In this case the value is the `Hello Python!` text.

When you’re using variables in Python, you need to adhere to a few rules and guidelines. Breaking some of these rules will cause errors; other guidelines just help you write code that’s easier to read and understand. Be sure to keep the following rules in mind when working with variables:

* Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number. For instance, you can call a variable `message_1` but not `1_message`.
* Spaces are not allowed in variable names, but underscores can be used to separate words in variable names. For example, `greeting_message` works but `greeting message` will cause errors.
* Avoid using Python keywords and function names *(see Keywords below)* as variable names. For example, do not use the word `print` as a variable name; Python has reserved it for a particular programmatic purpose.
* Variable names should be short but descriptive. For example, `name` is better than `n`, `student_name` is better than `s_n`, and `name_length` is better than `length_of_persons_name`.
* Be careful when using the lowercase letter `l` and the uppercase letter `O` because they could be confused with the numbers `1` and `0`.

#### Local and Global Variables
When working with variables in Python, you need to be aware of the scope of the variable. The scope of a variable is the part of your code where the variable is available. When you create a variable in Python, it is either a **local** or **global** variable.

A local variable is only available within the scope in which it is created. For example, if you create a variable inside of a function, it will only be available inside of that function.

A global variable is available throughout your entire Python program. For example, if you create a variable at the top level of your program (outside of any functions), it will be globally available throughout your program.

Simply stated, if you wish to use the same variable throughout your program declare it as a global variable; whereas, if you want to utilize that variable in only one function or procedure of your code, declare it as a local variable.

>Note: You should generally avoid using global variables in your code, as they can lead to unexpected results and make your code difficult to debug.

#### Keywords

Python keywords are reserved words that have special meanings and cannot be used as variables, functions, or classes.

In other words, Python keywords are words that are built into the Python language and have a specific meaning. They cannot be used as regular names for variables, functions, or classes.

Rules for Keywords in Python
* Python keywords cannot be used as identifiers. 
* Python identifiers are the names that we give to variables, functions, classes, and other objects in Python. They are case-sensitive, and they can only contain letters, numbers, and underscores.
* All the keywords in Python should be in lowercase except True and False. 


#### List of Python Keywords

+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keyword  | Description                                                                                                                                                  |
+==========+==============================================================================================================================================================+
| and      | This is a logical operator which returns true if both the operands are true else returns false.                                                              |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| or       | This is also a logical operator which returns true if anyone operand is true else returns false.                                                             |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| not      | This is again a logical operator it returns True if the operand is false else returns false.                                                                 |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| if       | This is used to make a conditional statement.                                                                                                                |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| elif     | elif is a condition statement used with an if statement. The elif statement is executed if the previous conditions were not true.                            |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| else     | Else is used with if and elif conditional statements. The else block is executed if the given condition is not true.                                         |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| for      | This is used to create a loop.                                                                                                                               |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| while    | This keyword is used to create a while loop.                                                                                                                 |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| break    | This is used to terminate the loop.                                                                                                                          |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| as       | This is used to create an alternative.                                                                                                                       |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| def      | It helps us to define functions.                                                                                                                             |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lambda   | It is used to define the anonymous function.                                                                                                                 |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pass     | This is a null statement which means it will do nothing.                                                                                                     |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| return   | It will return a value and exit the function.                                                                                                                |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| True     | This is a boolean value.                                                                                                                                     |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| False    | This is also a boolean value.                                                                                                                                |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| try      | It makes a try-except statement.                                                                                                                             |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| with     | The with keyword is used to simplify exception handling.                                                                                                     |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| assert   | This function is used for debugging purposes. Usually used to check the correctness of code.                                                                 |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| class    | It helps us to define a class.                                                                                                                               |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| continue | It continues to the next iteration of a loop.                                                                                                                |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| del      | It deletes a reference to an object.                                                                                                                         |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| except   | Used with exceptions, what to do when an exception occurs.                                                                                                   |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| finally  | finally is used with exceptions, a block of code that will be executed no matter if there is an exception or not.                                            |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| from     | It is used to import specific parts of any module.                                                                                                           |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| global   | This declares a global variable.                                                                                                                             |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| import   | This is used to import a module.                                                                                                                             |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| in       | It’s used to check whether a value is present in a list, range, tuple, etc.                                                                                  |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| is       | This is used to check if the two variables are equal or not.                                                                                                 |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| none     | This is a special constant used to denote a null value or avoid. It’s important to remember, 0, any empty container (e.g empty list) do not compute to None. |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| raise    | This raises an exception.                                                                                                                                    |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| yield    | It ends a function and returns a generator.                                                                                                                  |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| async    | It is used to create asynchronous coroutine.                                                                                                                 |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| await    | It releases the flow of control back to the event loop.                                                                                                      |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+


#### Rules for Naming Python Identifiers
* It cannot be a reserved Python keyword
* It should not contain white space
* It can be a combination of A-Z, a-z, 0-9, or underscore
* It should start with an alphabet character or an underscore ( _ )
* It should not contain any special character other than an underscore ( _ )

#### Examples of Python Identifiers
Valid identifiers:

```
var1
_var1
_1_var
var_1
```

Invalid Identifiers

```
!var1
1var
1_var
var#1
var 1
```
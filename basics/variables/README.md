
# Python Basics

## Variables

Variables are often described as containers where you store values. Variables can be used to store anything from simple data types (like integers and strings) to more complex data structures (like lists and dictionaries). You can think of them as labels you attach to values to keep track of them. You can also say that a variable references a certain value.

Python uses `=` to assign values to variables. There's no need to declare a variable in advance (or to assign a data type to it), assigning a value to a variable itself declares and initializes the variable with that value.

>Data types are the classification or categorization of data items and include numeric types (int, float, complex), textual types (str), collection types (list, tuple, dict, set), and boolean type (bool).

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

| Keywords |          |
|----------|----------|
| and      | as       |
| assert   | break    |
| class    | continue |
| def      | del      |
| elif     | else     |
| except   | False    |
| finally  | for      |
| from     | global   |
| if       | import   |
| in       | is       |
| lambda   | None     |
| nonlocal | not      |
| pass     | raise    |
| return   | True     |
| try      | while    |
| with     | yield    |


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

# Introduction to Python

## Credits
Portions of the material for this introduction to Python is derived from the book [Python Crash Course - Third Edition](https://nostarch.com/python-crash-course-3rd-edition).  It's available where ever you purchase your books.

### History
There are many different programming languages, Java, .NET, JavaScript and C++ are some of the more well-known languages.  In recent years, one language has certainly gained momentum: Python.

People use Python for many purposes: to make games, build web applications, solve business problems, and develop internal tools at all kinds of interesting companies. Python is also used heavily in scientific fields, for academic research and applied work.

Python is a cross-platform programming language, which means it runs on all the major operating systems. Any Python program you write should run on any modern computer that has Python installed.

Python is a "batteries-included" language because 

## Getting Started

### Installing Python

Installing Python is generally easy, and nowadays many Linux and UNIX distributions include a recent Python. Even some Windows computers now come with Python already installed. If you do need to install Python and aren't confident about the task you can find a few notes on the [BeginnersGuide/Download wiki page](https://wiki.python.org/moin/BeginnersGuide/Download), but installation is unremarkable on most platforms.

#### Coding Tools

Every Python installation comes with an **Integrated Development and Learning Environment**, which you’ll see shortened to IDLE or even IDE. These are a class of applications that help you write code more efficiently. While there are many IDEs for you to choose from, Python IDLE is very basic, which makes it the perfect tool for a beginning programmer.

Python IDLE comes included in Python installations on Windows and Mac. If you’re a Linux user, then you should be able to find and download Python IDLE using your package manager. Once you’ve installed it, you can then use Python IDLE as an interactive interpreter or as a file editor:

![](images/python-idle.png)

For our lab, we'll be using **Visual Studio Code**, a free coding editor that helps you start coding quickly. Use it to code in any programming language, without switching editors. Visual Studio Code has support for many languages, including Python, Java, C++, JavaScript, and more.

Visual Studio Code is built with extensibility in mind. From the UI to the editing experience, almost every part of VS Code can be customized and enhanced through the Extension API. In fact, many core features of VS Code are built as extensions and use the same Extension API.

![](images/vscode.png)

We'll be using a Python extension to help guide us through the coding exercises:

![](images/python-extension.png)

Of course, you can choose to use the command line interface (CLI) to write and execute Python scripts. It's straightforward and simple but can become a bit cumbersome when you begin to write more advanced applications.

```
C:\> python
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> ^Z

C:\>
```

```
C:\> python
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello Python interpreter!")
Hello Python interpreter!
```

Create a file called `hello_world.py` and enter the following line in the editor:

```
print("Hello Python world!")
```

Enter the following commands to run `hello_world.py`:

```
C:\> python hello_world.py
Hello Python world!
```

### Python Basics

#### Variables

Variables are often described as boxes where you can store values. This idea can be helpful the first few times you use a variable, but it isn’t an accurate way to describe how variables are represented internally in Python. It’s much better to think of variables as labels that you can assign to values. You can also say that a variable references a certain value.

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
* Avoid using Python keywords and function names as variable names. For example, do not use the word `print` as a variable name; Python has reserved it for a particular programmatic purpose.
* Variable names should be short but descriptive. For example, `name` is better than `n`, `student_name` is better than `s_n`, and `name_length` is better than `length_of_persons_name`.
* Be careful when using the lowercase letter `l` and the uppercase letter `O` because they could be confused with the numbers `1` and `0`.


#### Strings

Because most programs define and gather some sort of data and then do something useful with it, it helps to classify different types of data. The first data type we’ll look at is the string. Strings are quite simple at first glance, but you can use them in many different ways.

A string is a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around your strings like this:

```
"This is a string."
`This is also a string.`
```

This flexibility allows you to use quotes and apostrophes within your strings:

```
`I told my friend, "Python is my favorite language!"`
"The language `Python` is named after Monty Python, not the snake."
"One of Python`s strengths is its diverse and supportive community."
```

#### Changing Case in a String with Methods

One of the simplest tasks you can do with strings is change the case of the words in a string. Look at the following code, and try to determine what’s happening:

```
name = "ada lovelace"
print(name.title())
```

Save this file as `name.py` and then run it. You should see this output:

```
Ada Lovelace
```

In this example, the variable name refers to the lowercase string `ada lovelace`. The method `title()` appears after the variable in the `print()` call. A method is an action that Python can perform on a piece of data. The dot (.) after name in `name.title()` tells Python to make the `title()` method act on the variable name. Every method is followed by a set of parentheses, because methods often need additional information to do their work. That information is provided inside the parentheses. The `title()` function doesn’t need any additional information, so its parentheses are empty.

The `title()` method changes each word to title case, where each word begins with a capital letter. This is useful because you’ll often want to think of a name as a piece of information. For example, you might want your program to recognize the input values Ada, ADA, and ada as the same name, and display all of them as Ada.

Several other useful methods are available for dealing with case as well. For example, you can change a string to all uppercase or all lowercase letters like this:

```
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
```

This will display the following:

```
ADA LOVELACE
ada lovelace
```

The `lower()` method is particularly useful for storing data. You typically won’t want to trust the capitalization that your users provide, so you’ll convert strings to lowercase before storing them. Then when you want to display the information, you’ll use the case that makes the most sense for each string.

#### Using Variables in Strings

In some situations, you’ll want to use a variable’s value inside a string. For example, you might want to use two variables to represent a first name and a last name, respectively, and then combine those values to display someone’s full name:

```
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" ❶ 
print(full_name)
```

To insert a variable’s value into a string, place the letter `f` immediately before the opening quotation mark ❶. Put braces around the name or names of any variable you want to use inside the string. Python will replace each variable with its value when the string is displayed.

These strings are called f-strings. The `f` is for format, because Python formats the string by replacing the name of any variable in braces with its value. The output from the previous code is:

```
ada lovelace
```

You can do a lot with f-strings. For example, you can use f-strings to compose complete messages using the information associated with a variable, as shown here:

```
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!") ❶ 
```

The `full name` is used in a sentence that greets the user ❶, and the `title()` method changes the name to title case. This code returns a simple but nicely formatted greeting:

```
Hello, Ada Lovelace!
```

You can also use f-strings to compose a message, and then assign the entire message to a variable:

```
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!" ❶ 
print(message) ❷ 
```

This code displays the message Hello, Ada Lovelace! as well, but by assigning the message to a variable ❶ we make the final `print()` call much simpler ❷.

#### Adding Whitespace to Strings with Tabs or Newlines

In programming, whitespace refers to any nonprinting characters, such as spaces, tabs, and end-of-line symbols. You can use whitespace to organize your output so it’s easier for users to read.

To add a tab to your text, use the character combination \t:

```
>>> print("Python")
Python
>>> print("\tPython")
    Python
```

To add a newline in a string, use the character combination \n:

```
>>> print("Languages:\nPython\nC\nJavaScript")
Languages:
Python
C
JavaScript
```

You can also combine tabs and newlines in a single string. The string "\n\t" tells Python to move to a new line, and start the next line with a tab. The following example shows how you can use a one-line string to generate four lines of output:

```
>>> print("Languages:\n\tPython\n\tC\n\tJavaScript")
Languages:
    Python
    C
    JavaScript
```

### Numbers

Numbers are used quite often in programming to keep score in games, represent data in visualizations, store information in web applications, and so on. Python treats numbers in several different ways, depending on how they’re being used. Let’s first look at how Python manages integers, because they’re the simplest to work with.

#### Integers
You can add (+), subtract (-), multiply (*), and divide (/) integers in Python.

```
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5
```

In a terminal session, Python simply returns the result of the operation. Python uses two multiplication symbols to represent exponents:
```
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000
```

Python supports the order of operations too, so you can use multiple operations in one expression. You can also use parentheses to modify the order of operations so Python can evaluate your expression in the order you specify. For example:

```
>>> 2 + 3*4
14
>>> (2 + 3) * 4
20
```

The spacing in these examples has no effect on how Python evaluates the expressions; it simply helps you more quickly spot the operations that have priority when you’re reading through the code.

#### Floats
Python calls any number with a decimal point a float. This term is used in most programming languages, and it refers to the fact that a decimal point can appear at any position in a number. Every programming language must be carefully designed to properly manage decimal numbers so numbers behave appropriately, no matter where the decimal point appears.

For the most part, you can use floats without worrying about how they behave. Simply enter the numbers you want to use, and Python will most likely do what you expect:
```
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
```

However, be aware that you can sometimes get an arbitrary number of decimal places in your answer:

```
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
```

This happens in all languages and is of little concern. Python tries to find a way to represent the result as precisely as possible, which is sometimes difficult given how computers have to represent numbers internally. Just ignore the extra decimal places for now; you’ll learn ways to deal with the extra places when you need to in the projects in Part II.

#### Integers and Floats
When you divide any two numbers, even if they are integers that result in a whole number, you’ll always get a float:

```
>>> 4/2
2.0
```

If you mix an integer and a float in any other operation, you’ll get a float as well:
```
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0
```

Python defaults to a float in any operation that uses a float, even if the output is a whole number.

#### Underscores in Numbers
When you’re writing long numbers, you can group digits using underscores to make large numbers more readable:
```
>>> universe_age = 14_000_000_000
```

When you print a number that was defined using underscores, Python prints only the digits:
```
>>> print(universe_age)
14000000000
```

Python ignores the underscores when storing these kinds of values. Even if you don’t group the digits in threes, the value will still be unaffected. To Python, 1000 is the same as 1_000, which is the same as 10_00. This feature works for both integers and floats.

#### Multiple Assignment
You can assign values to more than one variable using just a single line of code. This can help shorten your programs and make them easier to read; you’ll use this technique most often when initializing a set of numbers.

For example, here’s how you can initialize the variables x, y, and z to zero:
```
>>> x, y, z = 0, 0, 0
```

You need to separate the variable names with commas, and do the same with the values, and Python will assign each value to its respective variable. As long as the number of values matches the number of variables, Python will match them up correctly.

#### Constants
A constant is a variable whose value stays the same throughout the life of a program. Python doesn’t have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed:
```
MAX_CONNECTIONS = 5000
```

When you want to treat a variable as a constant in your code, write the name of the variable in all capital letters.

### Comments
Comments are an extremely useful feature in most programming languages. Everything you’ve written in your programs so far is Python code. As your programs become longer and more complicated, you should add notes within your programs that describe your overall approach to the problem you’re solving. A comment allows you to write notes in your spoken language, within your programs.

How Do You Write Comments?
In Python, the hash mark (#) indicates a comment. Anything following a hash mark in your code is ignored by the Python interpreter. For example:
```
# Say hello to everyone.
print("Hello Python people!")
```

Python ignores the first line and executes the second line.
```
Hello Python people!
```

#### What Kinds of Comments Should You Write?
The main reason to write comments is to explain what your code is supposed to do and how you are making it work. When you’re in the middle of working on a project, you understand how all of the pieces fit together. But when you return to a project after some time away, you’ll likely have forgotten some of the details. You can always study your code for a while and figure out how segments were supposed to work, but writing good comments can save you time by summarizing your overall approach clearly.

If you want to become a professional programmer or collaborate with other programmers, you should write meaningful comments. Today, most software is written collaboratively, whether by a group of employees at one company or a group of people working together on an open source project. Skilled programmers expect to see comments in code, so it’s best to start adding descriptive comments to your programs now. Writing clear, concise comments in your code is one of the most beneficial habits you can form as a new programmer.

When you’re deciding whether to write a comment, ask yourself if you had to consider several approaches before coming up with a reasonable way to make something work; if so, write a comment about your solution. It’s much easier to delete extra comments later than to go back and write comments for a sparsely commented program. From now on, I’ll use comments in examples throughout this book to help explain sections of code.

### Lists
A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0 to 9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list don’t have to be related in any particular way. Because a list usually contains more than one element, it’s a good idea to make the name of your list plural, such as letters, digits, or names.

In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas. Here’s a simple example of a list that contains a few kinds of bicycles:
```
bicycles = [`trek`, `cannondale`, `redline`, `specialized`]
print(bicycles)
```

If you ask Python to print a list, Python returns its representation of the list, including the square brackets:
```
[`trek`, `cannondale`, `redline`, `specialized`]
```

Because this isn’t the output you want your users to see, let’s learn how to access the individual items in a list.

#### Accessing Elements in a List
Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired. To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.

For example, let’s pull out the first bicycle in the list bicycles:
```
bicycles = [`trek`, `cannondale`, `redline`, `specialized`]
print(bicycles[0])
```

When we ask for a single item from a list, Python returns just that element without square brackets:
```
trek
```

This is the result you want your users to see: clean, neatly formatted output.

You can also use the string methods from Chapter 2 on any element in this list. For example, you can format the element `trek` to look more presentable by using the title() method:
```
bicycles = [`trek`, `cannondale`, `redline`, `specialized`]
print(bicycles[0].title())
```

This example produces the same output as the preceding example, except `Trek` is capitalized.

#### Index Positions Start at 0, Not 1
Python considers the first item in a list to be at position 0, not position 1. This is true of most programming languages, and the reason has to do with how the list operations are implemented at a lower level. If you’re receiving unexpected results, ask yourself if you’re making a simple but common off-by-one error.

The second item in a list has an index of 1. Using this counting system, you can get any element you want from a list by subtracting one from its position in the list. For instance, to access the fourth item in a list, you request the item at index 3.

The following asks for the bicycles at index 1 and index 3:
```
bicycles = [`trek`, `cannondale`, `redline`, `specialized`]
print(bicycles[1])
print(bicycles[3])
```

This code returns the second and fourth bicycles in the list:
```
cannondale
specialized
```

Python has a special syntax for accessing the last element in a list. If you ask for the item at index -1, Python always returns the last item in the list:
```
bicycles = [`trek`, `cannondale`, `redline`, `specialized`]
print(bicycles[-1])
```

This code returns the value `specialized`. This syntax is quite useful, because you’ll often want to access the last items in a list without knowing exactly how long the list is. This convention extends to other negative index values as well. The index -2 returns the second item from the end of the list, the index -3 returns the third item from the end, and so forth.

#### Using Individual Values from a List
You can use individual values from a list just as you would any other variable. For example, you can use f-strings to create a message based on a value from a list.

Let’s try pulling the first bicycle from the list and composing a message using that value:
```
bicycles = [`trek`, `cannondale`, `redline`, `specialized`]
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)
```

We build a sentence using the value at bicycles[0] and assign it to the variable message. The output is a simple sentence about the first bicycle in the list:
```
My first bicycle was a Trek.
```

#### Modifying, Adding, and Removing Elements
Most lists you create will be dynamic, meaning you’ll build a list and then add and remove elements from it as your program runs its course. For example, you might create a game in which a player has to shoot aliens out of the sky. You could store the initial set of aliens in a list and then remove an alien from the list each time one is shot down. Each time a new alien appears on the screen, you add it to the list. Your list of aliens will increase and decrease in length throughout the course of the game.

#### Modifying Elements in a List
The syntax for modifying an element is similar to the syntax for accessing an element in a list. To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

For example, say we have a list of motorcycles and the first item in the list is `honda`. We can change the value of this first item after the list has been created:

```
motorcycles = [`honda`, `yamaha`, `suzuki`]
print(motorcycles)

motorcycles[0] = `ducati`
print(motorcycles)
```

Here we define the list motorcycles, with `honda` as the first element. Then we change the value of the first item to `ducati`. The output shows that the first item has been changed, while the rest of the list stays the same:

```
[`honda`, `yamaha`, `suzuki`]
[`ducati`, `yamaha`, `suzuki`]
```

You can change the value of any item in a list, not just the first item.

#### Adding Elements to a List
You might want to add a new element to a list for many reasons. For example, you might want to make new aliens appear in a game, add new data to a visualization, or add new registered users to a website you’ve built. Python provides several ways to add new data to existing lists.

#### Appending Elements to the End of a List
The simplest way to add a new element to a list is to append the item to the list. When you append an item to a list, the new element is added to the end of the list. Using the same list we had in the previous example, we’ll add the new element `ducati` to the end of the list:

```
motorcycles = [`honda`, `yamaha`, `suzuki`]
print(motorcycles)

motorcycles.append(`ducati`)
print(motorcycles)
```

Here the append() method adds `ducati` to the end of the list, without affecting any of the other elements in the list:

```
[`honda`, `yamaha`, `suzuki`]
[`honda`, `yamaha`, `suzuki`, `ducati`]
```

The `append()` method makes it easy to build lists dynamically. For example, you can start with an empty list and then add items to the list using a series of `append()` calls. Using an empty list, let’s add the elements `honda`, `yamaha`, and `suzuki` to the list:

```
motorcycles = []

motorcycles.append(`honda`)
motorcycles.append(`yamaha`)
motorcycles.append(`suzuki`)

print(motorcycles)
```

The resulting list looks exactly the same as the lists in the previous examples:

```
[`honda`, `yamaha`, `suzuki`]
```

Building lists this way is very common, because you often won’t know the data your users want to store in a program until after the program is running. To put your users in control, start by defining an empty list that will hold the users’ values. Then append each new value provided to the list you just created.

#### Inserting Elements into a List
You can add a new element at any position in your list by using the `insert()` method. You do this by specifying the index of the new element and the value of the new item:
```
motorcycles = [`honda`, `yamaha`, `suzuki`]

motorcycles.insert(0, `ducati`)
print(motorcycles)
```

In this example, we insert the value `ducati` at the beginning of the list. The `insert()` method opens a space at position 0 and stores the value `ducati` at that location:

```
[`ducati`, `honda`, `yamaha`, `suzuki`]
```

This operation shifts every other value in the list one position to the right.

#### Removing Elements from a List
Often, you’ll want to remove an item or a set of items from a list. For example, when a player shoots down an alien from the sky, you’ll most likely want to remove it from the list of active aliens. Or when a user decides to cancel their account on a web application you created, you’ll want to remove that user from the list of active users. You can remove an item according to its position in the list or according to its value.

#### Removing an Item Using the del Statement
If you know the position of the item you want to remove from a list, you can use the `del` statement:

```
motorcycles = [`honda`, `yamaha`, `suzuki`]
print(motorcycles)

del motorcycles[0]
print(motorcycles)
```

Here we use the `del` statement to remove the first item, `honda`, from the list of motorcycles:

```
[`honda`, `yamaha`, `suzuki`]
[`yamaha`, `suzuki`]
```

You can remove an item from any position in a list using the `del` statement if you know its index. For example, here’s how to remove the second item, `yamaha`, from the list:

```
motorcycles = [`honda`, `yamaha`, `suzuki`]
print(motorcycles)

del motorcycles[1]
print(motorcycles)
```

The second motorcycle is deleted from the list:

```
[`honda`, `yamaha`, `suzuki`]
[`honda`, `suzuki`]
```

In both examples, you can no longer access the value that was removed from the list after the `del` statement is used.

#### Removing an Item Using the pop() Method
Sometimes you’ll want to use the value of an item after you remove it from a list. For example, you might want to get the x and y position of an alien that was just shot down, so you can draw an explosion at that position. In a web application, you might want to remove a user from a list of active members and then add that user to a list of inactive members.

The `pop()` method removes the last item in a list, but it lets you work with that item after removing it. The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack. In this analogy, the top of a stack corresponds to the end of a list.

Let’s pop a motorcycle from the list of motorcycles:

```
motorcycles = [`honda`, `yamaha`, `suzuki`] ❶ 
print(motorcycles)

popped_motorcycle = motorcycles.pop() ❷ 
print(motorcycles) ❸ 
print(popped_motorcycle) ❹ 
```

We start by defining and printing the list motorcycles ❶. Then we pop a value from the list, and assign that value to the variable popped_motorcycle ❷. We print the list ❸ to show that a value has been removed from the list. Then we print the popped value ❹ to prove that we still have access to the value that was removed.

The output shows that the value `suzuki` was removed from the end of the list and is now assigned to the variable popped_motorcycle:

```
[`honda`, `yamaha`, `suzuki`]
[`honda`, `yamaha`]
suzuki
```

How might this `pop()` method be useful? Imagine that the motorcycles in the list are stored in chronological order, according to when we owned them. If this is the case, we can use the `pop()` method to print a statement about the last motorcycle we bought:

```
motorcycles = [`honda`, `yamaha`, `suzuki`]

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
```

The output is a simple sentence about the most recent motorcycle we owned:

```
The last motorcycle I owned was a Suzuki.
```

#### Popping Items from Any Position in a List
You can use `pop()` to remove an item from any position in a list by including the index of the item you want to remove in parentheses:

```
motorcycles = [`honda`, `yamaha`, `suzuki`]

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
```

We start by popping the first motorcycle in the list, and then we print a message about that motorcycle. The output is a simple sentence describing the first motorcycle I ever owned:

```
The first motorcycle I owned was a Honda.
```

Remember that each time you use `pop()`, the item you work with is no longer stored in the list.

If you’re unsure whether to use the `del` statement or the `pop()` method, here’s a simple way to decide: when you want to delete an item from a list and not use that item in any way, use the `del` statement; if you want to use an item as you remove it, use the `pop()` method.

#### Removing an Item by Value
Sometimes you won’t know the position of the value you want to remove from a list. If you only know the value of the item you want to remove, you can use the `remove()` method.

For example, say we want to remove the value `ducati` from the list of motorcycles:

```
motorcycles = [`honda`, `yamaha`, `suzuki`, `ducati`]
print(motorcycles)

motorcycles.remove(`ducati`)
print(motorcycles)
```

Here the `remove()` method tells Python to figure out where `ducati` appears in the list and remove that element:

```
[`honda`, `yamaha`, `suzuki`, `ducati`]
[`honda`, `yamaha`, `suzuki`]
```

You can also use the `remove()` method to work with a value that’s being removed from a list. Let’s remove the value `ducati` and print a reason for removing it from the list:

```
motorcycles = [`honda`, `yamaha`, `suzuki`, `ducati`] ❶ 
print(motorcycles)

too_expensive = `ducati` ❷ 
motorcycles.remove(too_expensive) ❸ 
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.") ❹ 
```

After defining the list ❶, we assign the value `ducati` to a variable called `too_expensive` ❷. We then use this variable to tell Python which value to remove from the list ❸. The value `ducati` has been removed from the list ❹ but is still accessible through the variable `too_expensive`, allowing us to print a statement about why we removed `ducati` from the list of motorcycles:

```
[`honda`, `yamaha`, `suzuki`, `ducati`]
[`honda`, `yamaha`, `suzuki`]

A Ducati is too expensive for me.
```

### Loops
You’ll often want to run through all entries in a list, performing the same task with each item. For example, in a game you might want to move every element on the screen by the same amount. In a list of numbers, you might want to perform the same statistical operation on every element. Or perhaps you’ll want to display each headline from a list of articles on a website. When you want to do the same action with every item in a list, you can use Python’s for loop.

Say we have a list of magicians’ names, and we want to print out each name in the list. We could do this by retrieving each name from the list individually, but this approach could cause several problems. For one, it would be repetitive to do this with a long list of names. Also, we’d have to change our code each time the list’s length changed. Using a for loop avoids both of these issues by letting Python manage these issues internally.

Let’s use a for loop to print out each name in a list of magicians:

```
magicians = [`alice`, `david`, `carolina`]
for magician in magicians:
    print(magician)
```
    
We begin by defining a list, just as we did in Chapter 3. Then we define a for loop. This line tells Python to pull a name from the list magicians, and associate it with the variable magician. Next, we tell Python to print the name that’s just been assigned to magician. Python then repeats these last two lines, once for each name in the list. It might help to read this code as “For every magician in the list of magicians, print the magician’s name.” The output is a simple printout of each name in the list:

```
alice
david
carolina
```

#### A Closer Look at Looping
Looping is important because it’s one of the most common ways a computer automates repetitive tasks. For example, in a simple loop like we used in `magicians.py`, Python initially reads the first line of the loop:

```
for magician in magicians:
```

This line tells Python to retrieve the first value from the list magicians and associate it with the variable magician. This first value is `alice`. Python then reads the next line:

```
print(magician)
```

Python prints the current value of magician, which is still `alice`. Because the list contains more values, Python returns to the first line of the loop:

```
for magician in magicians:
```

Python retrieves the next name in the list, `david`, and associates that value with the variable magician. Python then executes the line:

```
print(magician)
```

Python prints the current value of magician again, which is now `david`. Python repeats the entire loop once more with the last value in the list, `carolina`. Because no more values are in the list, Python moves on to the next line in the program. In this case nothing comes after the for loop, so the program ends.

When you’re using loops for the first time, keep in mind that the set of steps is repeated once for each item in the list, no matter how many items are in the list. If you have a million items in your list, Python repeats these steps a million times—and usually very quickly.

Also keep in mind when writing your own for loops that you can choose any name you want for the temporary variable that will be associated with each value in the list. However, it’s helpful to choose a meaningful name that represents a single item from the list. For example, here’s a good way to start a for loop for a list of cats, a list of dogs, and a general list of items:

```
for cat in cats:
for dog in dogs:
for item in list_of_items:
```

These naming conventions can help you follow the action being done on each item within a for loop. Using singular and plural names can help you identify whether a section of code is working with a single element from the list or the entire list.

#### Doing More Work Within a for Loop
You can do just about anything with each item in a for loop. Let’s build on the previous example by printing a message to each magician, telling them that they performed a great trick:

```
magicians = [`alice`, `david`, `carolina`]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
```

The only difference in this code is where we compose a message to each magician, starting with that magician’s name. The first time through the loop the value of magician is `alice`, so Python starts the first message with the name `alice`. The second time through, the message will begin with `david`, and the third time through, the message will begin with `carolina`.

The output shows a personalized message for each magician in the list:

```
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
```

You can also write as many lines of code as you like in the for loop. Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list. Therefore, you can do as much work as you like with each value in the list.

Let’s add a second line to our message, telling each magician that we’re looking forward to their next trick:

```
magicians = [`alice`, `david`, `carolina`]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can`t wait to see your next trick, {magician.title()}.\n")
```

Because we have indented both calls to `print()`, each line will be executed once for every magician in the list. The newline `("\n")` in the second print() call inserts a blank line after each pass through the loop. This creates a set of messages that are neatly grouped for each person in the list:

```
Alice, that was a great trick!
I can`t wait to see your next trick, Alice.

David, that was a great trick!
I can`t wait to see your next trick, David.

Carolina, that was a great trick!
I can`t wait to see your next trick, Carolina.
```

You can use as many lines as you like in your for loops. In practice, you’ll often find it useful to do a number of different operations with each item in a list when you use a for loop.

#### Doing Something After a for Loop
What happens once a for loop has finished executing? Usually, you’ll want to summarize a block of output or move on to other work that your program must accomplish.

Any lines of code after the for loop that are not indented are executed once without repetition. Let’s write a thank you to the group of magicians as a whole, thanking them for putting on an excellent show. To display this group message after all of the individual messages have been printed, we place the thank you message after the for loop, without indentation:

```
magicians = [`alice`, `david`, `carolina`]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can`t wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
```

The first two calls to `print()` are repeated once for each magician in the list, as you saw earlier. However, because the last line is not indented, it’s printed only once:

```
Alice, that was a great trick!
I can`t wait to see your next trick, Alice.

David, that was a great trick!
I can`t wait to see your next trick, David.

Carolina, that was a great trick!
I can`t wait to see your next trick, Carolina.

Thank you, everyone. That was a great magic show!
```

When you’re processing data using a for loop, you’ll find that this is a good way to summarize an operation that was performed on an entire dataset. For example, you might use a for loop to initialize a game by running through a list of characters and displaying each character on the screen. You might then write some additional code after this loop that displays a Play Now button after all the characters have been drawn to the screen.

### Avoiding Indentation Errors
Python uses indentation to determine how a line, or group of lines, is related to the rest of the program. In the previous examples, the lines that printed messages to individual magicians were part of the for loop because they were indented. Python’s use of indentation makes code very easy to read. Basically, it uses whitespace to force you to write neatly formatted code with a clear visual structure. In longer Python programs, you’ll notice blocks of code indented at a few different levels. These indentation levels help you gain a general sense of the overall program’s organization.

As you begin to write code that relies on proper indentation, you’ll need to watch for a few common indentation errors. For example, people sometimes indent lines of code that don’t need to be indented or forget to indent lines that need to be indented. Seeing examples of these errors now will help you avoid them in the future and correct them when they do appear in your own programs.

Let’s examine some of the more common indentation errors.

#### Forgetting to Indent
Always indent the line after the `for` statement in a loop. If you forget, Python will remind you:

```
magicians = [`alice`, `david`, `carolina`]
for magician in magicians:
print(magician) ❶ 
```

The call to `print()` ❶ should be indented, but it’s not. When Python expects an indented block and doesn’t find one, it lets you know which line it had a problem with:

```
  File "magicians.py", line 3
    print(magician)
    ^
IndentationError: expected an indented block after `for` statement on line 2
```

You can usually resolve this kind of indentation error by indenting the line or lines immediately after the for statement.

#### Forgetting to Indent Additional Lines
Sometimes your loop will run without any errors but won’t produce the expected result. This can happen when you’re trying to do several tasks in a loop and you forget to indent some of its lines.

For example, this is what happens when we forget to indent the second line in the loop that tells each magician we’re looking forward to their next trick:

```
magicians = [`alice`, `david`, `carolina`]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can`t wait to see your next trick, {magician.title()}.\n") ❶ 
```

The second call to `print()` ❶ is supposed to be indented, but because Python finds at least one indented line after the for statement, it doesn’t report an error. As a result, the first `print()` call is executed once for each name in the list because it is indented. The second `print()` call is not indented, so it is executed only once after the loop has finished running. Because the final value associated with magician is `carolina`, she is the only one who receives the “looking forward to the next trick” message:

```
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
I can`t wait to see your next trick, Carolina.
```

This is a logical error. The syntax is valid Python code, but the code does not produce the desired result because a problem occurs in its logic. If you expect to see a certain action repeated once for each item in a list and it’s executed only once, determine whether you need to simply indent a line or a group of lines.

#### Indenting Unnecessarily
If you accidentally indent a line that doesn’t need to be indented, Python informs you about the unexpected indent:

```
message = "Hello Python world!"
    print(message)
```

We don’t need to indent the `print()` call, because it isn’t part of a loop; hence, Python reports that error:

```
  File "hello_world.py", line 2
    print(message)
    ^
IndentationError: unexpected indent
```

You can avoid unexpected indentation errors by indenting only when you have a specific reason to do so. In the programs you’re writing at this point, the only lines you should indent are the actions you want to repeat for each item in a for loop.

#### Indenting Unnecessarily After the Loop
If you accidentally indent code that should run after a loop has finished, that code will be repeated once for each item in the list. Sometimes this prompts Python to report an error, but often this will result in a logical error.

For example, let’s see what happens when we accidentally indent the line that thanked the magicians as a group for putting on a good show:

```
magicians = [`alice`, `david`, `carolina`]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can`t wait to see your next trick, {magician.title()}.\n")

     print("Thank you everyone, that was a great magic show!") ❶
```

Because the last line ❶ is indented, it’s printed once for each person in the list:

```
Alice, that was a great trick!
I can`t wait to see your next trick, Alice.

Thank you everyone, that was a great magic show!
David, that was a great trick!
I can`t wait to see your next trick, David.

Thank you everyone, that was a great magic show!
Carolina, that was a great trick!
I can`t wait to see your next trick, Carolina.

Thank you everyone, that was a great magic show!
```

This is another logical error, similar to the one in “Forgetting to Indent Additional Lines”. Because Python doesn’t know what you’re trying to accomplish with your code, it will run all code that is written in valid syntax. If an action is repeated many times when it should be executed only once, you probably need to unindent the code for that action.

#### Forgetting the Colon
The colon at the end of a for statement tells Python to interpret the next line as the start of a loop.

```
magicians = [`alice`, `david`, `carolina`]
for magician in magicians ❶ 
    print(magician)
```

If you accidentally forget the colon ❶, you’ll get a syntax error because Python doesn’t know exactly what you’re trying to do:

```
  File "magicians.py", line 2
    for magician in magicians
                             ^
SyntaxError: expected `:`
```

Python doesn’t know if you simply forgot the colon, or if you meant to write additional code to set up a more complex loop. If the interpreter can identify a possible fix it will suggest one, like adding a colon at the end of a line, as it does here with the response expected `:`. Some errors have easy, obvious fixes, thanks to the suggestions in Python’s tracebacks. Some errors are much harder to resolve, even when the eventual fix only involves a single character. Don’t feel bad when a small fix takes a long time to find; you are absolutely not alone in this experience.

### IF Statements

Programming often involves examining a set of conditions and deciding which action to take based on those conditions. Python’s if statement allows you to examine the current state of a program and respond appropriately to that state.

In this chapter, you’ll learn to write conditional tests, which allow you to check any condition of interest. You’ll learn to write simple if statements, and you’ll learn how to create a more complex series of if statements to identify when the exact conditions you want are present. You’ll then apply this concept to lists, so you’ll be able to write a for loop that handles most items in a list one way but handles certain items with specific values in a different way.

#### A Simple Example
The following example shows how if tests let you respond to special situations correctly. Imagine you have a list of cars and you want to print out the name of each car. Car names are proper names, so the names of most cars should be printed in title case. However, the value `bmw` should be printed in all uppercase. The following code loops through a list of car names and looks for the value `bmw`. Whenever the value is `bmw`, it’s printed in uppercase instead of title case:

```
cars = [`audi`, `bmw`, `subaru`, `toyota`]

for car in cars: ❶
     if car == `bmw`:
        print(car.upper())
    else:
        print(car.title())
```

The loop in this example first checks if the current value of car is `bmw` ❶. If it is, the value is printed in uppercase. If the value of car is anything other than `bmw`, it’s printed in title case:

```
Audi
BMW
Subaru
Toyota
```

This example combines a number of the concepts you’ll learn about in this chapter. Let’s begin by looking at the kinds of tests you can use to examine the conditions in your program.

#### Conditional Tests
At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test. Python uses the values True and False to decide whether the code in an if statement should be executed. If a conditional test evaluates to True, Python executes the code following the if statement. If the test evaluates to False, Python ignores the code following the if statement.

#### Checking for Equality
Most conditional tests compare the current value of a variable to a specific value of interest. The simplest conditional test checks whether the value of a variable is equal to the value of interest:

```
>>> car = `bmw`
>>> car == `bmw`
True
```

The first line sets the value of car to `bmw` using a single equal sign, as you’ve seen many times already. The next line checks whether the value of car is `bmw` by using a double equal sign (==). This equality operator returns True if the values on the left and right side of the operator match, and False if they don’t match. The values in this example match, so Python returns True.

When the value of car is anything other than `bmw`, this test returns False:

```
>>> car = `audi`
>>> car == `bmw`
False
```

A single equal sign is really a statement; you might read the first line of code here as “Set the value of car equal to `audi`.” On the other hand, a double equal sign asks a question: “Is the value of car equal to `bmw`?” Most programming languages use equal signs in this way.

#### Ignoring Case When Checking for Equality
Testing for equality is case sensitive in Python. For example, two values with different capitalization are not considered equal:

```
>>> car = `Audi`
>>> car == `audi`
False
```

If case matters, this behavior is advantageous. But if case doesn’t matter and instead you just want to test the value of a variable, you can convert the variable’s value to lowercase before doing the comparison:

```
>>> car = `Audi`
>>> car.lower() == `audi`
True
```

This test will return True no matter how the value `Audi` is formatted because the test is now case insensitive. The lower() method doesn’t change the value that was originally stored in car, so you can do this kind of comparison without affecting the original variable:

```
>>> car = `Audi`
>>> car.lower() == `audi`
True
>>> car
`Audi`
```

We first assign the capitalized string `Audi` to the variable car. Then, we convert the value of car to lowercase and compare the lowercase value to the string `audi`. The two strings match, so Python returns True. We can see that the value stored in car has not been affected by the lower() method.

Websites enforce certain rules for the data that users enter in a manner similar to this. For example, a site might use a conditional test like this to ensure that every user has a truly unique username, not just a variation on the capitalization of another person’s username. When someone submits a new username, that new username is converted to lowercase and compared to the lowercase versions of all existing usernames. During this check, a username like `John` will be rejected if any variation of `john` is already in use.

#### Checking for Inequality
When you want to determine whether two values are not equal, you can use the inequality operator (!=). Let’s use another if statement to examine how to use the inequality operator. We’ll store a requested pizza topping in a variable and then print a message if the person did not order anchovies:

```
requested_topping = `mushrooms`

if requested_topping != `anchovies`:
    print("Hold the anchovies!")
```

This code compares the value of requested_topping to the value `anchovies`. If these two values do not match, Python returns True and executes the code following the if statement. If the two values match, Python returns False and does not run the code following the if statement.

Because the value of requested_topping is not `anchovies`, the print() function is executed:

Hold the anchovies!
Most of the conditional expressions you write will test for equality, but sometimes you’ll find it more efficient to test for inequality.

#### Numerical Comparisons
Testing numerical values is pretty straightforward. For example, the following code checks whether a person is 18 years old:

```
>>> age = 18
>>> age == 18
True
```

You can also test to see if two numbers are not equal. For example, the following code prints a message if the given answer is not correct:

```
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
```

The conditional test passes, because the value of answer (17) is not equal to 42. Because the test passes, the indented code block is executed:

That is not the correct answer. Please try again!
You can include various mathematical comparisons in your conditional statements as well, such as less than, less than or equal to, greater than, and greater than or equal to:

```
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
```

Each mathematical comparison can be used as part of an if statement, which can help you detect the exact conditions of interest.

#### Checking Multiple Conditions
You may want to check multiple conditions at the same time. For example, sometimes you might need two conditions to be True to take an action. Other times, you might be satisfied with just one condition being True. The keywords and and or can help you in these situations.

#### Using and to Check Multiple Conditions
To check whether two conditions are both True simultaneously, use the keyword and to combine the two conditional tests; if each test passes, the overall expression evaluates to True. If either test fails or if both tests fail, the expression evaluates to False.

For example, you can check whether two people are both over 21 by using the following test:

```
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21 ❶ 
False
>>> age_1 = 22 ❷ 
>>> age_0 >= 21 and age_1 >= 21
True
```

First, we define two ages, `age_0` *and* `age_1`. Then we check whether both ages are 21 or older ❶. The test on the left passes, but the test on the right fails, so the overall conditional expression evaluates to False. We then change age_1 to 22 ❷. The value of age_1 is now greater than 21, so both individual tests pass, causing the overall conditional expression to evaluate as True.

To improve readability, you can use parentheses around the individual tests, but they are not required. If you use parentheses, your test would look like this:

```
(age_0 >= 21) and (age_1 >= 21)
```

#### Using or to Check Multiple Conditions
The keyword or allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass. An or expression fails only when both individual tests fail.

Let’s consider two ages again, but this time we’ll look for only one person to be over 21:

```
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21 ❶ 
True
>>> age_0 = 18 ❷ 
>>> age_0 >= 21 or age_1 >= 21
False
```

We start with two age variables again. Because the test for `age_0` ❶ passes, the overall expression evaluates to True. We then lower `age_0` to 18. In the final test ❷, both tests now fail and the overall expression evaluates to False.

#### Checking Whether a Value Is in a List
Sometimes it’s important to check whether a list contains a certain value before taking an action. For example, you might want to check whether a new username already exists in a list of current usernames before completing someone’s registration on a website. In a mapping project, you might want to check whether a submitted location already exists in a list of known locations.

To find out whether a particular value is already in a list, use the keyword in. Let’s consider some code you might write for a pizzeria. We’ll make a list of toppings a customer has requested for a pizza and then check whether certain toppings are in the list.

```
>>> requested_toppings = [`mushrooms`, `onions`, `pineapple`]
>>> `mushrooms` in requested_toppings
True
>>> `pepperoni` in requested_toppings
False
```

The keyword in tells Python to check for the existence of `mushrooms` and `pepperoni` in the list requested_toppings. This technique is quite powerful because you can create a list of essential values, and then easily check whether the value you’re testing matches one of the values in the list.

#### Checking Whether a Value Is Not in a List
Other times, it’s important to know if a value does not appear in a list. You can use the keyword not in this situation. For example, consider a list of users who are banned from commenting in a forum. You can check whether a user has been banned before allowing that person to submit a comment:
```
banned_users = [`andrew`, `carolina`, `david`]
user = `marie`

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
```

The if statement here reads quite clearly. If the value of user is not in the list banned_users, Python returns True and executes the indented line.

The user `marie` is not in the list banned_users, so she sees a message inviting her to post a response:

```
Marie, you can post a response if you wish.
```

#### Boolean Expressions
As you learn more about programming, you’ll hear the term Boolean expression at some point. A Boolean expression is just another name for a conditional test. A Boolean value is either True or False, just like the value of a conditional expression after it has been evaluated.

Boolean values are often used to keep track of certain conditions, such as whether a game is running or whether a user can edit certain content on a website:

```
game_active = True
can_edit = False
```

Boolean values provide an efficient way to track the state of a program or a particular condition that is important in your program.

### if Statements
When you understand conditional tests, you can start writing if statements. Several different kinds of if statements exist, and your choice of which to use depends on the number of conditions you need to test. You saw several examples of if statements in the discussion about conditional tests, but now let’s dig deeper into the topic.

#### Simple if Statements
The simplest kind of if statement has one test and one action:

```
if conditional_test:
    do something
```

You can put any conditional test in the first line and just about any action in the indented block following the test. If the conditional test evaluates to True, Python executes the code following the if statement. If the test evaluates to False, Python ignores the code following the if statement.

Let’s say we have a variable representing a person’s age, and we want to know if that person is old enough to vote. The following code tests whether the person can vote:

```
age = 19
if age >= 18:
    print("You are old enough to vote!")
```

Python checks to see whether the value of age is greater than or equal to 18. It is, so Python executes the indented `print()` call:

You are old enough to vote!
Indentation plays the same role in if statements as it did in for loops. All indented lines after an if statement will be executed if the test passes, and the entire block of indented lines will be ignored if the test does not pass.

You can have as many lines of code as you want in the block following the if statement. Let’s add another line of output if the person is old enough to vote, asking if the individual has registered to vote yet:

```
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

The conditional test passes, and both `print()` calls are indented, so both lines are printed:

```
You are old enough to vote!
Have you registered to vote yet?
```

If the value of age is less than 18, this program would produce no output.

#### if-else Statements
Often, you’ll want to take one action when a conditional test passes and a different action in all other cases. Python’s if-else syntax makes this possible. An if-else block is similar to a simple if statement, but the else statement allows you to define an action or set of actions that are executed when the conditional test fails.

We’ll display the same message we had previously if the person is old enough to vote, but this time we’ll add a message for anyone who is not old enough to vote:

```
age = 17
if age >= 18: ❶ 
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else: ❷ 
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

If the conditional test ❶ passes, the first block of indented print() calls is executed. If the test evaluates to False, the else block ❷ is executed. Because age is less than 18 this time, the conditional test fails and the code in the else block is executed:

```
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
```

This code works because it has only two possible situations to evaluate: a person is either old enough to vote or not old enough to vote. The if-else structure works well in situations in which you want Python to always execute one of two possible actions. In a simple if-else chain like this, one of the two actions will always be executed.

#### The if-elif-else Chain
Often, you’ll need to test more than two possible situations, and to evaluate these you can use Python’s `if-elif-else` syntax. Python executes only one block in an `if-elif-else` chain. It runs each conditional test in order, until one passes. When a test passes, the code following that test is executed and Python skips the rest of the tests.

Many real-world situations involve more than two possible conditions. For example, consider an amusement park that charges different rates for different age groups:

```
Admission for anyone under age 4 is free.
Admission for anyone between the ages of 4 and 18 is $25.
Admission for anyone age 18 or older is $40.
```

How can we use an if statement to determine a person’s admission rate? The following code tests for the age group of a person and then prints an admission price message:

```
age = 12
if age < 4: ❶ 
    print("Your admission cost is $0.")
elif age < 18: ❷ 
    print("Your admission cost is $25.")
else: ❸ 
    print("Your admission cost is $40.")
```

The `if` test ❶ checks whether a person is under 4 years old. When the test passes, an appropriate message is printed and Python skips the rest of the tests. The `elif` line ❷ is really another if test, which runs only if the previous test failed. At this point in the chain, we know the person is at least 4 years old because the first test failed. If the person is under 18, an appropriate message is printed and Python skips the else block. If both the `if` and `elif` tests fail, Python runs the code in the `else` block ❸.

In this example the if test ❶ evaluates to False, so its code block is not executed. However, the `elif` test evaluates to True (12 is less than 18) so its code is executed. The output is one sentence, informing the user of the admission cost:

```
Your admission cost is $25.
```

Any age greater than 17 would cause the first two tests to fail. In these situations, the else block would be executed and the admission price would be $40.

Rather than printing the admission price within the `if-elif-else` block, it would be more concise to set just the price inside the `if-elif-else` chain and then have a single `print()` call that runs after the chain has been evaluated:
```
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
```

The indented lines set the value of price according to the person’s age, as in the previous example. After the price is set by the `if-elif-else` chain, a separate unindented `print()` call uses this value to display a message reporting the person’s admission price.

This code produces the same output as the previous example, but the purpose of the `if-elif-else` chain is narrower. Instead of determining a price and displaying a message, it simply determines the admission price. In addition to being more efficient, this revised code is easier to modify than the original approach. To change the text of the output message, you would need to change only one `print()` call rather than three separate `print()` calls.

#### Using Multiple elif Blocks
You can use as many `elif` blocks in your code as you like. For example, if the amusement park were to implement a discount for seniors, you could add one more conditional test to the code to determine whether someone qualifies for the senior discount. Let’s say that anyone 65 or older pays half the regular admission, or $20:

```
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")
```

Most of this code is unchanged. The second `elif` block now checks to make sure a person is less than age 65 before assigning them the full admission rate of $40. Notice that the value assigned in the else block needs to be changed to $20, because the only ages that make it to this block are for people 65 or older.

#### Omitting the else Block
Python does not require an else block at the end of an if-elif chain. Sometimes, an else block is useful. Other times, it’s clearer to use an additional elif statement that catches the specific condition of interest:

```
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
```

The final `elif` block assigns a price of $20 when the person is 65 or older, which is a little clearer than the general else block. With this change, every block of code must pass a specific test in order to be executed.

The else block is a catchall statement. It matches any condition that wasn’t matched by a specific `if` or `elif` test, and that can sometimes include invalid or even malicious data. If you have a specific final condition you’re testing for, consider using a final elif block and omit the else block. As a result, you’ll be more confident that your code will run only under the correct conditions.

#### Testing Multiple Conditions
The `if-elif-else` chain is powerful, but it’s only appropriate to use when you just need one test to pass. As soon as Python finds one test that passes, it skips the rest of the tests. This behavior is beneficial, because it’s efficient and allows you to test for one specific condition.

However, sometimes it’s important to check all conditions of interest. In this case, you should use a series of simple if statements with no `elif` or else blocks. This technique makes sense when more than one condition could be True, and you want to act on every condition that is True.

Let’s reconsider the pizzeria example. If someone requests a two-topping pizza, you’ll need to be sure to include both toppings on their pizza:

```
requested_toppings = [`mushrooms`, `extra cheese`]

if `mushrooms` in requested_toppings:
    print("Adding mushrooms.")
if `pepperoni` in requested_toppings: ❶ 
    print("Adding pepperoni.")
if `extra cheese` in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

We start with a list containing the requested toppings. The first if statement checks to see whether the person requested mushrooms on their pizza. If so, a message is printed confirming that topping. The test for pepperoni ❶ is another simple `if` statement, not an `elif` or else statement, so this test is run regardless of whether the previous test passed or not. The last if statement checks whether extra cheese was requested, regardless of the results from the first two tests. These three independent tests are executed every time this program is run.

Because every condition in this example is evaluated, both mushrooms and extra cheese are added to the pizza:

```
Adding mushrooms.
Adding extra cheese.

Finished making your pizza!
```

This code would not work properly if we used an `if-elif-else` block, because the code would stop running after only one test passes. Here’s what that would look like:

```
requested_toppings = [`mushrooms`, `extra cheese`]

if `mushrooms` in requested_toppings:
    print("Adding mushrooms.")
elif `pepperoni` in requested_toppings:
    print("Adding pepperoni.")
elif `extra cheese` in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

The test for `mushrooms` is the first test to pass, so mushrooms are added to the pizza. However, the values `extra cheese` and `pepperoni` are never checked, because Python doesn’t run any tests beyond the first test that passes in an `if-elif-else` chain. The customer’s first topping will be added, but all of their other toppings will be missed:

```
Adding mushrooms.

Finished making your pizza!
```

In summary, if you want only one block of code to run, use an `if-elif-else` chain. If more than one block of code needs to run, use a series of independent `if` statements.

#### Using if Statements with Lists
You can do some interesting work when you combine lists and if statements. You can watch for special values that need to be treated differently than other values in the list. You can efficiently manage changing conditions, such as the availability of certain items in a restaurant throughout a shift. You can also begin to prove that your code works as you expect it to in all possible situations.

#### Checking for Special Items
This chapter began with a simple example that showed how to handle a special value like `bmw`, which needed to be printed in a different format than other values in the list. Now that you have a basic understanding of conditional tests and if statements, let’s take a closer look at how you can watch for special values in a list and handle those values appropriately.

Let’s continue with the pizzeria example. The pizzeria displays a message whenever a topping is added to your pizza, as it’s being made. The code for this action can be written very efficiently by making a list of toppings the customer has requested and using a loop to announce each topping as it’s added to the pizza:

```
requested_toppings = [`mushrooms`, `green peppers`, `extra cheese`]

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
```

The output is straightforward because this code is just a simple for loop:

```
Adding mushrooms.
Adding green peppers.
Adding extra cheese.

Finished making your pizza!
```

But what if the pizzeria runs out of green peppers? An if statement inside the for loop can handle this situation appropriately:

```
requested_toppings = [`mushrooms`, `green peppers`, `extra cheese`]

for requested_topping in requested_toppings:
    if requested_topping == `green peppers`:
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
```

This time, we check each requested item before adding it to the pizza. The if statement checks to see if the person requested green peppers. If so, we display a message informing them why they can’t have green peppers. The else block ensures that all other toppings will be added to the pizza.

The output shows that each requested topping is handled appropriately.

```
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.

Finished making your pizza!
```

#### Checking That a List Is Not Empty
We’ve made a simple assumption about every list we’ve worked with so far: we’ve assumed that each list has at least one item in it. Soon we’ll let users provide the information that’s stored in a list, so we won’t be able to assume that a list has any items in it each time a loop is run. In this situation, it’s useful to check whether a list is empty before running a for loop.

As an example, let’s check whether the list of requested toppings is empty before building the pizza. If the list is empty, we’ll prompt the user and make sure they want a plain pizza. If the list is not empty, we’ll build the pizza just as we did in the previous examples:

```
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

This time we start out with an empty list of requested toppings. Instead of jumping right into a for loop, we do a quick check first. When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False. If requested_toppings passes the conditional test, we run the same for loop we used in the previous example. If the conditional test fails, we print a message asking the customer if they really want a plain pizza with no toppings.

The list is empty in this case, so the output asks if the user really wants a plain pizza:

```
Are you sure you want a plain pizza?
```

If the list is not empty, the output will show each requested topping being added to the pizza.

#### Using Multiple Lists
People will ask for just about anything, especially when it comes to pizza toppings. What if a customer actually wants french fries on their pizza? You can use lists and if statements to make sure your input makes sense before you act on it.

Let’s watch out for unusual topping requests before we build a pizza. The following example defines two lists. The first is a list of available toppings at the pizzeria, and the second is the list of toppings that the user has requested. This time, each item in requested_toppings is checked against the list of available toppings before it’s added to the pizza:

```
available_toppings = [`mushrooms`, `olives`, `green peppers`,
                      `pepperoni`, `pineapple`, `extra cheese`]

requested_toppings = [`mushrooms`, `french fries`, `extra cheese`] ❶ 

for requested_topping in requested_toppings:
     if requested_topping in available_toppings: ❷
        print(f"Adding {requested_topping}.")
     else: ❸
        print(f"Sorry, we don`t have {requested_topping}.")

print("\nFinished making your pizza!")
```

First, we define a list of available toppings at this pizzeria. Note that this could be a tuple if the pizzeria has a stable selection of toppings. Then, we make a list of toppings that a customer has requested. There’s an unusual request for a topping in this example: `french fries` ❶. Next we loop through the list of requested toppings. Inside the loop, we check to see if each requested topping is actually in the list of available toppings ❷. If it is, we add that topping to the pizza. If the requested topping is not in the list of available toppings, the else block will run ❸. The else block prints a message telling the user which toppings are unavailable.

This code syntax produces clean, informative output:

```
Adding mushrooms.
Sorry, we don`t have french fries.
Adding extra cheese.

Finished making your pizza!
```

In just a few lines of code, we’ve managed a real-world situation pretty effectively!


#### Styling Your if Statements
In every example in this chapter, you’ve seen good styling habits. The only recommendation PEP 8 provides for styling conditional tests is to use a single space around comparison operators, such as ==, >=, and <=. For example:

```
if age < 4:
```

is better than:

```
if age<4:
```

Such spacing does not affect the way Python interprets your code; it just makes your code easier for you and others to read.

### User Input & WHILE Loops

Most programs are written to solve an end user’s problem. To do so, you usually need to get some information from the user. For example, say someone wants to find out whether they’re old enough to vote. If you write a program to answer this question, you need to know the user’s age before you can provide an answer. The program will need to ask the user to enter, or input, their age; once the program has this input, it can compare it to the voting age to determine if the user is old enough and then report the result.

In this chapter you’ll learn how to accept user input so your program can then work with it. When your program needs a name, you’ll be able to prompt the user for a name. When your program needs a list of names, you’ll be able to prompt the user for a series of names. To do this, you’ll use the input() function.

You’ll also learn how to keep programs running as long as users want them to, so they can enter as much information as they need to; then, your program can work with that information. You’ll use Python’s while loop to keep programs running as long as certain conditions remain true.

With the ability to work with user input and the ability to control how long your programs run, you’ll be able to write fully interactive programs.

#### How the input() Function Works
The `input()` function pauses your program and waits for the user to enter some text. Once Python receives the user’s input, it assigns that input to a variable to make it convenient for you to work with.

For example, the following program asks the user to enter some text, then displays that message back to the user:

```
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

The `input()` function takes one argument: the prompt that we want to display to the user, so they know what kind of information to enter. In this example, when Python runs the first line, the user sees the prompt Tell me something, and I will repeat it back to you: . The program waits while the user enters their response and continues after the user presses ENTER. The response is assigned to the variable message, then print(message) displays the input back to the user:

```
Tell me something, and I will repeat it back to you: Hello everyone!
Hello everyone!
```

#### Writing Clear Prompts
Each time you use the `input()` function, you should include a clear, easy-to-follow prompt that tells the user exactly what kind of information you’re looking for. Any statement that tells the user what to enter should work. For example:

```
name = input("Please enter your name: ")
print(f"\nHello, {name}!")
```

Add a space at the end of your prompts (after the colon in the preceding example) to separate the prompt from the user’s response and to make it clear to your user where to enter their text. For example:

```
Please enter your name: Eric
Hello, Eric!
```

Sometimes you’ll want to write a prompt that’s longer than one line. For example, you might want to tell the user why you’re asking for certain input. You can assign your prompt to a variable and pass that variable to the `input()` function. This allows you to build your prompt over several lines, then write a clean `input()` statement.

```
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
```

This example shows one way to build a multiline string. The first line assigns the first part of the message to the variable prompt. In the second line, the operator += takes the string that was assigned to prompt and adds the new string onto the end.

The prompt now spans two lines, again with space after the question mark for clarity:

```
If you share your name, we can personalize the messages you see.
What is your first name? Eric

Hello, Eric!
```

#### Using int() to Accept Numerical Input
When you use the `input()` function, Python interprets everything the user enters as a string. Consider the following interpreter session, which asks for the user’s age:

```
>>> age = input("How old are you? ")
How old are you? 21
>>> age
'21'
```

The user enters the number 21, but when we ask Python for the value of age, it returns '21', the string representation of the numerical value entered. We know Python interpreted the input as a string because the number is now enclosed in quotes. If all you want to do is print the input, this works well. But if you try to use the input as a number, you’ll get an error:

```
>>> age = input("How old are you? ")
How old are you? 21
>>> age >= 18 ❶
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>=' not supported between instances of 'str' and 'int' ❷
```

When you try to use the input to do a numerical comparison ❶, Python produces an error because it can’t compare a string to an integer: the string '21' that’s assigned to age can’t be compared to the numerical value 18 ❷.

We can resolve this issue by using the int() function, which converts the input string to a numerical value. This allows the comparison to run successfully:

```
>>> age = input("How old are you? ")
How old are you? 21
>>> age = int(age) ❶ 
>>> age >= 18
True
```

In this example, when we enter 21 at the prompt, Python interprets the number as a string, but the value is then converted to a numerical representation by int() ❶. Now Python can run the conditional test: it compares age (which now represents the numerical value 21) and 18 to see if age is greater than or equal to 18. This test evaluates to True.

How do you use the int() function in an actual program? Consider a program that determines whether people are tall enough to ride a roller coaster:

```
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

The program can compare height to 48 because `height = int(height)` converts the input value to a numerical representation before the comparison is made. If the number entered is greater than or equal to 48, we tell the user that they’re tall enough:

```
How tall are you, in inches? 71

You're tall enough to ride!
```

When you use numerical input to do calculations and comparisons, be sure to convert the input value to a numerical representation first.

#### The Modulo Operator
A useful tool for working with numerical information is the modulo operator (%), which divides one number by another number and returns the remainder:

```
>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
```

The modulo operator doesn’t tell you how many times one number fits into another; it only tells you what the remainder is.

When one number is divisible by another number, the remainder is 0, so the modulo operator always returns 0. You can use this fact to determine if a number is even or odd:

```
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
```

Even numbers are always divisible by two, so if the modulo of a number and two is zero (here, if number % 2 == 0) the number is even. Otherwise, it’s odd.

```
Enter a number, and I'll tell you if it's even or odd: 42

The number 42 is even.
```

### Introducing while Loops
The for loop takes a collection of items and executes a block of code once for each item in the collection. In contrast, the while loop runs as long as, or while, a certain condition is true.

#### The while Loop in Action
You can use a while loop to count up through a series of numbers. For example, the following while loop counts from 1 to 5:

```
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

In the first line, we start counting from 1 by assigning `current_number` the value 1. The while loop is then set to keep running as long as the value of `current_number` is less than or equal to 5. The code inside the loop prints the value of `current_number` and then adds 1 to that value with `current_number += 1`. (The `+=` operator is shorthand for `current_number = current_number + 1`.)

Python repeats the loop as long as the condition `current_number <= 5` is true. Because 1 is less than 5, Python prints 1 and then adds 1, making the current number 2. Because 2 is less than 5, Python prints 2 and adds 1 again, making the current number 3, and so on. Once the value of current_number is greater than 5, the loop stops running and the program ends:

```
1
2
3
4
5
```

The programs you use every day most likely contain while loops. For example, a game needs a while loop to keep running as long as you want to keep playing, and so it can stop running as soon as you ask it to quit. Programs wouldn’t be fun to use if they stopped running before we told them to or kept running even after we wanted to quit, so while loops are quite useful.

#### Letting the User Choose When to Quit
We can make the parrot.py program run as long as the user wants by putting most of the program inside a while loop. We’ll define a quit value and then keep the program running as long as the user has not entered the quit value:

```
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
```

We first define a prompt that tells the user their two options: entering a message or entering the quit value (in this case, 'quit'). Then we set up a variable message to keep track of whatever value the user enters. We define message as an empty string, "", so Python has something to check the first time it reaches the while line. The first time the program runs and Python reaches the while statement, it needs to compare the value of message to 'quit', but no user input has been entered yet. If Python has nothing to compare, it won’t be able to continue running the program. To solve this problem, we make sure to give message an initial value. Although it’s just an empty string, it will make sense to Python and allow it to perform the comparison that makes the while loop work. This while loop runs as long as the value of message is not 'quit'.

The first time through the loop, message is just an empty string, so Python enters the loop. At message = input(prompt), Python displays the prompt and waits for the user to enter their input. Whatever they enter is assigned to message and printed; then, Python reevaluates the condition in the while statement. As long as the user has not entered the word 'quit', the prompt is displayed again and Python waits for more input. When the user finally enters 'quit', Python stops executing the while loop and the program ends:

```
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
quit
```

This program works well, except that it prints the word 'quit' as if it were an actual message. A simple if test fixes this:

```
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
```

Now the program makes a quick check before displaying the message and only prints the message if it does not match the quit value:

```
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
```

#### Using a Flag
In the previous example, we had the program perform certain tasks while a given condition was true. But what about more complicated programs in which many different events could cause the program to stop running?

For example, in a game, several different events can end the game. When the player runs out of ships, their time runs out, or the cities they were supposed to protect are all destroyed, the game should end. It needs to end if any one of these events happens. If many possible events might occur to stop the program, trying to test all these conditions in one while statement becomes complicated and difficult.

For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False. As a result, our overall while statement needs to check only one condition: whether the flag is currently True. Then, all our other tests (to see if an event has occurred that should set the flag to False) can be neatly organized in the rest of the program.

Let’s add a flag to `parrot.py` from the previous section. This flag, which we’ll call active (though you can call it anything), will monitor whether or not the program should continue running:

```
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
❶ while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
```

We set the variable active to True so the program starts in an active state. Doing so makes the while statement simpler because no comparison is made in the while statement itself; the logic is taken care of in other parts of the program. As long as the active variable remains True, the loop will continue running ❶.

In the if statement inside the while loop, we check the value of message once the user enters their input. If the user enters 'quit', we set active to False, and the while loop stops. If the user enters anything other than 'quit', we print their input as a message.

This program has the same output as the previous example where we placed the conditional test directly in the while statement. But now that we have a flag to indicate whether the overall program is in an active state, it would be easy to add more tests (such as elif statements) for events that should cause active to become False. This is useful in complicated programs like games, in which there may be many events that should each make the program stop running. When any of these events causes the active flag to become False, the main game loop will exit, a Game Over message can be displayed, and the player can be given the option to play again.

#### Using break to Exit a Loop
To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement. The break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren’t, so the program only executes code that you want it to, when you want it to.

For example, consider a program that asks the user about places they’ve visited. We can stop the while loop in this program by calling break as soon as the user enters the 'quit' value:

```
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

❶ while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```

A loop that starts with while True ❶ will run forever unless it reaches a break statement. The loop in this program continues asking the user to enter the names of cities they’ve been to until they enter 'quit'. When they enter 'quit', the break statement runs, causing Python to exit the loop:

```
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) New York
I'd love to go to New York!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) San Francisco
I'd love to go to San Francisco!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) quit
```

>NOTE:
>
>You can use the break statement in any of Python’s loops. For example, you could use break to quit a for loop that’s working through a list or a dictionary.

#### Using continue in a Loop
Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop, based on the result of a conditional test. For example, consider a loop that counts from 1 to 10 but prints only the odd numbers in that range:

```
current_number = 0
while current_number < 10:
❶     current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
```

First, we set `current_number` to 0. Because it’s less than 10, Python enters the while loop. Once inside the loop, we increment the count by 1 ❶, so `current_number` is 1. The if statement then checks the modulo of `current_number` and `2`. If the modulo is 0 (which means current_number is divisible by 2), the continue statement tells Python to ignore the rest of the loop and return to the beginning. If the current number is not divisible by 2, the rest of the loop is executed and Python prints the current number:

```
1
3
5
7
9
```

#### Avoiding Infinite Loops
Every while loop needs a way to stop running so it won’t continue to run forever. For example, this counting loop should count from 1 to 5:

```
x = 1
while x <= 5:
    print(x)
    x += 1
```

However, if you accidentally omit the line x += 1, the loop will run forever:

```
# This loop runs forever!
x = 1
while x <= 5:
    print(x)
```

Now the value of x will start at 1 but never change. As a result, the conditional test x <= 5 will always evaluate to True and the while loop will run forever, printing a series of 1s, like this:

```
1
1
1
1
--snip--
```

Every programmer accidentally writes an infinite while loop from time to time, especially when a program’s loops have subtle exit conditions. If your program gets stuck in an infinite loop, press CTRL-C or just close the terminal window displaying your program’s output.

To avoid writing infinite loops, test every while loop and make sure the loop stops when you expect it to. If you want your program to end when the user enters a certain input value, run the program and enter that value. If the program doesn’t end, scrutinize the way your program handles the value that should cause the loop to exit. Make sure at least one part of the program can make the loop’s condition False or cause it to reach a break statement.

>NOTE:
>
>VS Code, like many editors, displays output in an embedded terminal window. To cancel an infinite loop, make sure you click in the output area of the editor before pressing CTRL-C.


#### Using a while Loop with Lists and Dictionaries
So far, we’ve worked with only one piece of user information at a time. We received the user’s input and then printed the input or a response to it. The next time through the while loop, we’d receive another input value and respond to that. But to keep track of many users and pieces of information, we’ll need to use lists and dictionaries with our while loops.

A for loop is effective for looping through a list, but you shouldn’t modify a list inside a for loop because Python will have trouble keeping track of the items in the list. To modify a list as you work through it, use a while loop. Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and report on later.

#### Moving Items from One List to Another
Consider a list of newly registered but unverified users of a website. After we verify these users, how can we move them to a separate list of confirmed users? One way would be to use a while loop to pull users from the list of unconfirmed users as we verify them and then add them to a separate list of confirmed users. Here’s what that code might look like:

```
# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
❶ unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
❷ while unconfirmed_users:
❸     current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
❹     confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

We begin with a list of unconfirmed users ❶ (Alice, Brian, and Candace) and an empty list to hold confirmed users. The while loop runs as long as the list `unconfirmed_users` is not empty ❷. Within this loop, the `pop()` method removes unverified users one at a time from the end of `unconfirmed_users` ❸. Because Candace is last in the `unconfirmed_users` list, her name will be the first to be removed, assigned to `current_user`, and added to the `confirmed_users` list ❹. Next is Brian, then Alice.

We simulate confirming each user by printing a verification message and then adding them to the list of confirmed users. As the list of unconfirmed users shrinks, the list of confirmed users grows. When the list of unconfirmed users is empty, the loop stops and the list of confirmed users is printed:

```
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
Candace
Brian
Alice
```

#### Removing All Instances of Specific Values from a List
In Chapter 3, we used `remove()` to remove a specific value from a list. The `remove()` function worked because the value we were interested in appeared only once in the list. But what if you want to remove all instances of a value from a list?

Say you have a list of pets with the value `cat` repeated several times. To remove all instances of that value, you can run a while loop until `cat` is no longer in the list, as shown here:

```
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

We start with a list containing multiple instances of `cat`. After printing the list, Python enters the while loop because it finds the value `cat` in the list at least once. Once inside the loop, Python removes the first instance of `cat`, returns to the while line, and then reenters the loop when it finds that `cat` is still in the list. It removes each instance of `cat` until the value is no longer in the list, at which point Python exits the loop and prints the list again:

```
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
```

## Resources

[Python Documentation](https://docs.python.org/3/)


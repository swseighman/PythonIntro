# Data Types

## Strings

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
name = "joe thomas"
print(name.title())
```

>`title` is a Python method which are functions that are associated with objects. Methods are used to perform actions on objects.

Save this file as `name.py` and then run it. You should see this output:

```
Joe Thomas
```

In this example, the variable name refers to the lowercase string `joe thomas`. The method `title()` appears after the variable in the `print()` call. A method is an action that Python can perform on a piece of data (object). The dot (.) after name in `name.title()` tells Python to make the `title()` method act on the variable name. Every method is followed by a set of parentheses, because methods often need additional information to do their work. That information is provided inside the parentheses. The `title()` function doesn’t need any additional information, so its parentheses are empty.

The `title()` method changes each word to title case, where each word begins with a capital letter. This is useful because you’ll often want to think of a name as a piece of information. For example, you might want your program to recognize the input values Joe, JOE, and joe as the same name, and display all of them as Joe.

Several other useful methods are available for dealing with case as well. For example, you can change a string to all uppercase or all lowercase letters like this:

```
name = "Joe Thomas"
print(name.upper())
print(name.lower())
```

This will display the following:

```
JOE THOMAS 
joe thomas
```

The `lower()` method is particularly useful for storing data. You typically won’t want to trust the capitalization that your users provide, so you’ll convert strings to lowercase before storing them. Then when you want to display the information, you’ll use the case that makes the most sense for each string.

#### Using Variables in Strings

In some situations, you’ll want to use a variable’s value inside a string. For example, you might want to use two variables to represent a first name and a last name, respectively, and then combine those values to display someone’s full name:

```
first_name = "joe"
last_name = "thomas"
full_name = f"{first_name} {last_name}" ❶ 
print(full_name)
```

To insert a variable’s value into a string, place the letter `f` immediately before the opening quotation mark ❶. Put braces around the name or names of any variable you want to use inside the string. Python will replace each variable with its value when the string is displayed.

These strings are called f-strings. The `f` is for format, because Python formats the string by replacing the name of any variable in braces with its value. The output from the previous code is:

```
joe thomas
```

You can do a lot with f-strings. For example, you can use f-strings to compose complete messages using the information associated with a variable, as shown here:

```
first_name = "joe"
last_name = "thomas"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!") ❶ 
```

The `full name` is used in a sentence that greets the user ❶, and the `title()` method changes the name to title case. This code returns a simple but nicely formatted greeting:

```
Hello, Joe Thomas!
```

You can also use f-strings to compose a message, and then assign the entire message to a variable:

```
first_name = "joe"
last_name = "thomas"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!" ❶ 
print(message) ❷ 
```

This code displays the message Hello, Joe Thomas! as well, but by assigning the message to a variable ❶ we make the final `print()` call much simpler ❷.

#### Adding Whitespace to Strings with Tabs or Newlines

In programming, whitespace refers to any nonprinting characters, such as spaces, tabs, and end-of-line symbols. You can use whitespace to organize your output so it’s easier for users to read.

To add a tab to your text, use the character combination \t:

```
>>> print("Go Browns!")
Python
>>> print("\tGo Browns!")
    Go Browns!
```

To add a newline in a string, use the character combination \n:

```
>>> print("Teams:\nBrowns\nSteelers\nBengals\nRavens")
Teams:
Browns
Steelers
Bengals
Ravens
```

You can also combine tabs and newlines in a single string. The string "\n\t" tells Python to move to a new line, and start the next line with a tab. The following example shows how you can use a one-line string to generate four lines of output:

```
>>> print("Teams:\n\tBrowns\n\tSteelers\n\tBengals\n\tRavens")
Teams:
    Browns
    Steelers
    Bengals
    Ravens
```
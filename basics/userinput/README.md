# Python Basics

## User Input

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
prompt = "\nIf you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!\n")
```

This example shows one way to build a multiline string. The first line assigns the first part of the message to the variable prompt. In the second line, the operator `+=` takes the string that was assigned to prompt and adds the new string onto the end.

The prompt now spans two lines, again with space after the question mark for clarity:

```
If you share your name, we can personalize the messages you see.
What is your first name? Scott

Hello, Scott!
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

We can resolve this issue by using the `int()` function, which converts the input string to a numerical value. This allows the comparison to run successfully:

```
>>> age = input("How old are you? ")
How old are you? 21
>>> age = int(age) ❶ 
>>> age >= 18
True
```

In this example, when we enter 21 at the prompt, Python interprets the number as a string, but the value is then converted to a numerical representation by int() ❶. Now Python can run the conditional test: it compares age (which now represents the numerical value 21) and 18 to see if age is greater than or equal to 18. This test evaluates to True.

How do you use the `int()` function in an actual program? Consider a program that determines whether people are tall enough to ride a roller coaster:

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
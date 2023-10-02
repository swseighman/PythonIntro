### Python Basics

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
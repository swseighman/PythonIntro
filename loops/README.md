# Python Basics

## Loops
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
# Python Basics

## Loops
You’ll often want to run through all entries in a list, performing the same task with each item. For example, in a game you might want to move every element on the screen by the same amount. In a list of numbers, you might want to perform the same statistical operation on every element. Or perhaps you’ll want to display each headline from a list of articles on a website. When you want to do the same action with every item in a list, you can use Python’s for loop.

Say we have a list of toppings, and we want to print out each topping in the list. We could do this by retrieving each topping from the list individually, but this approach could cause several problems. For one, it would be repetitive to do this with a long list of toppings. Also, we’d have to change our code each time the list’s length changed. Using a for loop avoids both of these issues by letting Python manage these issues internally.

Let’s use a for loop to print out each topping in a list of toppings:

```
toppings = [`pepperoni`, `sausage`, `cheese`]
for toppings in toppings:
    print(toppings)
```
    
We begin by defining a list, then we define a for loop. This line tells Python to pull a topping from the list toppings, and associate it with the variable topping. Next, we tell Python to print the topping that’s just been assigned to topping. Python then repeats these last two lines, once for each topping in the list. It might help to read this code as “For every topping in the list of toppings, print the topping’s topping.” The output is a simple printout of each topping in the list:

```
pepperoni
sausage
cheese
```

#### A Closer Look at Looping
Looping is important because it’s one of the most common ways a computer automates repetitive tasks. For example, in a simple loop like we used in `toppings.py`, Python initially reads the first line of the loop:

```
for topping in toppings:
```

This line tells Python to retrieve the first value from the list toppings and associate it with the variable topping. This first value is `pepperoni`. Python then reads the next line:

```
print(topping)
```

Python prints the current value of topping, which is still `pepperoni`. Because the list contains more values, Python returns to the first line of the loop:

```
for topping in toppings:
```

Python retrieves the next topping in the list, `sausage`, and associates that value with the variable topping. Python then executes the line:

```
print(topping)
```

Python prints the current value of topping again, which is now `sausage`. Python repeats the entire loop once more with the last value in the list, `cheese`. Because no more values are in the list, Python moves on to the next line in the program. In this case nothing comes after the for loop, so the program ends.

When you’re using loops for the first time, keep in mind that the set of steps is repeated once for each item in the list, no matter how many items are in the list. If you have a million items in your list, Python repeats these steps a million times—and usually very quickly.

Also keep in mind when writing your own for loops that you can choose any name you want for the temporary variable that will be associated with each value in the list. However, it’s helpful to choose a meaningful name that represents a single item from the list. For example, here’s a good way to start a for loop for a list of cats, a list of dogs, and a general list of items:

```
for cat in cats:
for dog in dogs:
for item in list_of_items:
```

These naming conventions can help you follow the action being done on each item within a for loop. Using singular and plural names can help you identify whether a section of code is working with a single element from the list or the entire list.

#### Doing More Work Within a for Loop
You can do just about anything with each item in a for loop. Let’s build on the previous example by printing a message to each topping, telling them how much you like each topping:

```
toppings = [`pepperoni`, `sausage`, `cheese`]
for topping in toppings:
    print(f"{topping.title()} is the best!")
```

The only difference in this code is where we compose a message to each topping, starting with that topping’s topping. The first time through the loop the value of topping is `pepperoni`, so Python starts the first message with the topping `pepperoni`. The second time through, the message will begin with `sausage`, and the third time through, the message will begin with `cheese`.

The output shows a personalized message for each topping in the list:

```
pepperoni is the best!
sausage is the best!
cheese is the best!
```

You can also write as many lines of code as you like in the for loop. Every indented line following the line for topping in toppings is considered inside the loop, and each indented line is executed once for each value in the list. Therefore, you can do as much work as you like with each value in the list.

Let’s add a second line to our message, telling each topping that we’re looking forward to their next trick:

```
toppings = [`pepperoni`, `sausage`, `cheese`]
for topping in toppings:
    print(f"{topping.title()} is the best!")
    print(f"I can`t wait to try {topping.title()}.\n")
```

Because we have indented both calls to `print()`, each line will be executed once for every topping in the list. The newline `("\n")` in the second print() call inserts a blank line after each pass through the loop. This creates a set of messages that are neatly grouped for each person in the list:

```
pepperoni is the best!
I can`t wait to try pepperoni.

sausage is the best!
I can`t wait to try sausage.

cheese is the best!
I can`t wait to try cheese.
```

You can use as many lines as you like in your for loops. In practice, you’ll often find it useful to do a number of different operations with each item in a list when you use a for loop.

#### Doing Something After a for Loop
What happens once a for loop has finished executing? Usually, you’ll want to summarize a block of output or move on to other work that your program must accomplish.

Any lines of code after the for loop that are not indented are executed once without repetition. Let’s write a thank you to the group of toppings as a whole, thanking the chef for a great pizza. To display this group message after all of the individual messages have been printed, we place the thank you message after the for loop, without indentation:

```
toppings = [`pepperoni`, `sausage`, `cheese`]
for topping in toppings:
    print(f"{topping.title()} is the best!")
    print(f"I can`t wait to try {topping.title()}.\n")

print("Thank you chef, that pizza was great!\n")
```

The first two calls to `print()` are repeated once for each topping in the list, as you saw earlier. However, because the last line is not indented, it’s printed only once:

```
pepperoni is the best!
I can`t wait to try pepperoni.

sausage is the best!
I can`t wait to try sausage.

cheese is the best!
I can`t wait to try cheese.

Thank you chef, that pizza was great!
```

When you’re processing data using a for loop, you’ll find that this is a good way to summarize an operation that was performed on an entire dataset. For example, you might use a for loop to initialize a game by running through a list of characters and displaying each character on the screen. You might then write some additional code after this loop that displays a Play Now button after all the characters have been drawn to the screen.
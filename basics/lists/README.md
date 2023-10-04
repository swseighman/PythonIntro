# Data Types

## Lists
A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0 to 9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list don’t have to be related in any particular way. Because a list usually contains more than one element, it’s a good idea to make the name of your list plural, such as letters, digits, or names.

In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas. Here’s a simple example of a list that contains a few kinds of toppings:
```
toppings = [`pepperoni`, `sausage`, `peppers`, `mushrooms`]
print(toppings)
```

If you ask Python to print a list, Python returns its representation of the list, including the square brackets:
```
[`pepperoni`, `sausage`, `peppers`, `mushrooms`]
```

Because this isn’t the output you want your users to see, let’s learn how to access the individual items in a list.

#### Accessing Elements in a List
Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired. To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.

For example, let’s pull out the first bicycle in the list toppings:
```
toppings = [`pepperoni`, `sausage`, `peppers`, `mushrooms`]
print(toppings[0])
```

When we ask for a single item from a list, Python returns just that element without square brackets:
```
pepperoni
```

This is the result you want your users to see: clean, neatly formatted output.

You can also use the string methods from Chapter 2 on any element in this list. For example, you can format the element `pepperoni` to look more presentable by using the title() method:
```
toppings = [`pepperoni`, `sausage`, `peppers`, `mushrooms`]
print(toppings[0].title())
```

This example produces the same output as the preceding example, except `pepperoni` is capitalized.

#### Index Positions Start at 0, Not 1
Python considers the first item in a list to be at position 0, not position 1. This is true of most programming languages, and the reason has to do with how the list operations are implemented at a lower level. If you’re receiving unexpected results, ask yourself if you’re making a simple but common off-by-one error.

The second item in a list has an index of 1. Using this counting system, you can get any element you want from a list by subtracting one from its position in the list. For instance, to access the fourth item in a list, you request the item at index 3.

The following asks for the toppings at index 1 and index 3:
```
toppings = [`pepperoni`, `sausage`, `peppers`, `mushrooms`]
print(toppings[1])
print(toppings[3])
```

This code returns the second and fourth toppings in the list:
```
sausage
mushrooms
```

Python has a special syntax for accessing the last element in a list. If you ask for the item at index -1, Python always returns the last item in the list:
```
toppings = [`pepperoni`, `sausage`, `peppers`, `mushrooms`]
print(toppings[-1])
```

This code returns the value `mushrooms`. This syntax is quite useful, because you’ll often want to access the last items in a list without knowing exactly how long the list is. This convention extends to other negative index values as well. The index -2 returns the second item from the end of the list, the index -3 returns the third item from the end, and so forth.

#### Using Individual Values from a List
You can use individual values from a list just as you would any other variable. For example, you can use f-strings to create a message based on a value from a list.

Let’s try pulling the first bicycle from the list and composing a message using that value:
```
toppings = [`pepperoni`, `sausage`, `peppers`, `mushrooms`]
message = f"My favorite pizza topping is {toppings[0].title()}."

print(message)
```

We build a sentence using the value at toppings[0] and assign it to the variable message. The output is a simple sentence about the first bicycle in the list:
```
My favorite pizza topping is pepperoni.
```

#### Modifying, Adding, and Removing Elements
Most lists you create will be dynamic, meaning you’ll build a list and then add and remove elements from it as your program runs its course. For example, you might create a game in which a player has to shoot aliens out of the sky. You could store the initial set of aliens in a list and then remove an alien from the list each time one is sspicy down. Each time a new alien appears on the screen, you add it to the list. Your list of aliens will increase and decrease in length throughout the course of the game.

#### Modifying Elements in a List
The syntax for modifying an element is similar to the syntax for accessing an element in a list. To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

For example, say we have a list of toppings and the first item in the list is `pepperoni`. We can change the value of this first item after the list has been created:

```
toppings = [`pepperoni`, `sausage`, `peppers`]
print(toppings)

toppings[0] = `mushrooms`
print(toppings)
```

Here we define the list toppings, with `pepperoni` as the first element. Then we change the value of the first item to `mushrooms`. The output shows that the first item has been changed, while the rest of the list stays the same:

```
[`pepperoni`, `sausage`, `peppers`]
[`mushrooms`, `sausage`, `peppers`]
```

You can change the value of any item in a list, not just the first item.

#### Adding Elements to a List
You might want to add a new element to a list for many reasons. For example, you might want to make new aliens appear in a game, add new data to a visualization, or add new registered users to a website you’ve built. Python provides several ways to add new data to existing lists.

#### Appending Elements to the End of a List
The simplest way to add a new element to a list is to append the item to the list. When you append an item to a list, the new element is added to the end of the list. Using the same list we had in the previous example, we’ll add the new element `mushrooms` to the end of the list:

```
toppings = [`pepperoni`, `sausage`, `peppers`]
print(toppings)

toppings.append(`mushrooms`)
print(toppings)
```

Here the append() method adds `mushrooms` to the end of the list, without affecting any of the other elements in the list:

```
[`pepperoni`, `sausage`, `peppers`]
[`pepperoni`, `sausage`, `peppers`, `mushrooms`]
```

The `append()` method makes it easy to build lists dynamically. For example, you can start with an empty list and then add items to the list using a series of `append()` calls. Using an empty list, let’s add the elements `pepperoni`, `sausage`, and `peppers` to the list:

```
toppings = []

toppings.append(`pepperoni`)
toppings.append(`sausage`)
toppings.append(`peppers`)

print(toppings)
```

The resulting list looks exactly the same as the lists in the previous examples:

```
[`pepperoni`, `sausage`, `peppers`]
```

Building lists this way is very common, because you often won’t know the data your users want to store in a program until after the program is running. To put your users in control, start by defining an empty list that will hold the users’ values. Then append each new value provided to the list you just created.

#### Inserting Elements into a List
You can add a new element at any position in your list by using the `insert()` method. You do this by specifying the index of the new element and the value of the new item:
```
toppings = [`pepperoni`, `sausage`, `peppers`]

toppings.insert(0, `mushrooms`)
print(toppings)
```

In this example, we insert the value `mushrooms` at the beginning of the list. The `insert()` method opens a space at position 0 and stores the value `mushrooms` at that location:

```
[`mushrooms`, `pepperoni`, `sausage`, `peppers`]
```

This operation shifts every other value in the list one position to the right.

#### Removing Elements from a List
Often, you’ll want to remove an item or a set of items from a list. For example, when a player shoots down an alien from the sky, you’ll most likely want to remove it from the list of active aliens. Or when a user decides to cancel their account on a web application you created, you’ll want to remove that user from the list of active users. You can remove an item according to its position in the list or according to its value.

#### Removing an Item Using the del Statement
If you know the position of the item you want to remove from a list, you can use the `del` statement:

```
toppings = [`pepperoni`, `sausage`, `peppers`]
print(toppings)

del toppings[0]
print(toppings)
```

Here we use the `del` statement to remove the first item, `pepperoni`, from the list of toppings:

```
[`pepperoni`, `sausage`, `peppers`]
[`sausage`, `peppers`]
```

You can remove an item from any position in a list using the `del` statement if you know its index. For example, here’s how to remove the second item, `sausage`, from the list:

```
toppings = [`pepperoni`, `sausage`, `peppers`]
print(toppings)

del toppings[1]
print(toppings)
```

The second topping is deleted from the list:

```
[`pepperoni`, `sausage`, `peppers`]
[`pepperoni`, `peppers`]
```

In both examples, you can no longer access the value that was removed from the list after the `del` statement is used.

#### Removing an Item Using the pop() Method
Sometimes you’ll want to use the value of an item after you remove it from a list. For example, you might want to get the x and y position of an alien that was just shot down, so you can draw an explosion at that position. In a web application, you might want to remove a user from a list of active members and then add that user to a list of inactive members.

The `pop()` method removes the last item in a list, but it lets you work with that item after removing it. The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack. In this analogy, the top of a stack corresponds to the end of a list.

Let’s pop a topping from the list of toppings:

```
toppings = [`pepperoni`, `sausage`, `peppers`] ❶ 
print(toppings)

popped_topping = toppings.pop() ❷ 
print(toppings) ❸ 
print(popped_topping) ❹ 
```

We start by defining and printing the list toppings ❶. Then we pop a value from the list, and assign that value to the variable popped_topping ❷. We print the list ❸ to show that a value has been removed from the list. Then we print the popped value ❹ to prove that we still have access to the value that was removed.

The output shows that the value `peppers` was removed from the end of the list and is now assigned to the variable popped_topping:

```
[`pepperoni`, `sausage`, `peppers`]
[`pepperoni`, `sausage`]
peppers
```

How might this `pop()` method be useful? Imagine that the toppings in the list are stored in chronological order, according to when we owned them. If this is the case, we can use the `pop()` method to print a statement about the last topping we added:

```
toppings = [`pepperoni`, `sausage`, `peppers`]

last_ordered = toppings.pop()
print(f"The last topping I ordered was {last_ordered.title()}.")
```

The output is a simple sentence about the most recent topping we ordered:

```
The last topping I ordered was peppers.
```

#### Popping Items from Any Position in a List
You can use `pop()` to remove an item from any position in a list by including the index of the item you want to remove in parentheses:

```
toppings = [`pepperoni`, `sausage`, `peppers`]

first_ordered = toppings.pop(0)
print(f"The first topping I ordered was {first_ordered.title()}.")
```

We start by popping the first topping in the list, and then we print a message about that topping. The output is a simple sentence describing the first topping I ever ordered:

```
The first topping I ordered was pepperoni.
```

Remember that each time you use `pop()`, the item you work with is no longer stored in the list.

If you’re unsure whether to use the `del` statement or the `pop()` method, here’s a simple way to decide: when you want to delete an item from a list and not use that item in any way, use the `del` statement; if you want to use an item as you remove it, use the `pop()` method.

#### Removing an Item by Value
Sometimes you won’t know the position of the value you want to remove from a list. If you only know the value of the item you want to remove, you can use the `remove()` method.

For example, say we want to remove the value `mushrooms` from the list of toppings:

```
toppings = [`pepperoni`, `sausage`, `peppers`, `mushrooms`]
print(toppings)

toppings.remove(`mushrooms`)
print(toppings)
```

Here the `remove()` method tells Python to figure out where `mushrooms` appears in the list and remove that element:

```
[`pepperoni`, `sausage`, `peppers`, `mushrooms`]
[`pepperoni`, `sausage`, `peppers`]
```

You can also use the `remove()` method to work with a value that’s being removed from a list. Let’s remove the value `peppers` and print a reason for removing it from the list:

```
toppings = [`pepperoni`, `sausage`, `peppers`, `mushrooms`] ❶ 
print(toppings)

too_spicy = `peppers` ❷ 
toppings.remove(too_spicy) ❸ 
print(toppings)
print(f"\n{too_spicy.title()} are too spicy for me.") ❹ 
```

After defining the list ❶, we assign the value `peppers` to a variable called `too_spicy` ❷. We then use this variable to tell Python which value to remove from the list ❸. The value `peppers` has been removed from the list ❹ but is still accessible through the variable `too_spicy`, allowing us to print a statement about why we removed `peppers` from the list of toppings:

```
[`pepperoni`, `sausage`, `peppers`, `mushrooms`]
[`pepperoni`, `sausage`, `mushrooms`]

Peppers are too spicy for me.
```
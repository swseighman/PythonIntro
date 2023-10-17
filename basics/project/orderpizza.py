# Let's set some variables
# Create an empty list to use for toppings
toppings = []
# Our base pizza price
basepizzaprice = 5.00
# Price for each topping
topping = 0.75
# We'll use the order 'flag' to monitor state for our loop
order = True

# Get input from user
question = input("Would you like to order a pizza? (Yes or No): ")

# Let's add some logic
# Using .lower() so users can enter 'Yes' or 'yes'
if question.lower() == "yes":
    addtopping = input("Please add a topping (Press enter for plain): ")
    # If the user hits enter, set flag to False, exit the loop and move to the calculations
    if addtopping == "":
       # Exit
       order = False
    else:
      # If the user enters a topping, add it to our list
      toppings.append(addtopping)
      # Begin a while loop until the user hits enter
      while (order == True):
         moretoppings = input("Add another topping or press enter to finish): ")
         # If the user presses enter (to finish) set flag to False, exit the loop and move to the calculation
         if moretoppings == "":
           # Exit loop
           order = False
         # Otherwise add another topping and loop back
         else:
           toppings.append(moretoppings)
    
    # Get the total number of toppings
    toppingAmount = len(toppings)
    # Start with the base pizza price (5.00) and add the number of toppings * .75
    pizzaPrice = basepizzaprice + (toppingAmount * topping)
    print("")
    # Print out the total number of toppings
    print(f"You ordered a cheese pizza with {toppingAmount} toppings.")
    # Print out the total price
    print(f"Your total is ${pizzaPrice:.2f}")
    print("")
               
else:
    print("OK, but you'll be hungry later!")
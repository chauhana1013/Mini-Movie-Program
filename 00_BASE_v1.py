# Functions...

# Checks user has entered yes / no to a question
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        
        elif response == "no" or response == "n":
            return "no"
        
        else:
            print("Please enter yes or no")

# Checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # If user's response is blank, program displays this message
        if response == "":
            print("Sorry this can't be blank. Please try again")
        
        else:
            return response

# Checks users enter an integer to a given question
def num_check(question): 
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError: 
            print("Please enter an integer")

# Calculate the ticket price based on the age 
def calc_ticket_price(var_age):

    # Ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5
    
    # Ticket is $10.50 for users under 65
    elif var_age < 65:
        price = 10.5 

    # Ticket price is $6.5 for seniors (65+)
    else:
        price = 6.5

    return price




# Main Routine...

# Set values for Testing
max_tickets = 3
tickets_sold = 0

# Asks user if they want to see the instructions
print()
want_instructions= yes_no("Do you want to read the instructions? ").lower()

# If they say yes, output 'program continues'
if want_instructions == "yes":  
    print("Display Instructions")
print()

# Loop for selling tickets
while tickets_sold < max_tickets:

    # Program asks user
    name = not_blank("Please enter your name or 'xxx' to quit: ").lower()

    if name == "xxx":
        break
    
    age = num_check("Your Age: ")


    if 12 <= age <= 120:
        pass

    elif age < 12:
        print("You're too young for this movie")
        continue

    else:
        print("?? That looks like a typo, please try again")
        continue

    # Calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print(f"Age: {age}, Ticket Price: ${ticket_cost:.2f}")
    
    tickets_sold += 1
    


# If all tickets sold out, program ends
if tickets_sold == max_tickets:
    print("Congratulations you have sold all tickets.")

# If the Max Amount of tickets not sold, it shows how many are left and how many were sold
else:   
    print(f"You sold {tickets_sold} ticket/s. There is {max_tickets - tickets_sold} ticket/s still left")

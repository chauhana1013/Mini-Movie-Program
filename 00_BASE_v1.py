# Functions...

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

# Checks that users enter a valid response (eg yes / no / cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):
    
    error = f"Please choose {valid_responses[0]} or {valid_responses[1]}"

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item
        
        print(error)




# Main Routine...

# Set values for Testing
max_tickets = 3
tickets_sold = 0

# Lists for String Checker 
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]



# Asks user if they want to see the instructions
print()
want_instructions = string_checker("Do you want to read the instructions? ", 1, yes_no_list)

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
    
    # Get payment method
    pay_method = string_checker("Payment method: ", 2, payment_list)
    
    tickets_sold += 1
    


# If all tickets sold out, program ends
if tickets_sold == max_tickets:
    print("Congratulations you have sold all tickets.")

# If the Max Amount of tickets not sold, it shows how many are left and how many were sold
else:   
    print(f"You sold {tickets_sold} ticket/s. There is {max_tickets - tickets_sold} ticket/s still left")

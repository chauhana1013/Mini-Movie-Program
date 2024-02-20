import pandas
import random
from datetime import date

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


# Checks that users enter a valid response (e.g. yes / no / cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):
    
    error = f"Please choose {valid_responses[0]} or {valid_responses[1]}"

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item
        
        print(error)


# Currency Formatting Function
def currency(x):
    return f"${x:.2f}"


# Main Routine...

# Set values for Testing
max_tickets = 5
tickets_sold = 0

# Lists for String Checker 
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Dictionaries to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# Dictionary used to create data frame
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

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

    if pay_method == "cash":
        surcharge = 0

    else:
        # Calculate 5% surcharge if users are paying by credit card
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # Add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

# Create data frame from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)


# Calculate the total cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# Choose a winner from our name list
winner_name = random.choice(all_names)

# Get position of winner name in list
win_index = all_names.index(winner_name)

# Look up total amount won (ie: ticket price +surcharge)
total_won = mini_movie_frame.at[win_index, 'Total']

mini_movie_frame = mini_movie_frame.set_index('Name')

print("*---- Ticket Data ----*")

# Output table with ticket data
print(mini_movie_frame)

print()
print("*---- Ticket Cost / Profit ----*")

# Output total ticket sales and profit
print(f"Total Ticket Sales: ${total:.2f}")
print(f"Total Profit: ${profit:.2f}")

print()
print("*---- Raffle Winner ----*")
print(f"Congratulations {winner_name}. You have won {total_won} ie: your ticket is free")


if tickets_sold == max_tickets:
    print("Congratulations you have sold all tickets.")

# If the Max Amount of tickets not sold, it shows how many are left and how many were sold
else:   
    print(f"You sold {tickets_sold} ticket/s. There is {max_tickets - tickets_sold} ticket/s still left")

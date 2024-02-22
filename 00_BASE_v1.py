import pandas
import random
from datetime import date

# Functions...


# Shows Instructions
def show_instructions():
    print('''\n 
***** Instructions *****

For each ticket, enter ...
- The person's name (can't be blank)
- Age (between 12 and 120)
- Payment Method (Cash / Credit)    

When you have entered all the users, press 'xxx' to quit.

The program will then display the ticket details
including the cost of each ticket, the total cost 
and the total profit.

This information will also be automatically written to a text file.

*************************''')


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
want_instructions = string_checker("Do you want to read the instructions (y/n): ", 1, yes_no_list)

# If they say yes, output 'program continues'
if want_instructions == "yes":  
    show_instructions()
print()

# Loop for selling tickets
while tickets_sold < max_tickets:

    # Program asks user
    name = not_blank("Please enter your name or 'xxx' to quit: ").lower()

    # Exit Loop if users type 'xxx' and have sold at least one ticket
    if name == "xxx" and len(all_names) > 0:
        break
    elif name == "xxx":
        print("You must sell at least ONE ticket before quitting")
        continue

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

# Choose winner and look up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']


# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)


mini_movie_frame = mini_movie_frame.set_index('Name')

# **** Get current date for heading and file name ****
# Get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = f"---- Mini Movie Fundraiser Ticket Data ({day}/{month}/{year}) ----\n"
filename = f"MMF_{year}_{month}_{day}"

# Change frame to a string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# Create strings for printing
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = f"Total Ticket Sales: ${total:.2f}"
total_profit = f"Total Profit: ${profit:.2f}"

# Shows how many tickets have been sold


if tickets_sold == max_tickets:
    sales_status = "\n*** All the tickets have been sold ***"

# If the Max Amount of tickets not sold, it shows how many are left and how many were sold
else:
    sales_status = f"\n***** You sold {tickets_sold} out of {max_tickets} tickets *****"

winner_heading = "\n---- Raffle Winner ----"
winner_text = f"The winner of the raffle is {winner_name}. They have won ${total_won:.2f} i.e. Their ticket is free!"

print()
# List holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading, total_ticket_sales, total_profit,
            sales_status, winner_heading, winner_text]

for item in to_write:
    print(item)

# Write output to file create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# Close File
text_file.close()




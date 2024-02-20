import pandas
import random
from datetime import date

# Currency Formatting Function
def currency(x):
    return f"${x:.2f}"

# Dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}
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

# Set index at end (before printing)
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
total_ticket_sales = f"Total Ticket Sales: ${total}"
total_profit = f"Total Profit: ${profit}"

# Edit text below!! I
sales_status = "\n*** All the tickets have been sold ***"

winner_heading = "\n---- Raffle Winner ----"
winner_text = f"The winner of the raffle is {winner_name}. They have won ${total_won} i.e. Their ticket is free!"

# List holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading, total_ticket_sales, total_profit, sales_status, winner_heading, winner_text]

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







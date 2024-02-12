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
print

# Loop for selling tickets
while True:

    # If all tickets sold out, program ends
    if max_tickets == 0:
        print("Congratulations you have sold all tickets.")
        break
    
    # Program asks user
    name = input("Please enter your name or 'xxx' to quit ").lower()

    if name != "xxx":
        tickets_sold += 1
        max_tickets -= 1
    
    # If the Max Amount of tickets not sold, it shows how many are left and how many were sold
    else:
        print(f"You sold {tickets_sold} ticket/s. There is {max_tickets} ticket/s still left")
        break
    
    # Testing if program functions properly
    print(max_tickets)

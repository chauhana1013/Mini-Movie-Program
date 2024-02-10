# Main Routine...

# Set values for Testing
max_tickets = 3
tickets_sold = 0

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

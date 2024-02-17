# Functions go here
def cash_credit(question):

    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"
        
        elif response == "credit" or response == "cr":
            return "credit"
        
        else:
            print("Please choose a valid payment method")


# Main Routine goes here

while True:
# Ask the user for payment method
    print()
    payment_method = cash_credit("Choose a payment method (cash or credit): ").lower()

    print("You chose", payment_method)


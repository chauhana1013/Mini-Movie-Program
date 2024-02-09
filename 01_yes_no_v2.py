# Functions go here
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        
        elif response == "no" or response == "n":
            return "no"
        
        else:
            print("Please enter yes or no")




# Main Routine goes here

while True:
# Ask the user if they have played before
    print()
    want_instructions= yes_no("Do you want to read the instructions? ").lower()

    # If they say yes, output 'program continues'
    if want_instructions == "yes":  
        print("Display Instructions")

    print("Program Continues...")
    print
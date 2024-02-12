# Functions go here

# Checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        
        else:
            return response

# Main Routine...

while True:
    username = not_blank("Please enter your name or 'xxx' to quit ")

    if username == "xxx":
        
        break
    
    print("Program continues")    

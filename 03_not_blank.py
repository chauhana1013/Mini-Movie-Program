# Functions go here

# Checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # If user's response is blank, program displays this message
        if response == "":
            print("Sorry this can't be blank. Please try again")
        
        else:
            return response

# Main Routine...

while True:
    username = not_blank("Please enter your name or 'xxx' to quit ")

    # Program ends if user types in the exit code
    if username == "xxx":
        break
          
print("We are done")  
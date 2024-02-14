# Functions...

# Checks users enter an integer to a given question
def num_check(question): 
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError: 
            print("Please enter an integer")

# Main Routine...
tickets_sold = 0

while True:

    name = input("Enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = num_check("Your Age: ")

    if age < 12:
        print("You're too young for this movie")
        continue

    elif age > 120:
        print("?? That looks like a typo, please try again")
        continue
    else:
        pass
    
    tickets_sold += 1

print (f"You sold {tickets_sold} tickets")

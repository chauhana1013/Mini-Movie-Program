want_instructions = ""
while want_instructions != "xxx":

    # Ask the user if they have played before
    print()
    want_instructions= input("Do you want to read the instructions? ").lower()

    # If they say yes, output 'program continues'
    if want_instructions == "yes" or want_instructions == "y":
        want_instructions = "yes"
        print("Display Instructions")

    # If they say no, output 'display instructions'
    elif want_instructions == "no" or want_instructions == "n":
        want_instructions = "no"
        print("Program Continues")

    # If they say something else, the code asks them to answer in yes/no
    else:
        print("Please answer yes / no")

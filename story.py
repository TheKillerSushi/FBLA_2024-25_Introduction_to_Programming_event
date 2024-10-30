# Imported Libraries


# Story procedures functions
    

def create_start_state(): # This function prints the start screen of the story and presents the user with options on what they want to do

    print("FILTER\n\n")

    print('Type "stop" at anytime to exit the program.\n\n')

    # Taking user input to move to another 
    user_choice = ""
    while user_choice not in ["1", "2", "3", "stop"]:
        user_choice = input("Please choose an option:\n1) Start the story\n2) Help\n3) Settings\n\n")

create_start_state()
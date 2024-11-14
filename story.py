# Imported Libraries
import filters


# Global variables

# Make sure to include the result of the choice a list [prompt (short), choice, age]
all_user_choices = {} # This variable stores every user choice (that is significant) so that these choices can be made into a report

# Story procedures functions

def generate_user_choices(all_user_choices): # This function generates a report of the users main choices and actions throughout the story

    if len(all_user_choices) == 0:
        print("No choices Made!")
        return 1
    else:
        for choice in all_user_choices:
            print("You decided to {all_user_choices[choice[1]]} when presented the option to {all_user_choices[choice[0]]} when you were {all_user_choices[choice[2]]}")

def start_story(): # Starts the story and runs the entirety of it
        
        # all the fiter functions
        filters = {}

        # What filters are being used 
        filters_in_use = []
        
        # Each image (with filters included)
        images = {}

        # Question, [choice1, filter1], [choice2, fitler2]
        ALL_STORY_BEATS = [
            ["When you arrive at the beach, you see two areas you could photograph. Which one do you want to take a photo of?", ["Photograph the crystal blue ocean","BLUE"], ["2 Photograph the beach, the golden sand, pristine and undisturbed","YELLOW"]],
            []
        ]

        choices_made = 0
        for situation in ALL_STORY_BEATS:
            print("\n",situation[0])
            # What would user like to do?
            user_choice = ""
            while user_choice not in ["1","2","stop"]:
                user_choice = input(f"1 {situation[1][0]}\n{situation[2][0]}\n").lower()

            # User typed stop and this function returns 3 to mark the programs end. 1 chooses the first option and 2 chooses the second.
            if user_choice == "stop":
                return 3
            
            print("You chose to ", situation[int(user_choice)][1],"\n")
            choices_made += 1
            all_user_choices[choices_made] = situation[int(user_choice)][0]
            
            # FILTER LOGIC HERE
            


            filters_in_use.append(situation[int(user_choice)][2])

            
def start_help():
    print("--------------------")
    print("Help\n")

    # What would user like to do?
    user_choice = ""
    while user_choice not in ["1","2","stop"]:
        user_choice = input("What would you like to do?\n1 Return to start screen\n2 View FAQ\n\n").lower()

    # All Frequently asked questions [question, answer format]
    FAQ = [["How long is this story?", "This story is short and can be completed in a few minutes."],
           ["Do your choices actually have an impact on the outcome of the story?", "Every choice has an impact on the final remarks of the story and the final images you get."],
           ["Are there branching paths in this game?", "This story does not have branching paths, but it does have many possible combinations of pictures and filters for your images."],
           ["Why do the images get filtered?", "The pictures get filtered as an artistic design choice and to elevate the symbolism and ideas of the story."]]
    # User typed stop and this function returns 3 to mark that for other functions to use.
    if user_choice == "stop":
        return 3
    elif user_choice == "1":
        return 0
    elif user_choice == "2":
        print("Frequently Asked Questions")
        for i in FAQ:
            print("Question: ", i[0], "\nAnswer: ", i[1], "\n\n")

def create_start_state(): # This function prints the start screen of the story and presents the user with options on what they want to do
    print("--------------------")
    
    print("FILTER\n\n")

    print('Type the number corresponding to the choice you want to make or type "stop" at anytime to exit the program.\n\n')

    # Taking user input to move to another 
    user_choice = ""
    while user_choice != "stop":
        while user_choice not in ["1", "2", "stop"]:

            # Obtains user input and transfers it to lowercase to account for capitalization cases
            user_choice = input("Please choose an option:\n1 Start the story\n2 Help\n\n").lower()
    
        if user_choice == "1":

            # start the story
            # if statement is trying to figure out if the user typed stop
            story_state = start_story()
            if story_state == 3:
                return 0


        elif user_choice == "2":

            # start the help page
            # if statement is trying to figure out if the user typed stop
            if start_help() == 3:
                return 0


    # user has typed stop, end the program.
    return 0 
create_start_state()

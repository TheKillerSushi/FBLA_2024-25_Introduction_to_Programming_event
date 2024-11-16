# Imported Libraries
import filters
from PIL import Image
import math

# Global variables


all_user_choices = {} # This variable stores every user choice (that is significant) so that these choices can be made into a report

# Story procedures functions

def generate_user_choices(all_user_choices, choices_made): # This function generates a report of the users main choices and actions throughout the story

    if choices_made == 0:
        print("No choices Made!")
        return 1
    else:
        print("REPORT:\n")
        for choice in all_user_choices:
            print(f"You decided to {all_user_choices[choice][0]} causing your image to be filtered with the {all_user_choices[choice][1]} filter\n")
    input("click enter to continue")

def start_story(): # Starts the story and runs the entirety of it
        
        # IMAGE to filter
        image = Image.open("Beach.jpg")
        size = image.size


        # Question, [choice1, filter1], [choice2, fitler2]
        ALL_STORY_BEATS = [
            ["You are a newly 8 year old boy. It is your birthday, and as a present, you are given a camera by your parents. You are going to the beach to celebrate and you decide to bring the camera into what will become your lifelong passion. These are the some of the most important moments in your life. When you arrive at the beach, you see two areas you could photograph. Which one do you want to take a photo of?", ["Photograph the crystal blue ocean", "NONE"], ["Photograph the beach, the golden sand, pristine and undisturbed","NONE"]],
            ["After that day at the beach, you began photographing more things, particularly birds. As you grew, you reaelized that you hadn't really taken any photos that represented you. Now at the age of 12, you decided you wanted to start taking pictures that were more personal to you. Now what idea would be more personally significant to you?", ["Photograph your house, a place you can always feel safe, and a place you know you can return to no matter what", "sepia"], ["Photograph your bedroom, your HQ, where you can connect with your freinds from online, and where you can be alone", "gray"]],
            ["As a 16 year old, you began to branch out and hang out wiht more people, but after a fall you woke up and realized that you couldn't remember what had happened earlier in your life. Now, with your memorys fading forever, you need to choose how you want to remember your life thus far. What will you do?", ["Focus on your past and maybe miss some details", "dither"], ["Let your memory's fade, and keep whatever parts of the memory's you can hold onto", "blur"]]
        ]

        choices_made = 0
        for situation in ALL_STORY_BEATS:
            print("\n",situation[0])
            # What would user like to do?
            user_choice = ""
            while user_choice not in ["1","2","stop"]:
                user_choice = input(f"1 {situation[1][0]}\n2 {situation[2][0]}\n\n").lower()

            # User typed stop and this function returns 3 to mark the programs end. 1 chooses the first option and 2 chooses the second.
            if user_choice == "stop":
                return 3
            
            # Filtering based on user choice
            user_choice_int = int(user_choice)

            #if situation[user_choice_int][1] == "blue":
                #image = filters.blue_filter(image)
            #elif situation[user_choice_int][1] == "yellow":
                #image = filters.yellow_filter(image)
            if situation[user_choice_int][1] == "sepia":
                image = filters.sepia_filter(image)
            elif situation[user_choice_int][1] == "gray":
                image = filters.gray_filter(image)
            elif situation[user_choice_int][1] == "blur":
                image = filters.blur(image)
            elif situation[user_choice_int][1] == "dither":
                image = filters.dither(image)
    

            print("You chose to ", situation[user_choice_int][0],"\n")
            choices_made += 1
            all_user_choices[choices_made] = situation[user_choice_int]
        
            image.save("test.jpg")
        
        print("After all you had been through, and with what memory's you retained, you rediscovered your first photo ever and saw it thorugh a new lens. A new filter. How did your experiences shape what you see?")
        
        # Show the image to the user and closes it in the actual code
        image.show()
        image.close()
        generate_user_choices(all_user_choices,choices_made)
        

            
        

            
def start_help():

    print("Help\n")

    # What would user like to do?
    user_choice = ""
    while user_choice not in ["1","2","stop"]:
        user_choice = input("What would you like to do?\n1 Return to start screen\n2 View FAQ\n\n").lower()

    # All Frequently asked questions [question, answer format]
    FAQ = [["How long is this story?", "This story is short and can be completed in a few minutes."],
           ["Do your choices actually have an impact on the outcome of the story?", "The story mostly surrounds remembering your past with the biases of the future, and the final image is a reflection of that, and thus is the ending of the story in of itself meaning that your choices DO have an imapact on the outcome of the story."],
           ["Are there branching paths in this game?", "This story does not have branching paths, but it does have many possible combinations of choices you make which can lead to a brand new final image every time."],
           ["Why does the image get filtered?", "The picture gets filtered as an artistic design choice and to elevate the symbolism and ideas of the story which can make the end of the story more substantial by not outright concluding the story but allowing the user to SEE the outcome of their choices."]]
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
    user_choice = ""
    while user_choice != "stop":
    
        print("FILTER\n\n")

        print('Type the number corresponding to the choice you want to make or type "stop" at anytime to exit the program.\n\n')

        # Taking user input to move to another 
        

        user_choice = ""
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

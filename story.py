import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
import filters

# Initalize the screen
#window.attributes("-fullscreen", True)
#window = tk.Tk()
#window.configure(bg="#222831")

# Screen size for wrapping elements
#screen_width = window.winfo_screenwidth()
#screen_height = window.winfo_screenheight()



#def exit():
    #window.destroy()



class App(tk.Tk):
    def __init__(self):
        super().__init__()  

        self.filters = {
            "blue" : filters.blue_filter,
            "yellow" : filters.yellow_filter,
            "gray" : filters.gray_filter,
            "dither" : filters.dither,
            "blur" : filters.blur,
            "sepia" : filters.sepia_filter,
        }
        self.attributes("-fullscreen", True)
        self.frame_container = tk.Frame(self)
        self.frame_container.pack(fill="both", expand=True)

        self.choices = [[None,None],[None,None],[None,None]]

        self.main_image = Image.open("beach.jpg")

        self.frame_container.grid_rowconfigure(0, weight=1)
        self.frame_container.grid_columnconfigure(0, weight=1)

        self.used_frames = {}

        # Add every frame to the usable frames list and sets them up
        for FRAME in (main_screen, help_screen, story_screen_1, story_screen_2, story_screen_3, report_screen):
            frame = FRAME(parent=self.frame_container, controller=self,)
            self.used_frames[FRAME] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.display(main_screen)
    
    def display(self, FRAME):

        # Raise a frame to be the current one
        frame = self.used_frames[FRAME]
        frame.tkraise()

    def remember_choice(self, choice, info=[]):
        self.choices[choice] = info

        # Apply the filter to the main image
        self.main_image = self.filters[info[1]](self.main_image).copy()  # Ensure it's a new copy

        # Update the next frame’s image before switching
        for frame in (story_screen_1, story_screen_2, story_screen_3, report_screen):
            self.used_frames[frame].update_image()



    # Ends the program when the X is clicked

class main_screen(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(bg="#ECE6E6")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = tk.Label(self, text="Snapshot", font=("Castellar", 40), anchor="center", bg="#ECE6E6")
        label.grid(row=0, column=0, sticky="n", pady=20)
        

        # Buttons
        button_width = 7
        button_height = 1

        # Creates a button object to add to the grid
        story_button = tk.Button(self, text="STORY", font=("Cooper", 43), bg="#EEEEEE", command=self.display_story_1, width=button_width, height=button_height)
        story_button.grid(row=1, column=0, sticky="n", pady=50)
        
        help_button = tk.Button(self, text="HELP", font=("Cooper", 43), bg="#EEEEEE", command=self.display_help, width=button_width, height=button_height)
        help_button.grid(row=2, column=0, sticky="n", pady=50)

        quit_button = tk.Button(self, text="STOP", font=("Cooper", 43), bg="#EEEEEE", command=self.quit, width=button_width, height=button_height)
        quit_button.grid(row=3, column=0, sticky="n", pady=50)
    # Display each specified frame
    def display_help(self):
        self.controller.display(help_screen)

    def display_story_1(self):
        self.controller.display(story_screen_1)

    def display_story_2(self):
        self.controller.display(story_screen_2)
    
    def display_story_3(self):
        self.controller.display(story_screen_3)
    def quit(self):
        self.controller.destroy()
    
class help_screen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(bg="#ECE6E6")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = tk.Label(self, text="Help", font=("Castellar", 40), anchor="center", bg="#ECE6E6")
        label.grid(row=0, column=0, sticky="n", pady=20)
        
        # HELP information
        label_mouse = tk.Label(self, text="Navigate with your mouse and click on buttons to make choices.", font=("Century Gothic", 28), anchor="center", bg="#ECE6E6", wraplength=self.screen_width*0.5)
        label_mouse.grid(row=1, column=0, stick="n", pady=20)

        label_quit = tk.Label(self, text="Quit using the quit button or the X in the top right of the story. PROGRESS WILL NOT SAVE!", font=("Century Gothic", 28), anchor="center", bg="#ECE6E6", wraplength=self.screen_width*0.5)
        label_quit.grid(row=2, column=0, stick="n", pady=20)

        label_fun = tk.Label(self, text="Please enjoy the story, your choices have a visible impact :)", font=("Century Gothic", 28), anchor="center", bg="#ECE6E6", wraplength=self.screen_width*0.5)
        label_fun.grid(row=3, column=0, stick="n", pady=20)        
        # Button
        button_width = 7
        button_height = 1

        quit_button = tk.Button(self, text="Return", font=("Cooper", 43), bg="#EEEEEE", command=self.return_to_main, width=button_width, height=button_height)
        quit_button.grid(row=4, column=0, sticky="n", pady=50)
    
    def return_to_main(self):
        self.controller.display(main_screen)

class story_screen_1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#ECE6E6")

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Story title
        label = tk.Label(self, text="Story", font=("Castellar", 40), bg="#ECE6E6")
        label.grid(row=0, column=0, columnspan=2, pady=20)

        # Story text
        label_prompt = tk.Label(self, text="You are a newly 8-year-old boy. As a birthday gift, you were given a camera and went to a beach for the day. You could take a picture of anything, but one thing captures your attention the most. What will you take a picture of?",
                                font=("Century Gothic", 14), bg="#ECE6E6", wraplength=self.screen_width * 0.5)
        label_prompt.grid(row=1, column=0, columnspan=2, pady=20)

        # Display Image (Resized)
        self.main_image = self.update_image()

        # Choice Buttons
        self.button_answer_1 = tk.Button(self, text="The Ocean", font=("Cooper", 20), command=self.memory_1, bg="#EEEEEE", width=15, height=2)
        self.button_answer_1.grid(row=3, column=0, padx=20, pady=50, sticky="e")

        self.button_answer_2 = tk.Button(self, text="A Sandcastle", font=("Cooper", 20), command=self.memory_2, bg="#EEEEEE", width=15, height=2)
        self.button_answer_2.grid(row=3, column=1, padx=20, pady=50, sticky="w")

    def update_image(self):
        # Resize image while maintaining aspect ratio
        new_size = (self.screen_width // 4, self.screen_height // 4)
        resized_image = self.controller.main_image.resize(new_size, Image.Resampling.LANCZOS)

        self.photo = ImageTk.PhotoImage(resized_image)  # Convert to Tkinter format
        self.image_label = tk.Label(self, image=self.photo, bg="#ECE6E6")
        self.image_label.grid(row=2, column=0, columnspan=2, pady=20)  # Center the image

        return self.photo

    def memory_1(self):
        self.controller.remember_choice(0, [self.button_answer_1.cget("text"), "blue"])
        print(self.controller.choices)
        self.controller.display(story_screen_2)

    def memory_2(self):
        self.controller.remember_choice(0, [self.button_answer_2.cget("text"), "yellow"])
        print(self.controller.choices)
        self.controller.display(story_screen_2)

class story_screen_2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(bg="#ECE6E6")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()


        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)  # Configure second column for side-by-side buttons

        label = tk.Label(self, text="Story", font=("Castellar", 40), anchor="center", bg="#ECE6E6")
        label.grid(row=0, column=0, columnspan=2, sticky="n", pady=20)  # Span across both columns

        label_prompt = tk.Label(
            self, 
            text="After that day at the beach, you began photographing more things, particularly birds. you even won 3rd place and got a trophy when you entered one of your photos into a competition! Even though you were 12, you knew this was what you wanted to do with your life! Now you just needed to photograph one thing to remember this feeling, what should you take a photo of?", 
            font=("Century Gothic", 14), 
            anchor="center", 
            bg="#ECE6E6", 
            wraplength=self.screen_width * 0.5
        )
        label_prompt.grid(row=1, column=0, columnspan=2, sticky="n", pady=20)  # Span across both columns

        # Display Image (Resized)
        self.update_image()
    
        # Buttons for choices
        self.button_answer_1 = tk.Button(self, text="Your trophy", font=("Cooper", 20), command=self.memory_1, bg="#EEEEEE", width=15, height=2)
        self.button_answer_1.grid(row=3, column=0, padx=20, pady=50, sticky="e")

        self.button_answer_2 = tk.Button(self, text="Yourself smiling", font=("Cooper", 20), command=self.memory_2, bg="#EEEEEE", width=15, height=2)
        self.button_answer_2.grid(row=3, column=1, padx=20, pady=50, sticky="w")
    def update_image(self):
        # Resize image while maintaining aspect ratio
        new_size = (self.screen_width // 4, self.screen_height // 4)
        resized_image = self.controller.main_image.resize(new_size, Image.Resampling.LANCZOS)

        self.photo = ImageTk.PhotoImage(resized_image)  # Convert to Tkinter format
        self.image_label = tk.Label(self, image=self.photo, bg="#ECE6E6")
        self.image_label.grid(row=2, column=0, columnspan=2, pady=20)  # Center the image

    def memory_1(self):
        self.controller.remember_choice(1, [self.button_answer_1.cget("text"), "sepia"])
        print(self.controller.choices)
        print(self.controller.choices)
        self.controller.display(story_screen_3)
    def memory_2(self):
        self.controller.remember_choice(1, [self.button_answer_2.cget("text"), "gray"])
        print(self.controller.choices)
        self.controller.display(story_screen_3)

class story_screen_3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(bg="#ECE6E6")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.current_image = self.controller.main_image

        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)  # Configure second column for side-by-side buttons

        label = tk.Label(self, text="Story", font=("Castellar", 40), anchor="center", bg="#ECE6E6")
        label.grid(row=0, column=0, columnspan=2, sticky="n", pady=20)  # Span across both columns

        label_prompt = tk.Label(
            self, 
            text="As a 16 year old, you began to branch out and hang out with more people, but after a fall you woke up and realized that you couldn't remember what had happened earlier in your life. Now, with your memorys fading forever, you need to choose how you want to remember your life thus far. What will you do? YOu could lose friends only living in the past, or you you could lose you past all together.", 
            font=("Century Gothic", 14), 
            anchor="center", 
            bg="#ECE6E6", 
            wraplength=self.screen_width * 0.5
        )
        label_prompt.grid(row=1, column=0, columnspan=2, sticky="n", pady=20)  # Span across both columns
        
        self.update_image()
        
        # Buttons for choices
        self.button_answer_1 = tk.Button(self, text="Remeber", font=("Cooper", 20),command=self.memory_1, bg="#EEEEEE", width=15, height=2)
        self.button_answer_1.grid(row=3, column=0, padx=20, pady=50, sticky="e")
        
        self.button_answer_2 = tk.Button(self, text="Forget", font=("Cooper", 20),command=self.memory_2, bg="#EEEEEE", width=15, height=2)
        self.button_answer_2.grid(row=3, column=1, padx=20, pady=50, sticky="w")
    def update_image(self):
        # Resize image while maintaining aspect ratio
        new_size = (self.screen_width // 4, self.screen_height // 4)
        resized_image = self.controller.main_image.resize(new_size, Image.Resampling.LANCZOS)

        self.photo = ImageTk.PhotoImage(resized_image)  # Convert to Tkinter format
        self.image_label = tk.Label(self, image=self.photo, bg="#ECE6E6")
        self.image_label.grid(row=2, column=0, columnspan=2, pady=20)  # Center the image
    def memory_1(self):
        self.controller.remember_choice(2, [self.button_answer_1.cget("text"), "dither"])
        print(self.controller.choices)
        self.controller.display(report_screen)
    def memory_2(self):
        self.controller.remember_choice(2, [self.button_answer_2.cget("text"), "blur"])
        print(self.controller.choices)
        self.controller.display(report_screen)

class report_screen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#ECE6E6")

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # Title, image, choice_1, choice_2, choice_3, exit button
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = tk.Label(self, text="Story", font=("Castellar", 40), anchor="center", bg="#ECE6E6")
        label.grid(row=0, column=0, sticky="n", pady=20)

        label_prompt = tk.Label(
            self, 
            text="Here is how your choices affected your story.", 
            font=("Century Gothic", 14), 
            anchor="center", 
            bg="#ECE6E6", 
            wraplength=self.screen_width * 0.5
        )
        label_prompt.grid(row=1, column=0, sticky="n", pady=20)

        self.update_image()
        self.update_choices()

        print(self.controller.choices)
        self.choice1 = label_prompt = tk.Label(self, text=f"{self.controller.choices[0][0]} Caused the image to be filtered with the {self.controller.choices[0][1]} filter", font=("Century Gothic", 14), anchor="center", bg="#ECE6E6", wraplength=self.screen_width * 0.5)
        self.choice1.grid(row=3, column=0, sticky="n", pady=20)
        
        self.choice2 = label_prompt = tk.Label(self, text=f"{self.controller.choices[1][0]} Caused the image to be filtered with the {self.controller.choices[1][1]} filter", font=("Century Gothic", 14), anchor="center", bg="#ECE6E6", wraplength=self.screen_width * 0.5)
        self.choice2.grid(row=4, column=0, sticky="n", pady=20)
        
        self.choice3 = label_prompt = tk.Label(self, text=f"{self.controller.choices[2][0]} Caused the image to be filtered with the {self.controller.choices[2][1]} filter", font=("Century Gothic", 14), anchor="center", bg="#ECE6E6", wraplength=self.screen_width * 0.5)
        self.choice3.grid(row=5, column=0, sticky="n", pady=20)
        
        self.return_button = tk.Button(self, text="Return", font=("Cooper", 20), command=self.return_main, bg="#EEEEEE", width=15, height=2,anchor="center")
        self.return_button.grid(row=6, column=0, padx=20, pady=50, sticky="w",)
        print("i")

    def return_main(self):
        self.controller.display(main_screen)
    def update_image(self):
        # Resize image while maintaining aspect ratio
        new_size = (self.screen_width // 4, self.screen_height // 4)
        resized_image = self.controller.main_image.resize(new_size, Image.Resampling.LANCZOS)

        self.photo = ImageTk.PhotoImage(resized_image)  # Convert to Tkinter format
        self.image_label = tk.Label(self, image=self.photo, bg="#ECE6E6")
        self.image_label.grid(row=2, column=0, columnspan=2, pady=20)  # Center the image

        self.choices = self.controller.choices

        self.choice1 = label_prompt = tk.Label(self, text=f"Your first choice caused the image to be filtered with the {self.controller.choices[0][1]} filter", font=("Century Gothic", 14), anchor="center", bg="#ECE6E6", wraplength=self.screen_width * 0.5)
        self.choice1.grid(row=3, column=0, sticky="n", pady=20)
        
        self.choice2 = label_prompt = tk.Label(self, text=f"Your second choice caused the image to be filtered with the {self.controller.choices[1][1]} filter", font=("Century Gothic", 14), anchor="center", bg="#ECE6E6", wraplength=self.screen_width * 0.5)
        self.choice2.grid(row=4, column=0, sticky="n", pady=20)
        
        self.choice3 = label_prompt = tk.Label(self, text=f"Your thrid choice caused the image to be filtered with the {self.controller.choices[2][1]} filter", font=("Century Gothic", 14), anchor="center", bg="#ECE6E6", wraplength=self.screen_width * 0.5)
        self.choice3.grid(row=5, column=0, sticky="n", pady=20)
    def update_choices(self):
        self.choices = self.controller.choices





if __name__ == "__main__":
    app = App()
    app.mainloop()
import tkinter as tk

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

        self.attributes("-fullscreen", True)
        self.frame_container = tk.Frame(self)
        self.frame_container.pack(fill="both", expand=True)


        self.frame_container.grid_rowconfigure(0, weight=1)
        self.frame_container.grid_columnconfigure(0, weight=1)

        self.used_frames = {}

        for FRAME in (main_screen, help_screen):
            frame = FRAME(parent=self.frame_container, controller=self)
            self.used_frames[FRAME] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.display(main_screen)
    
    def display(self, FRAME):

        frame = self.used_frames[FRAME]
        frame.tkraise()

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

        story_button = tk.Button(self, text="STORY", font=("Cooper", 43), bg="#EEEEEE", width=button_width, height=button_height)
        story_button.grid(row=1, column=0, sticky="n", pady=50)
        
        help_button = tk.Button(self, text="HELP", font=("Cooper", 43), bg="#EEEEEE", width=button_width, height=button_height)
        help_button.grid(row=2, column=0, sticky="n", pady=50)

        quit_button = tk.Button(self, text="QUIT", font=("Cooper", 43), bg="#EEEEEE", width=button_width, height=button_height)
        quit_button.grid(row=3, column=0, sticky="n", pady=50)


    
class help_screen(tk.Frame):
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

        story_button = tk.Button(self, text="STORY", font=("Cooper", 43), bg="#EEEEEE", width=button_width, height=button_height)
        story_button.grid(row=1, column=0, sticky="n", pady=50)
        
        help_button = tk.Button(self, text="HELP", font=("Cooper", 43), bg="#EEEEEE", width=button_width, height=button_height)
        help_button.grid(row=2, column=0, sticky="n", pady=50)

        quit_button = tk.Button(self, text="QUIT", font=("Cooper", 43), bg="#EEEEEE", width=button_width, height=button_height)
        quit_button.grid(row=3, column=0, sticky="n", pady=50)




#length_for_wrap = screen_width *.5 // 1

#current_prompt = "You are a newly 8 year old boy. It is your birthday, and as a present, you are given a camera by your parents. You are going to the beach to celebrate and you decide to bring the camera into what will become your lifelong passion. These are the some of the most important moments in your life. When you arrive at the beach, you see two areas you could photograph. Which one do you want to take a photo of?"

#prompt = tk.Label(master=window, text=current_prompt, wraplength=length_for_wrap)
#prompt.place(relx=.5, rely=.1, anchor="center")

if __name__ == "__main__":
    app = App()
    app.mainloop()

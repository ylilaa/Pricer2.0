import tkinter as tk
from tkinter import *
from multiprocessing import Process

import uvicorn


# External libraries
from tksheet import *
import customtkinter
# Command functions
from utils import *

# Pages
from pages.price_fundClass import Price_fund
from pages.price_titleClass import Price_title
from pages.price_listClass import Price_list



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Setting up Theme and Title
        self.title("Pricer Obligations SG")
        self.geometry("1400x600")
        customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

        # Creating a container
        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # List of pages
        self.frames = {}
        self.Price_fund = Price_fund
        self.Price_title = Price_title
        self.Price_list = Price_list

        # Defining frames and packing them, we show all frames stacked and raise one when needed
        for F in {Price_fund, Price_title, Price_list}:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Price_fund)

    def show_frame(self, cont):
        frame = self.frames[cont]
        menubar = frame.create_menubar(self)
        self.configure(menu=menubar)
        frame.tkraise()  # This line will put the frame on front




def loop2():
    uvicorn.run("server.main:app", host="127.0.0.1", port=8000, log_level="info")

if __name__ == "__main__":
    app = App()
    Process(target=loop2).start()
    print(colored('FastAPI server started','green'))
    Process(target=app.mainloop()).start()
    # app.mainloop()
    # uvicorn.run("server.main:app", host="127.0.0.1", port=8000, log_level="info")
    

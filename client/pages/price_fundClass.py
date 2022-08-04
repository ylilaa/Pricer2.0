import tkinter as tk
from tkinter import ttk
import customtkinter
from utils import *



# Forms inherited from pydantic 
from models.fundModel import fundInputForm

# ----------------------------------------  CONTAINER ------------------------------------------------------------------------

class Price_fund(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        # ============ create two frames ============
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                width=180,
                                                corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)


        # ============ LEFT FRAME ============

        # configure grid layout (1x11)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)

        # Title left grid
        self.leftTitle = customtkinter.CTkLabel(master=self.frame_left,
                                            text="Calcul VL",
                                            text_font=("Roboto Medium", -16))  # font name and size in px
        self.leftTitle.grid(row=1, column=0, pady=10, padx=10)

        # ========= Begin italian spaghetti code mama mia! must clean up later===========
        self.InputFundForm = fundInputForm()
        self.InputFundForm.name = initial_fund_display()
        
        def store_fund_input():
            self.InputFundForm.name = self.optionFonds.get()
            self.InputFundForm.AN = self.entryAN.get()
            self.InputFundForm.SR = self.entrySR.get()
            self.InputFundForm.PEncours = self.entryPEncours.get()
            self.InputFundForm.CEncours = self.entryCEncours.get()
            self.InputFundForm.Agios = self.entryAgios.get()
            self.InputFundForm.FdG = self.entryFdG.get()
            self.InputFundForm.Banque = self.entryBanque.get()
            self.InputFundForm.Levier = self.entryLevier.get()
            self.InputFundForm.RREPO = self.entryRREPO.get()
            self.InputFundForm.BDC = self.entryBDC.get()
            print(colored('Fund parameters registered Successfully','green'))

        self.dfTbl = get_fund_by_name(self.InputFundForm.name)
        
        
        def load_table():
            clear_data()
            self.table['column'] = list(self.dfTbl.columns)
            self.table['show'] = "headings"
            for column in self.table["columns"]:
                self.table.heading(column, text=column)
            
            df_rows = self.dfTbl.to_numpy().tolist()
            for row in df_rows:
                self.table.insert('','end',values=row)


        
        def tableChange(choice):
            if choice != self.InputFundForm.name:
                self.dfTbl = get_fund_by_name(choice)
                load_table()
        
        
        self.table = ttk.Treeview(self.frame_right)
        self.table.place(relheight=1, relwidth=1)
        def clear_data():
            self.table.delete(*self.table.get_children())
        
        load_table()
        tablescrolly = tk.Scrollbar(self.frame_right, orient="vertical", command=self.table.yview)
        tablescrollx = tk.Scrollbar(self.frame_right, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=tablescrollx.set,yscrollcommand=tablescrolly.set)
        tablescrollx.pack(side="bottom", fill="x")
        tablescrolly.pack(side="right", fill="y")

        
        self.optionFonds = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                    values=get_funds_array(), command=tableChange)
        self.optionFonds.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        
        # Champs à remplir modèle excel 
        
        self.entryAN = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="AN après S/R")
        self.entryAN.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.entrySR = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="S/R")
        self.entrySR.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        self.entryPEncours = customtkinter.CTkEntry(master=self.frame_left,
                                                placeholder_text="Pdts Encours")
        self.entryPEncours.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        self.entryCEncours = customtkinter.CTkEntry(master=self.frame_left,
                                                placeholder_text="Chgs Encours")
        self.entryCEncours.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.entryAgios = customtkinter.CTkEntry(master=self.frame_left,
                                                placeholder_text="Agios")
        self.entryAgios.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.entryFdG = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="FdG")
        self.entryFdG.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        self.entryBanque = customtkinter.CTkEntry(master=self.frame_left,
                                                placeholder_text="Banque")
        self.entryBanque.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        self.entryLevier = customtkinter.CTkEntry(master=self.frame_left,
                                                placeholder_text="Levier")
        self.entryLevier.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        self.entryRREPO = customtkinter.CTkEntry(master=self.frame_left,
                                                placeholder_text="RREPO")
        self.entryRREPO.grid(row=11, column=0, pady=10, padx=20, sticky="w")

        self.entryBDC = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="BDC")
        self.entryBDC.grid(row=12, column=0, pady=10, padx=20, sticky="w")

        self.buttonValidate = customtkinter.CTkButton(master=self.frame_left,
                                                    text="Valider",
                                                    command=store_fund_input)
        self.buttonValidate.grid(row=13, column=0, pady=10, padx=20, sticky="w")

    # ===========End spaghetti===================

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        # Menu
        
        actionmenu = Menu(menubar, tearoff=0, relief=RAISED)
        actionmenu.add_command(label="Pricer un Titre", command=lambda: parent.show_frame(parent.Price_title))
        actionmenu.add_command(label="Stress Test", command=lambda: parent.show_frame(parent.Price_list))
        actionmenu.add_separator()
        actionmenu.add_command(label="Exit", command=parent.quit)
        menubar.add_cascade(label="Actions", menu=actionmenu)

        querymenu = Menu(menubar, tearoff=0, relief=RAISED)
        querymenu.add_command(
            label="Actualiser les données depuis le fichier Manar", command=donothing)
        menubar.add_cascade(label="Requêtes", menu=querymenu)

        helpmenu = Menu(menubar, tearoff=0, relief=RAISED)
        helpmenu.add_command(label="Documentation", command=lambda: parent.show_frame(parent.docsClass))
        menubar.add_cascade(label="Aide", menu=helpmenu)
        return menubar

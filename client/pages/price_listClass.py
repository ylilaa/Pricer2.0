import tkinter as tk
from tkinter import filedialog
import customtkinter
from tkinter import ttk
from utils import *

#Forms inherited from pydantic
from models.listModel import TitleListInputForm

# ----------------------------------------  CONTAINER ------------------------------------------------------------------------

class Price_list(tk.Frame):
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
                                            text="Stress Test",
                                            text_font=("Roboto Medium", -16))  # font name and size in px
        self.leftTitle.grid(row=1, column=0, pady=10, padx=10)

        self.dfTbl = pd.DataFrame()
        self.titleListInputForm = TitleListInputForm()
        

        

        # Champs à remplir modèle excel
        self.check_var = tk.BooleanVar(master=self.frame_left)

        self.buttonImportList = customtkinter.CTkButton(master=self.frame_left,
                                                    text="Importer une liste de titres",
                                                    command=openFile)
        self.buttonImportList.grid(row=1, column=0, pady=10, padx=20, sticky="w")      
        
        self.entryDateValo = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="Date de valorisation")
        self.entryDateValo.grid(row=2, column=0, pady=10, padx=20, sticky="w") 
                

        def toggle_button():
            if self.check_var.get():
                self.buttonImportCurve.state=DISABLED 
            else:
                self.buttonImportCurve.state=NORMAL


        
        self.buttonImportCurve = customtkinter.CTkButton(master=self.frame_left,
                                                    text="Importer une courbe",
                                                    command=openFile)
        
        self.buttonImportCurve.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        self.checkCourbeBAM = customtkinter.CTkCheckBox(master=self.frame_left,
                                            text="Utiliser courbe BAM",
                                            command=toggle_button,
                                            variable=self.check_var, onvalue="on", offvalue="off")
        self.checkCourbeBAM.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        def load_table():
            clear_data()
            self.table['column'] = list(self.dfTbl.columns)
            self.table['show'] = "headings"
            for column in self.table["columns"]:
                self.table.heading(column, text=column)
            
            df_rows = self.dfTbl.to_numpy().tolist()
            for row in df_rows:
                self.table.insert('','end',values=row)
        
        
        def store_list_input():
            
            self.titleListInputForm.dateValo = self.entryDateValo.get()
            self.titleListInputForm.courbeBAM = self.checkCourbeBAM.get()
            self.dfTbl = stress_test_display(self.titleListInputForm)
            load_table()
            print(colored('Title parameters registered Successfully','green'))

        
        self.buttonValidate = customtkinter.CTkButton(master=self.frame_left,
                                                    text="Valider",
                                                    command=store_list_input)
        self.buttonValidate.grid(row=5, column=0, pady=10, padx=20, sticky="w")


        # ====================RIGHT FRAME ===========================
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


        
    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        # Menu
        
        actionmenu = Menu(menubar, tearoff=0, relief=RAISED)
        actionmenu.add_command(label="Pricer un Titre", command=lambda: parent.show_frame(parent.Price_title))
        actionmenu.add_command(label="Calcul VL", command=lambda: parent.show_frame(parent.Price_fund))
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

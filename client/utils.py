from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime



from models.titleModel import titleInputForm

import pandas as pd
import numpy as np
from termcolor import colored

from config import *


def donothing():
    messagebox.showinfo(title="walo", message=" w ta 9lwa walo")

def initial_fund_display():
    config = AppConfig()
    original_df = pd.read_excel(config.db_name)
    print(colored('Was here','red'))
    return original_df.iloc[0]['CODE_FONDS']

def get_fund_by_name(fund):
    config = AppConfig()
    original_df = pd.read_excel(config.db_name)
    df = original_df[original_df['CODE_FONDS'] == fund]
    print(colored('Fund retrieved from database Successfully','green'))
    return df

def get_title_by_code(titre):
    config = AppConfig()
    original_df = pd.read_excel(config.db_name)
    df = original_df[original_df['CODE_TITRE'] == titre]
    
    


def get_funds_array():
    config = AppConfig()
    original_df = pd.read_excel(config.db_name).astype(str)
    array = original_df['CODE_FONDS'].unique()
    print(colored('List of Funds retrieved from database Successfully','green'))
    return array

def title_pricing_display (input):
    input = titleInputForm()
    print(input.code)
    df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=['code','Date coupon','Amortissement','Restant','Coupon'])
    return df


def stress_test_display (input):
    input = titleInputForm()
    print(input.code)
    df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=['code','prix','sensibilité','duration'])
    return df

def openFile():
    # takes file location and its type
    file_location = filedialog.askopenfilename(initialdir="",
                                          title="Dialog box",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    file = open(file_location,'r')
    print(file.read())
    file.close()







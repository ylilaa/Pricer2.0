from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from datetime import date, datetime
from urllib import response
import requests
import json
from bson import json_util
import time


from models.titleModel import titleInputForm

import pandas as pd
import numpy as np
from termcolor import colored

from config import *


def donothing():
    messagebox.showinfo(title="walo", message=" w ta 9lwa walo")

def initial_fund_display():
    config = AppConfig()
    original_df = pd.read_excel(config.db_titres)
    return original_df.iloc[0]['CODE_FONDS']

def get_fund_by_name(fund):
    config = AppConfig()
    original_df = pd.read_excel(config.db_titres)
    df = original_df[original_df['CODE_FONDS'] == fund]
    print(colored('Fund retrieved from database Successfully','green'))
    return df

def get_title_by_code(titre):
    config = AppConfig()
    original_df = pd.read_excel(config.db_titres)
    df = original_df[original_df['CODE_TITRE'] == titre]
    return df
    


def get_funds_array():
    config = AppConfig()
    original_df = pd.read_excel(config.db_titres).astype(str)
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

def cloneManarTitres():
    config = AppConfig()
    original_df = pd.read_excel(config.db_titres)
    df = pd.DataFrame()
    
    df["code"] = original_df["CODE_TITRE"]
    df["description"] = original_df["DESCIRPTION"]
    df["nominal"] = original_df["NOMINAL"]    
    df['dateEmission'] = original_df['DATE_EMISSION'].dt.strftime('%Y-%m-%d')
    df["dateJouissance"] = original_df['DATE_JOUISSANCE'].dt.strftime('%Y-%m-%d')
    df["dateEcheance"] = original_df['DATE_ECHEANCE'].dt.strftime('%Y-%m-%d')
    df["tauxFacial"] = original_df["TAUX_FACIAL"]
    df["spread"] = original_df["SPREAD"]
    df["amort"] = original_df["AMORT"]
    df["lastPriceManar"] = original_df["COURS"]
    df["spread"]=df["spread"].fillna(0)
    df.dropna()
    print(df.head)
    
    payload = df.to_dict(orient='records')
    for i in df.index:
        code = df.iloc[i]["code"]
        print(code)
        # print(payload[i])
        res = requests.post(url=config.api_url+"titres/", json=payload[i])
        # print(i)
        #print(res.text)

def cloneManarEcheanciers():
    config = AppConfig()
    original_df = pd.read_excel(config.db_echeanciers)
    df = pd.DataFrame()
    
    df["titre_code"] = original_df["TITRE"]
    df["capitalAmorti"] = original_df["CAPITAL_AMORTIS"]
    df["capitalRestant"] = original_df["CAPITAL_RESTANT"]  
    df['dateTombee'] = pd.to_datetime(original_df['DATE_TOMBEE'])
    df['dateTombee'] = df['dateTombee'].dt.strftime('%Y-%m-%d')
    df["couponBrut"] = original_df["COUPON_BRUT"]
    df.dropna()

    pload = df[["capitalAmorti","capitalRestant",'dateTombee',"couponBrut","titre_code"]].copy()
    
    payload = pload.to_dict(orient='records')
    print(payload[0])

    for i in df.index:
        code = df.iloc[i]["titre_code"]
        # print(code)
        # print(payload[i])
        res = requests.post(url=config.api_url+"titres/"+str(code)+"/echeancier", json=payload[i])
        # print(i)
        # print(res.text)
    


import math as m
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

def isLeapYear(year):  
  # Checking if the given year is leap year
  if((year % 400 == 0) or  
     (year % 100 != 0) and  
     (year % 4 == 0)):   
    return 1  
  # Else it is not a leap year  
  else:  
    return 0  

def setBase(year):
    if isLeapYear(year):
        return 366
    else:
        return 365

class title:
    def __init__(self,dateJouissance,dateEcheance, dateEmission,periodicite, nominal, facial, spread,YTM):
        # codeTitre : int
        # dateEmission : datetime.date =None
        self.dateJouissance = dateJouissance
        self.dateEcheance = dateEcheance
        self.dateEmission = dateEmission 
        self.periodicite = periodicite
        self.nominal = nominal
        self.facial = facial
        self.spread = spread
        self.YTM = YTM
        # nominal : float
        # facial : float
        # spread : float
        # periodicite : str
        # dateValo : datetime.date=None
        # dateCourbe : datetime.date=None

    @classmethod
    def infine_fix_echeancier(self, dateJouissance, dateEcheance, dateEmission,periodicite, nominal, facial, spread, YTM):
        df = pd.DataFrame(columns=['Date','Amorti','Restant','Coupon','Flux'])
        i = 0
        # Dates column
        date = dateJouissance
        while date <= dateEcheance:
            df.loc[i,'Date'] = date
            if periodicite == 'AN':
                date = date + relativedelta(years=1)
            if periodicite == 'Mon':
                date = date + relativedelta(months=1)
            if periodicite == 'Q':
                date = date + relativedelta(months=3)
            if periodicite == 'SEM':
                date = date + relativedelta(months=6)
            i = i+1
        
        # Amorti column
        df.loc[:,'Amorti'] = 0
        df.loc[df.index[-1],'Amorti'] = nominal
        
        # Restant column
        i = 0
        for i in range(0,df.index[-1]):
             df.loc[i,'Restant'] = nominal - df.loc[i,'Amorti']
        
        df.loc[df.index[-1],'Restant'] = 0

        #Coupon column
        i = 0
        df.loc[i,'Coupon'] = int(df.loc[i,'Restant']*(facial+spread)*(df.loc[i,'Date']-dateEmission).days/setBase((df.loc[i,'Date']).year))/100
        max  = df.index[-1] + 1
        for i in range(1,max):
            df.loc[i,'Coupon'] = int(nominal*(facial+spread)*(df.loc[i,'Date']-df.loc[i-1,'Date']).days/setBase((df.loc[i,'Date']).year))/100
            
        
        
        #flux column
        for i in range(0,max):
            df.loc[i,'Flux'] = df.loc[i,'Amorti'] + df.loc[i,'Coupon']
        
        
        print(df)

titre = title(datetime.date(2020,6,18),datetime.date(2029,6,18),datetime.date(2019,2,4),'AN',100000,3.35,0)

titre.infine_fix_echeancier(datetime.date(2020,6,18),datetime.date(2029,6,18),datetime.date(2019,2,4),'AN',100000,3.35,0)


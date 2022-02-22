#Importing essentail libraries
from ctypes.wintypes import tagRECT
import os
import pandas as pd

#Displays the  data from the Excel file
data=pd.read_csv("C:\\Users\\Shubham Ambekar\\OneDrive - Liverpool John Moores University\\Desktop\\GitHub\\CW1- Computer Science Workshop\\WHO-COVID-19-global-data.csv")
print(data)




    
    
#def inputFromFile():
deathToll("india")  
    

def deathToll(targetcountry):
    deathToll=0
    country=data["Cumulative_deaths"]
    if(tragetCountry==country):
        deathToll+=tragetCountry
    else:
        deathToll+=0
    print(deathToll)
        
        
#Importing essentail libraries
from ctypes.wintypes import tagRECT
import os
import pandas as pd

#Displays the  data from the Excel file
data=pd.read_csv("C:\\Users\\Shubham Ambekar\\OneDrive - Liverpool John Moores University\\Desktop\\GitHub\\CW1- Computer Science Workshop\\WHO-COVID-19-global-data.csv")
print(data)

#Menu
print("--------------Menu--------------")
print("1.Current trends")
print("2.Find Information about your country: ")
print("3.Display all the countries Covid-19 Data ")
print("4.Compare two countries")
    
print("Please enter  the  option number :")
choosenOption=input()
option(choosenOption)

def option(chooseOption):
    
    
    


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
        
        
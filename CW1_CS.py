#Importing essentail libraries
from ctypes.wintypes import tagRECT
import os
import pandas as pd

#Displays the  data from the Excel file
data=pd.read_csv("WHO-COVID-19-global-data.csv")
print(data)

#Menu
print("--------------Menu--------------")
print("1.Current trends")
print("2.Find Information about your country: ")
print("3.Display all the countries Covid-19 Data ")
print("4.Compare two countries")
    
print("Please enter  the  option number :")
choosenOption=int(input())
option(choosenOption)

def option(chooseOption):
    if chooseOption==1:
        currentTrends()
    elif chooseOption==2:
        infoCovidCountry()
    elif chooseOption==3:
        displayAllCovidData()
    elif chooseOption==4:
        CompareCountryCovid19()
    else:
        print("Please choose the numbers from the menu.")
        
        
def currentTrends():
    
def infoCovidCountry():

def  displayAllCovidData():

def  CompareCountryCovid19():



     
    
    


#def inputFromFile():
#deathToll("india")  
    
#def deathToll(targetcountry):
#    deathToll=0
#    country=data["Cumulative_deaths"]
#    if(tragetCountry==country):
#        deathToll+=tragetCountry
#    else:
#        deathToll+=0
#    print(deathToll)
        

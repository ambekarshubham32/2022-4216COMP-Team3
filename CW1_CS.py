#Importing essentail libraries
from ctypes.wintypes import tagRECT
import os
import pandas as pd




     
    
    


#def inputFromFile():
#deathToll()  
    
#def deathToll(targetcountry):
#    deathToll=0
#    country=data["Cumulative_deaths"]
#    if(tragetCountry==country):
#        deathToll+=tragetCountry
#    else:
#        deathToll+=0
#    print(deathToll)
        





#Displays the  data from the Excel file
data=pd.read_csv("WHO-COVID-19-global-data.csv")
print(data)

print("Please enter the country's name below: ")
country=input()







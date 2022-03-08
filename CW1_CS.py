#Importing essentail libraries
from ctypes.wintypes import tagRECT
import os
import pandas as pd
#Displays the  data from the Excel file
##data=pd.read_csv("WHO-COVID-19-global-data.csv")
##print(data)

print("Menue")
print("1.    Top 5 vaccines Harry \n 2.    Finding data by country Shubham\n3.    What time of year had the most deaths/vaccines? Lydia\n 4.    Type of vaccines used Matty\n5.    Popular vaccine per country Vince\n 6.    Comparing total deaths and vaccines of specific countries Charlie")





print("Please enter the country's name below: ")
country=input()
#selectCountry()


print("What type of  Covid 19 related information do you want to know.")
print("1. Confimed Cases\n 2.Death\n 3. Vaccination")
coronavirusInfoType=input()
#CoronavirusParameters()

print("Different types of charts to presentation data . ")
print("1.Line graph \n 2. Bar chart\n 3. Pie chart \n4.Scatter chat \n5.Cumulative  graph ")
chartTypes=input()
#chart()
    
    
def chart():

#def selectCountry():
    
#def CoronavirusParameters():







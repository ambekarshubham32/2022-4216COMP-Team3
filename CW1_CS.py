# essentail libraries
from ctypes.wintypes import tagRECT
import os
from tokenize import String
from types import TracebackType
from matplotlib import dates
from matplotlib.axis import YAxis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime
from sympy import true
#Displays the  data from the Excel files
casesAndDeathData=pd.read_csv("WHO-COVID-19-global-data.csv")
vaccineData=pd.read_csv("vaccination-data.csv")

    
#Harry
#def topFiveVaccine(): 
#Lydia    
#def mostDeathOrVaccine(): 
#Matty
#def vaccineType():
#Vince 
#def popularVaccinePerCountry():
#Charlie
#def comparisonTotalDeathOrVaccineOnSpecificCountries():

#Shubham

    
        
def loadData(chartTypes,country,coronavirusInfoType,yesOrNoCumulativeGraph):
    
    try:
        with open('WHO-COVID-19-global-data.csv', 'r') as f:
            csv_reader = csv.reader(f)
            # skip the header
            next(csv_reader)
            
            #Two arrays stores the data for x and y axis number
            date=[]
            caseOrDeath=[]
            
            # retrieve specific data fromthe file and stores it in an array above 

            for rowData in csv_reader:
                if rowData[2]==country:
                    date.append(str(rowData[0]))
                    if (coronavirusInfoType==1 and yesOrNoCumulativeGraph==False):
                        case=int(rowData[4])
                        caseOrDeath.append(case)
                        yAxisLabel="Cases"

                    elif (coronavirusInfoType==2 and yesOrNoCumulativeGraph==False):
                        death=int(rowData[6])
                        caseOrDeath.append(death)
                        yAxisLabel="Deaths"
                    elif (coronavirusInfoType==1 and yesOrNoCumulativeGraph==True):
                        case=int(rowData[5])
                        caseOrDeath.append(case)
                        yAxisLabel="Cases"

                    elif (coronavirusInfoType==2 and yesOrNoCumulativeGraph==True):
                        death=int(rowData[7])
                        caseOrDeath.append(death)
                        yAxisLabel="Deaths"
                    
            
            
            
    except:
        print("Something went wrong retreiving data.")
    else:    
        displayVisualisation(chartTypes,country,date,caseOrDeath,yAxisLabel,yesOrNoCumulativeGraph)
            
    
def displayVisualisation(chartTypes,country,date,caseOrDeath,yAxisLabel,yesOrNoCumulativeGraph):
  #Display all the essentail features of the graph
    plt.xticks(rotation=90)
    plt.grid()
    plt.title("Number of "+yAxisLabel.lower()+" in  "+country)
    plt.xlabel('Date -(dd/MM/yyyy)')
    plt.ylabel(' '+yAxisLabel)  
  
    plt.legend(['Cases', 'Deaths'])

    if  chartTypes==1:
        plt.plot(date[0::30],caseOrDeath[0::30], marker = 'o', color='green')
    elif chartTypes==2:
        plt.bar(date[0::30],caseOrDeath[0::30], color='blue')
    elif chartTypes==3:       
        plt.scatter(date[0::30],caseOrDeath[0::30], marker = 'x', color='blue')
    elif chartTypes==4 and  yesOrNoCumulativeGraph==True:
        plt.plot(date[0::30],caseOrDeath[0::30], marker = 'o', color='black')
    else:
        print("This graph or chart is not available.")
    
    plt.show()



#User Input's country information and the graphor chart type
def countryDataSelection():
   
    try:
        print("Please enter the country's name below(first letter uppercase): ")
        country=input()
        #print("There is not data about this "+country+".Please try again")
 
        
        print("What type of  Covid 19 related information do you want to know.")
        print("1.Confimed Cases\n2.Death\n Please enter the number   below:")
        coronavirusInfoType=int(input())
    
            
    except:
        print("Invalid input.Please  enter a number from the given list")  
        countryDataSelection()
    else:
        
            print("Different types of charts to presentation data.")
            print("1.Line graph\n2.Bar chart\n3.Scatter chart\n4.Cumulative graph\n Please enter the number below:")
            chartTypes=int(input())
            if chartTypes==4 :
                yesOrNoCumulativeGraph=True
            else:
                yesOrNoCumulativeGraph=False
        
            loadData(chartTypes,country,coronavirusInfoType,yesOrNoCumulativeGraph)
  

    
    
      
    
        
#Menu
while(True):
    #Displays the menu
    print("Menu")
    print("1 - Top 5 vaccines\n2 - Find data by country\n3 - What time of year had the\
        most deaths vaccines?\n4 - Type of vaccines used\n5 - Popular vaccine per\
        country\n6 - Comparing total deaths and vaccines of specific countries\n7\
        - Quit\nPlease enter the number   below:")

    #user enter's the choosen option
    
    menuOption=input()

    #Runs a function depending on the user's input
    if menuOption=="1":
        topFiveVaccine()
    elif menuOption=="2":
        countryDataSelection()
    elif menuOption=="3":
        mostDeathOrVaccine()
    elif menuOption=="4":
        vaccineType()
    elif menuOption=="5":
        popularVaccinePerCountry()
        
    elif menuOption=="6":
        comparisonTotalDeathOrVaccineOnSpecificCountries()
    elif menuOption=="7":
        break 
    else:
        print("Invalid Input.Please enter a number from the menu.")

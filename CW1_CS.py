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

def barGraph(chartTypes,country,coronavirusInfoType):
    #calls ths function
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
                if coronavirusInfoType==1:
                    case=int(rowData[4])
                    caseOrDeath.append(case)
                    yAxis="Cases"

                elif coronavirusInfoType==2:
                    death=int(rowData[6])
                    caseOrDeath.append(death)
                    yAxis="Death"

               
        #Test Code below(check if data is added in the array)
        print(date)
        print(caseOrDeath)
   
    
    DisplayVisualisation(chartTypes,country,yAxis,coronavirusInfoType,date,caseOrDeath)

        
  

       
    


def scatterChart(chartTypes,country,coronavirusInfoType):
    
    #calls ths function
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
                if coronavirusInfoType==1:
                    case=int(rowData[4])
                    caseOrDeath.append(case)
                    yAxis="Cases"

                elif coronavirusInfoType==2:
                    death=int(rowData[6])
                    caseOrDeath.append(death)
                    yAxis="Death"

              
        #Test Code below(check if data is added in the array)
        print(date)
        print(caseOrDeath)
    
        DisplayVisualisation(chartTypes,country,yAxis,coronavirusInfoType,date,caseOrDeath)
        
    
    
      

            
def lineGraph(chartTypes,country,coronavirusInfoType):

    #calls ths function
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
                if coronavirusInfoType==1:
                    case=int(rowData[4])
                    caseOrDeath.append(case)
                    yAxis="Cases"

                elif coronavirusInfoType==2:
                    death=int(rowData[6])
                    caseOrDeath.append(death)
                    yAxis="Death"

                  
        #Test Code below(check if data is added in the array)    
        print(date)
        print(caseOrDeath)
    
  



    DisplayVisualisation(chartTypes,country,yAxis,coronavirusInfoType,date,caseOrDeath)
   
    
    
   
    
        
    
    
       
   
    





def cumulativeGraph(chartTypes,country,coronavirusInfoType):
    
    with open('WHO-COVID-19-global-data.csv', 'r') as f:
        csv_reader = csv.reader(f)
        # skip the header
        next(csv_reader)
        
        #Two arrays stores the data for x and y axis
        date=[]
        caseOrDeath=[]
        
        # retrieve specific data fromthe file and stores it in an array above 
        for rowData in csv_reader:
            if rowData[2]==country:
                date.append(str(rowData[0]))
                if coronavirusInfoType==1:
                    case=int(rowData[5])
                    caseOrDeath.append(case)
                    yAxis="Cases"
                  

                elif coronavirusInfoType==2:
                    death=int(rowData[7])
                    caseOrDeath.append(death)
                    yAxis="Death"

             
        #Test Code below(check if data is added in the array)
        print(date)
        print(caseOrDeath)
        
    
    DisplayVisualisation(chartTypes,country,yAxis,coronavirusInfoType,date,caseOrDeath)


def allVisualiation(chartTypes,country,coronavirusInfoType):
    #calls ths function
    with open('WHO-COVID-19-global-data.csv', 'r') as f:
        csv_reader = csv.reader(f)
        # skip the header
        next(csv_reader)
        
        #Two arrays stores the data for x and y axis number
        date=[]
        caseOrDeath=[]
        cumulativeCaseOrDeath=[]
           
    
        
        # retrieve specific data fromthe file and stores it in an array above 
        for rowData in csv_reader:
            if rowData[2]==country:
                date.append(str(rowData[0]))
                if (coronavirusInfoType==1 and chartTypes==4):
                    case=int(rowData[5])
                    caseOrDeath.append(case)
                    yAxis="Cases"

                elif coronavirusInfoType==2 and chartTypes==4:
                    death=int(rowData[7])
                    caseOrDeath.append(death)
                    yAxis="Deaths"

                elif coronavirusInfoType==1:
                    case=int(rowData[4])
                    caseOrDeath.append(case)
                    yAxis="Cases"

                elif coronavirusInfoType==2:
                    death=int(rowData[6])
                    caseOrDeath.append(death)
                    yAxis="Deaths"
        #Test Code below(check if data is added in the array)
        print(date)
        print(caseOrDeath)
    
    fig, axs = plt.subplots(1,2,3,4)
    axs[0].set_title("Number of "+yAxis+"in  "+country)
    axs[1].set_title("Number of "+yAxis+"in  "+country)
    axs[2].set_title("Number of "+yAxis+"in  "+country)
    axs[3].set_title("Number of "+yAxis+"in  "+country)
    axs[0].plt(dates, caseOrDeath)
    axs[1].bar(dates, caseOrDeath)
    axs[2].scatter(dates,caseOrDeath)
    axs[3].plt(dates,caseOrDeath) 
    
    plt.show()
  
def DisplayVisualisation(chartType,country,yAxis,coronavirusInfoType,date,caseOrDeath):
    #Display all the essentail features of the graph
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.title("Number of "+yAxis+" in  "+country)
    plt.xlabel('Date -(dd/MM/yyyy)')
    plt.ylabel(' '+yAxis)  
  
    plt.legend(['Cases', 'Deaths'])

    if  chartType==1:
        plt.plot(date[0::30],caseOrDeath[0::30])

    elif chartType==2:
        plt.bar(date[0::30],caseOrDeath[0::30])

    elif chartType==3:
        plt.scatter(date[0::30],caseOrDeath[0::30])

    
    elif chartType==4:
        plt.plot(date[0::30],caseOrDeath[0::30])

    
    
    plt.show()
    


    
    




#User Input's country information and the graphor chart type
def countryDataSelection():
    
        print("Please enter the country's name below: ")
        country=input()
        print("What type of  Covid 19 related information do you want to know.")
        print("1.Confimed Cases\n2.Death")
        coronavirusInfoType=int(input())
        print("Different types of charts to presentation data . ")
        print("1.Line graph\n2.Bar chart\n3.Scatter chart\n4.Cumulative graph\
            \n5. All the graph and function in the list ")
        chartTypes=int(input())
        if coronavirusInfoType==1:
            chartOrGraph(chartTypes,country,coronavirusInfoType)    
        elif coronavirusInfoType==2:    
            chartOrGraph(chartTypes,country,coronavirusInfoType)    
            
        else:
            print("Invalid Input")
          



  
    
           
 #Finds the graph or chart functions and runs them
def chartOrGraph(chartTypes,country,coronavirusInfoType): 
    while True:        
        if chartTypes==1:
            lineGraph(chartTypes,country,coronavirusInfoType)
            break
        elif chartTypes==2:
            barGraph(chartTypes,country,coronavirusInfoType)
            break
        elif chartTypes==3:
            scatterChart(chartTypes,country,coronavirusInfoType)
            break
        elif chartTypes==4:
            cumulativeGraph(chartTypes,country,coronavirusInfoType)
            break
        
        elif chartTypes==5:
            allVisualiation(chartTypes,country,coronavirusInfoType)
            break
            
        
        else:
            print("Invalid graph choice")
                 

#Menu
while(True):
    #Displays the menu
    print("Menu")
    print("1 - Top 5 vaccines\n2 - Finding data by country\n3 - What time of year had\
        the most deaths vaccines?\n4. - Type of vaccines used\n5. - Popular vaccine per country\
        \n6. - Comparing total deaths and vaccines of specific countries\n7 - Quit")

    #user enter's the choosen option
    print("Please enter the number  here:")
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
        print("Invalid Input. Please enter a number from the menu.")

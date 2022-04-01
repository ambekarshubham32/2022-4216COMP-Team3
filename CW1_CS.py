#Importing essentail libraries
from ctypes.wintypes import tagRECT
import os
from tokenize import String
from types import TracebackType
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
   
    
    if coronavirusInfoType==1:
        plt.bar(date[0::90],caseOrDeath[0::90], color='green')
    elif coronavirusInfoType==2:
        plt.bar(date[0::90],caseOrDeath[0::90], color='green')




    #Display all the essentail features of the graph
    plt.grid(True)
    plt.title("Number of death in  "+country)
    plt.xlabel('Date-(dd/MM/yyyy)')
    plt.ylabel(' '+yAxis)  
  
    plt.legend(['Cases', 'Deaths'])
    

    
 
    plt.show()     
                
        
  

       
    


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
    
   
   
    if coronavirusInfoType==1:
        plt.scatter(date[0::90],caseOrDeath[0::90], color='green')
    elif coronavirusInfoType==2:
        plt.scatter(date[0::90],caseOrDeath[0::90], color='green')



    #Display all the essentail features of the graph
    plt.grid(True)
    plt.title("Number of death in  "+country)
    plt.xlabel('Date-(dd/MM/yyyy)')
    plt.ylabel(' '+yAxis)  
  
    plt.legend(['Cases', 'Deaths'])
    plt.show()     
    
    
    
      

            
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
                    #ax.set_title("Cumulative Cases", fontsize=14)

                elif coronavirusInfoType==2:
                    death=int(rowData[6])
                    caseOrDeath.append(death)
                    yAxis="Death"

                  
        #Test Code below(check if data is added in the array)    
        print(date)
        print(caseOrDeath)
    
    if coronavirusInfoType==1:
        plt.plot(date[0::90],caseOrDeath[0::90],'*g--')
    elif coronavirusInfoType==2:
        plt.plot(date[0::90],caseOrDeath[0::90],'rD--')



    #Display all the essentail features of the graph
    plt.grid(True)
    plt.title("Number of "+yAxis+" in  "+country)
    plt.xlabel('Date -(dd/MM/yyyy)')
    plt.ylabel(' '+yAxis)  
  
    plt.legend(['Cases', 'Deaths'])
    
    plt.show()     
    
    
   
    
        
    
    
       
   
    





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
    
    if coronavirusInfoType==1:
        plt.plot(date[0::90],caseOrDeath[0::90],'*g--')
    elif coronavirusInfoType==2:
        plt.plot(date[0::90],caseOrDeath[0::90],'rD--')



    #Display all the essentail features of the graph
    plt.grid(True)
    plt.title("Number of death in  "+country)
    plt.xlabel('Date -(dd/MM/yyyy)')
    plt.ylabel(' '+yAxis)  
  
    plt.legend(['Cases', 'Deaths'])
    

   
 
    plt.show()     
                    





#User Input's country information and the graphor chart type
def countryDataSelection():
    
        print("Please enter the country's name below: ")
        country=input()
        print("What type of  Covid 19 related information do you want to know.")
        print("1.Confimed Cases\n2.Death")
        coronavirusInfoType=int(input())
        print("Different types of charts to presentation data . ")
        print("1.Line graph\n2.Bar chart\n3.Scatter chart\n4.Cumulative  graph\n ")
        chartTypes=int(input())
        if coronavirusInfoType==1:
            chartOrGraph(chartTypes,country,coronavirusInfoType)    
        elif coronavirusInfoType==2:    
            chartOrGraph(chartTypes,country,coronavirusInfoType)    
            
        else:
            print("Invalid Input")
          



  
    
           
 #runs the graph or chart function 
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
        else:
            print("Invalid graph choice")
                 

#Menu
while(True):
    print("Menu")
    print("1 - Top 5 vaccines\n2 - Finding data by country\n3 - What time of year had the most deaths/vaccines?\
        n4. - Type of vaccines used\n5. - Popular vaccine per country\n6. - Comparing total deaths and vaccines of specific countries\n7 - Quit")

    print("Please enter the number  here:")
    menuOption=input()

    #Executes the option code of the function
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
    
        
    
   
    
 

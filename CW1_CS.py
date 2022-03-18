#Importing essentail libraries
from ctypes.wintypes import tagRECT
import os
from tokenize import String
import pandas as pd
import matplotlib.pyplot as plt
#Displays the  data from the Excel files
casesAndDeathData=pd.read_csv("WHO-COVID-19-global-data.csv")
vaccineData=pd.read_csv("vaccination-data.csv")
#Initailisation of variables:
menuSelection=0




print("Menu")
print("1.Top 5 vaccines Harry \n2.Finding data by country Shubham\n3.What time of year had the most deaths/vaccines? Lydia\n4.Type of vaccines used Matty\n5.opular vaccine per country Vince\n6.omparing total deaths and vaccines of specific countries Charlie")

menuOption=int(input("Please enter the number   here:"))
menuSelection(menuOption)



def  menuSelection(menuOption):
    if menuOption==1:
        topFiveVaccine()
    elif menuOption==2:
        countryDataSelection()
    elif menuOption==3:
        mostDeathOrVaccine()
    elif menuOption==4:
        vaccineType()
    elif menuOption==5:
        popularVaccinePerCountry()
    elif menuOption==6:
        comparisonTotalDeathOrVaccineOnSpecificCountries()
    else:
        print("Please  enter a number from  the menu")   
        
        
        












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


def chart(chartTypes,country,coronavirusInfoType):
    if coronavirusInfoType==5: 
 
    
        
        if chartTypes==1:
            lineGraph(chartTypes,country,coronavirusInfoType)
        elif chartTypes==2:
            barGraph(chartTypes,country,coronavirusInfoType)
        elif chartTypes==3:
            scatterChart(chartTypes,country,coronavirusInfoType)
        elif chartTypes==4:
            cumulativeGraph(chartTypes,country,coronavirusInfoType)
        else:
            print("Invalid choice")
            
def lineGraph(chartTypes,country,coronavirusInfoType):
    # skip the header
    next(casesAndDeathData)
    
    #Two arrays stores the data for x and y axis
    date=[]
    numberofDeathOrCase=[]
    
    
    # read the data from excel file   
    for rowData in casesAndDeathData:
        
        #saves to the arrays
        countryData=int(rowData[2])
        if countryData==country:
            date.append(str(rowData[0]))
            if coronavirusInfoType==1:
                case=rowData[5]
                numberofDeathOrCase.append(case)
            elif coronavirusInfoType==2:
                case=rowData[7]
                numberofDeathOrCase.append(case)
            else:
                print()  
        else:
            print()
    
        #creates a graph and plots it
        fg,ax=plt.subplots()
        ax.polt(date,casesAndDeathData,'mD:')
        
        maxNoCaseOrDeath=max(numberofDeathOrCase)
        minNoCaseOrDeath=min(numberofDeathOrCase)
                    
        #Creates the axis for the graph   
        ax.xaxis.grid(date)
        ax.yaxis.grid()
        
        ax.set_yticks(range(10,maxNoCaseOrDeath,minNoCaseOrDeath))
        
        ax.set_ybound(minNoCaseOrDeath, maxNoCaseOrDeath)
        ax.set_xbound(date)
    




def cumulativeGraph(chartTypes,country,coronavirusInfoType):
    # skip the header
    next(casesAndDeathData)
    
    
    #Two arrays stores the data for x and y axis
    date=[]
    caseCumulative=[]
    
    # read the data from excel file   
    for rowData in casesAndDeathData:
        
        #saves to the arrays
        countryData=int(rowData[2])
        if countryData==country:
            date.append(str(rowData[0]))
            if coronavirusInfoType==1:
                case=rowData[5]
                caseCumulative.append(case)
            elif coronavirusInfoType==2:
                case=rowData[7]
                caseCumulative.append(case)
            else:
                print()  
        else:
            print()
    
        #creates a graph and plots it
        fg,ax=plt.subplots()
        ax.polt(date,caseCumulative,'mD:')
        
        maxNoCaseCumulative=max(caseCumulative)
        minNoCaseCumulative=min(caseCumulative)
                    
        #Creates the axis for the graph   
        ax.xaxis.grid(date)
        ax.yaxis.grid()
        
        ax.set_yticks(range(10,maxNoCaseCumulative,minNoCaseCumulative))
        
        ax.set_ybound(minNoCaseCumulative, maxNoCaseCumulative)
        ax.set_xbound(date)
    
    
    plt.show()        
                    

               
    




def countryDataSelection():
    
    #User inputs
    print("Please enter the country's name below: ")
    country=input()
    print("What type of  Covid 19 related information do you want to know.")
    print("1. Confimed Cases\n 2.Death 3.Vaccination")
    coronavirusInfoType=input()
  
    if coronavirusInfoType==1:
        
        print("Different types of charts to presentation data . ")
        print("1.Line graph \n 2.Bar chart\n 3.Scatter chart\n 4.Cumulative  graph ")
        chartTypes=int(input())
        chart(chartTypes,country,coronavirusInfoType)    
    elif coronavirusInfoType==2:    
        print("Different types of charts to presentation data . ")
        print("1.Line graph \n 2.Bar chart\n 3.Scatter chart\n 4.Cumulative  graph ")
        chartTypes=int(input())
        chart(chartTypes,country,coronavirusInfoType)    
        
    else:
        print()
        
        
    

 
         
           
    







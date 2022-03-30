#Importing essentail libraries
from ctypes.wintypes import tagRECT
import os
from tokenize import String
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
        
        #Two arrays stores the data for x and y axis
        date=[]
        caseOrDeath=[]
           
        # read the data from excel file   
        for rowData in csv_reader:
            
               
            data=rowData[2]
        
            if rowData[2]==country:
                date.append(str(rowData[0]))
                if coronavirusInfoType==1:
                    case=int(rowData[4])
                    caseOrDeath.append(case)
                    yAxisName="Cases"
                    #ax.set_title("Cumulative Cases", fontsize=14)

                elif coronavirusInfoType==2:
                    case=int(rowData[6])
                    caseOrDeath.append(case)
                    yAxisName="Death"

                    #ax.set_title("Cumulative Deaths", fontsize=14)
                else:
                    print()
        #print(date)
       # print(caseOrDeath)
      
    
    plt.bar(date, color='green')
    plt.xlabel("Date")
    
    plt.ylabel(" "+yAxisName)
    plt.title("Number of "+yAxisName+" in "+country)
    plt.axvline(date)
    plt.bar(date,caseOrDeath, width=3, color="blue")
    plt.show()

    #plt.xticks(date, caseOrDeath)
                
        
  

       
    


def scatterChart(chartTypes,country,coronavirusInfoType):
    
    #calls ths function
    with open('WHO-COVID-19-global-data.csv', 'r') as f:
        csv_reader = csv.reader(f)
        # skip the header
        next(csv_reader)
        
        #Two arrays stores the data for x and y axis
        date=[]
        caseOrDeath=[]
           
        #read the data from excel file   
        for rowData in csv_reader:
            
               
            data=rowData[2]
        
            if rowData[2]==country:
                date.append(str(rowData[0]))
                if coronavirusInfoType==1:
                    case=int(rowData[4])
                    caseOrDeath.append(case)
                    yAxisName="Cases"
                    #ax.set_title("Cumulative Cases", fontsize=14)

                elif coronavirusInfoType==2:
                    case=int(rowData[6])
                    caseOrDeath.append(case)
                    yAxisName="Death"

                    #ax.set_title("Cumulative Deaths", fontsize=14)
                else:
                    print()
       # print(date)
        #print(caseOrDeath)
    
    plt.xlabel("Date")
    
    plt.ylabel(" "+yAxisName)
    plt.title("Number of "+yAxisName.lower()+" "+country)

    plt.scatter(date, caseOrDeath)
    plt.show()

      

            
def lineGraph(chartTypes,country,coronavirusInfoType):
    #calls ths function
    with open('WHO-COVID-19-global-data.csv', 'r') as f:
        csv_reader = csv.reader(f)
        # skip the header
        next(csv_reader)
        
        #Two arrays stores the data for x and y axis
        date=[]
        caseOrDeath=[]
           
    
        
        # read the data from excel file   
        for rowData in csv_reader:
            if rowData[2]==country:
                date.append(str(rowData[0]))
                if coronavirusInfoType==1:
                    case=int(rowData[4])
                    caseOrDeath.append(case)
                    yAxisName="Cases"
                    #ax.set_title("Cumulative Cases", fontsize=14)

                elif coronavirusInfoType==2:
                    case=int(rowData[6])
                    caseOrDeath.append(case)
                    yAxisName="Death"

                    #ax.set_title("Cumulative Deaths", fontsize=14)
                else:
                    print()
       
        else:
            print()
    print(date)
    print(caseOrDeath)
    #ax.set_xticks(caseOrDeath.why[0::60])
    fig, ax = plt.subplots(figsize=18)
    if coronavirusInfoType==1:
        plt.plot(caseOrDeath[0::60],caseOrDeath[0::60],'*g--')
    elif coronavirusInfoType==2:
        plt.plot(caseOrDeath[0::60],caseOrDeath[0::60],'rD--')
            

    ax.set_title("Cases", fontsize=3)
    ax.set_title("Deaths", fontsize=3)
    fig, ax = plt.subplots(figsize=(12, 24))
    fig.suptitle("Number of "+yAxisName+" in " + country, fontsize=18)

  
    plt.legend(['Cases', 'Deaths'])
    

    ax.set_facecolor('xkcd:seashell')

    ax.xaxis.grid()
    ax.yaxis.grid()
   
   
    fig.suptitle("Numbers of "+yAxisName+" in "+country, fontsize=25)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel(" "+yAxisName, fontsize=12)
 
    plt.show()     
    
    
   
    
        
    
    
       
   
    



def cumulativeGraph(chartTypes,country,coronavirusInfoType):
    
    with open('WHO-COVID-19-global-data.csv', 'r') as f:
        csv_reader = csv.reader(f)
        # skip the header
        next(csv_reader)
        
        #Two arrays stores the data for x and y axis
        date=[]
        caseOrDeath=[]
   
        
    # read the data from excel file   
        for rowData in csv_reader:
            
               
            data=rowData[2]
        
            if rowData[2]==country:
                date.append(str(rowData[0]))
                if coronavirusInfoType==1:
                    case=int(rowData[4])
                    caseOrDeath.append(case)
                    yAxisName="Cases"
                    #ax.set_title("Cumulative Cases", fontsize=14)

                elif coronavirusInfoType==2:
                    case=int(rowData[6])
                    caseOrDeath.append(case)
                    yAxisName="Death"

                    #ax.set_title("Cumulative Deaths", fontsize=14)
                else:
                    print()
        #print(date)
        #print(caseOrDeath)
       
        fig, ax = plt.subplots()
        ax.set_title("Cumulative Cases", fontsize=14)
        ax.set_title("Cumulative Deaths", fontsize=14)

   
        fig.suptitle("Figure title", fontsize=18)
        ax.set_xlabel("Value", fontsize=12)
        ax.set_ylabel("Square of Value", fontsize=12)
    
        ax.plot(date, ax, 'mD:', label="squares")
        ax.legend() 
        plt.show()        
                    

              
 
    




def countryDataSelection():
        #validInput=True;
        #User inputs
    
        print("Please enter the country's name below: ")
        country=input()
        print("What type of  Covid 19 related information do you want to know.")
        print("1.Confimed Cases\n2.Death")
        coronavirusInfoType=int(input())
    
        if coronavirusInfoType==1:
            print("Different types of charts to presentation data . ")
            print("1.Line graph\n2.Bar chart\n3.Scatter hart\n4.Cumulative  graph ")
            chartTypes=int(input())
            chart(chartTypes,country,coronavirusInfoType)    
        elif coronavirusInfoType==2:    
            print("Different types of charts to presentation data . ")
            print("1.Line graph\n2.Bar chart\n3.Scatter chart\n4.Cumulative graph ")
            chartTypes=int(input())
            chart(chartTypes,country,coronavirusInfoType)    
            
        else:
            print()
            #invaldInput=False



  
    
           
  
def chart(chartTypes,country,coronavirusInfoType):
   # validInput=True;
    
    while True:        
        if chartTypes==1:
            lineGraph(chartTypes,country,coronavirusInfoType)
        elif chartTypes==2:
            barGraph(chartTypes,country,coronavirusInfoType)
        elif chartTypes==3:
            scatterChart(chartTypes,country,coronavirusInfoType)
        elif chartTypes==4:
            cumulativeGraph(chartTypes,country,coronavirusInfoType)
        else:
            print("Invalid graph choice")
            break     

#Menu
optionValid=""
while(True):
    print("Menu")
    print("1 - Top 5 vaccines\n2 - Finding data by country\n3 - What time of year had the most deaths/vaccines?\
        n4. - Type of vaccines used\n5. - Popular vaccine per country\n6. - Comparing total deaths and vaccines of specific countries\n7 - Quit")

    print("Please enter the number  here:")
    menuOption=input()

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
    
        
    
   
    
 

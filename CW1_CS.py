#Importing essentail libraries
from ctypes.wintypes import tagRECT
import os
from tokenize import String
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
#Displays the  data from the Excel files
casesAndDeathData=pd.read_csv("WHO-COVID-19-global-data.csv")
vaccineData=pd.read_csv("vaccination-data.csv")









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


     
                
        
  

       
    


def scatterGraph(chartTypes,country,coronavirusInfoType):
    #skip the header
    next(casesAndDeathData)
    
   #Two arrays stores the data for x and y axis
    date=[]
    numberOfDeathOrCase=[]
    
    
    # read the data from excel file   
#     for rowData in casesAndDeathData:
        
#         #saves to the arrays
#         countryData=int(rowData[2])
#         if countryData==country:
#             date.append(str(rowData[0]))
#             if coronavirusInfoType==1:
#                 case=rowData[5]
#                 numberofDeathOrCase.append(case)
#                 plt.title('Cases')
                
#             elif coronavirusInfoType==2:
#                 case=rowData[7]
#                 numberofDeathOrCase.append(case)
#                 plt.title('Death')
#             else:
#                 print()  
#         else:
#             print()
#    fig=plt.figure([2,0,4,4])
#    ax.scatter(numberofDeathOrCase,color='b')
    
#     plt.xticks(range(len(date)),numberofDeathOrCase)
#     plt.xlabel('Date')
#     plt.ylabel('Amounts')
    
   
#     plt.show()
        
        

      

            
#def lineGraph(chartTypes,country,coronavirusInfoType):
    #calls ths function
    
    
    
   
    
        
    
    
       
        #creates a graph and plots it
    #    plt.plot(date,numberOfDeathOrCase, label=" "+coronavirusInfoType) 
    #    plt.legend()
    #    plt.show()
    



def cumulativeGraph(chartTypes,country,coronavirusInfoType):
    
        #deathRate = casesAndDeathData["Cumulative_deaths"]

   
        
        with open('WHO-COVID-19-global-data.csv', 'r') as f:
            csv_reader = csv.reader(f)
            # skip the header
            next(csv_reader)
        
            #Two arrays stores the data for x and y axis
            date=[]
            caseOrDeathCumulative=[]
           
            # read the data from excel file   
            for rowData in csv_reader:
            
               
                data=rowData[2]
            
                if rowData[2]==country:
                    date.append(str(rowData[0]))
                    if coronavirusInfoType==1:
                        case=rowData[5]
                        caseOrDeathCumulative.append(case)
                        #ax.set_title("Cumulative Cases", fontsize=14)

                    elif coronavirusInfoType==2:
                        case=rowData[7]
                        caseOrDeathCumulative.append(case)
                        #ax.set_title("Cumulative Deaths", fontsize=14)
                    else:
                        print()
            print(date)
            print(caseOrDeathCumulative)
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
   # while validInput !=True:
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
    
   # while validInput:
            
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


#menu    
print("Menu")
print("1.Top 5 vaccines Harry\n2.Finding data by country Shubham\n3.What time of year had the most deaths/vaccines? Lydia\n4.Type of vaccines used Matty\n5.Popular vaccine per country Vince\n6.Comparing total deaths and vaccines of specific countries Charlie")

print("Please enter the number  here:")

menuOption=int(input())
menuSelection(menuOption)
 

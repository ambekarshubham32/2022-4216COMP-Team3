#Importing essentail libraries
from ctypes.wintypes import tagRECT
import os
from tokenize import String
import pandas as pd
import matplotlib.pyplot as plt
from tkinter.font import BOLD
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
        deathAndVaccine()
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
def deathAndVaccine(): 
#Reading files
    covid=pd.read_csv("WHO-COVID-19-global-data.csv")
    vaccination_data=pd.read_csv("vaccination-data.csv")

    #Highest death and vaccine rate in both files
    def highDeathAndVaccine():
    #scan through file and get country with the highets death/vaccine data
    
        death_rate = covid.iloc[covid['Cumulative_deaths'].argmax()]
        vaccine_rate = vaccination_data.iloc[vaccination_data['TOTAL_VACCINATIONS'].argmax()]

        print("The country with the highest death rate is:  ", death_rate.Country, death_rate.Cumulative_cases)
        print("The country with the highest vaccination rate is:  ", vaccine_rate.COUNTRY, vaccine_rate.TOTAL_VACCINATIONS, "\n")


    #Lowest death and vaccine rate in both files
    def lowDeathAndVaccine():

        death_rate = covid.iloc[covid['Cumulative_deaths'].argmin()]
        vaccine_rate = vaccination_data.iloc[vaccination_data['TOTAL_VACCINATIONS'].argmin()]

        print("The country with the lowest death rate is:  ", death_rate.Country, death_rate.Cumulative_cases)
        print("The country with the lowest vaccination rate is:  ", vaccine_rate.COUNTRY, vaccine_rate.TOTAL_VACCINATIONS, "\n")

   
    #Graph for death and vaccine rate per country
    def deathRateGraph():
        #user input for the country of choice
        print("please input a country")
        country_selected = input()

        #linking files to country selected
        country_data = covid[covid.Country==country_selected]

        #creating death cases graph
        fig,ax = plt.subplots()
        fig.suptitle("Number of Deaths from " + country_selected, fontsize=18, weight=BOLD)

        #plotting and labeling country death graph
        ax.plot(country_data.why[0::70], country_data.Cumulative_deaths[0::70], "r--",linewidth=3)
        ax.set_xlabel("Dates", fontsize=12, weight=BOLD)
        ax.set_ylabel("Number of Deaths Reported", fontsize=12, weight=BOLD)

        #graph additions/colours
        ax.set_facecolor("xkcd:pale")
        plt.tight_layout()
        ax.grid(True)
        plt.legend("deaths")

        plt.show()


#Menu options
def menu():
    strs =("1.Highest Death and Vaccine rate per Country\n"
                "2.Lowest Death and Vaccine rate per Country\n"
                "3.Death Rates graph\n"
                )
    print("Please input choice: ")
    
    choice = input(strs)
    return int(choice)


#While loop for the menu
while True:
    choice = menu()
    if choice == 1:
        highDeathAndVaccine()
    elif choice == 2:
        lowDeathAndVaccine()
    elif choice == 3:
        deathRateGraph()
    elif choice >3:
        print("Incorrect input, please try again \n")
    else:
        break


#Matty
#def vaccineType():


#Vince 
#def popularVaccinePerCountry():


#Charlie
#def comparisonTotalDeathOrVaccineOnSpecificCountries():



















#Shubham




        
        
def barGraph(chartTypes,country,coronavirusInfoType):
    #skip the header
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
                plt.title('Cases')
                
            elif coronavirusInfoType==2:
                case=rowData[7]
                numberofDeathOrCase.append(case)
                plt.title('Death')
            else:
                print()  
        else:
            print()
    plt.xticks(range(len(date)),numberofDeathOrCase)
    plt.xlabel('Date')
    plt.ylabel('Amounts')
    plt.bar(range(len(date)), date)
    plt.show()
      

            
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
    

 
         
           
    







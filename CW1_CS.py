
#imported libraries
from ctypes.wintypes import tagRECT
from tokenize import String
import pandas as pd
import matplotlib.pyplot as plt
import csv
from tkinter.font import BOLD
import csv

#Displays the  data from the Excel files
casesAndDeathData=pd.read_csv("WHO-COVID-19-global-data.csv")
vaccineData=pd.read_csv("vaccination-data.csv")

#Harry
def vaccineComparisonData():

    vaccination_data = pd.read_csv("vaccination-data.csv")
    file = vaccination_data[['COUNTRY', 'TOTAL_VACCINATIONS']]
    #begins reading from the file

    print("Welcome! Please input the name of a country :")
    choice = input()

    countryData = file[file.COUNTRY == choice]
    print(countryData)
    #requests the user's first choice and prints it

    print("Please input a country to compare this to :")
    second_choice = input()

    second_country = file[file.COUNTRY == second_choice]
    print(second_country)
    #requests the user's second choice and prints it

    fig, ax = plt.subplots(figsize=(5,6))
    fig.suptitle(choice + " vs " + second_choice + " Total Vaccinations", fontsize=18)
    plt.xlabel('Countries', fontsize=18)
    plt.ylabel('Vaccinations', fontsize=18)
    #sets the dimensions and titles of the bar chart

    ax.bar(countryData.COUNTRY, countryData.TOTAL_VACCINATIONS)
    ax.bar(second_country.COUNTRY, second_country.TOTAL_VACCINATIONS)
    plt.legend([choice, second_choice])
    #plots the data onto the bar chart

    ax.set_facecolor('xkcd:grey')
    fig.patch.set_facecolor('xkcd:white')
    #changes the colours of some elements of the bar chat

    plt.show()
    #shows the bar chart
    

    
 
#Lydia    
def deathAndVaccine(): 
#Reading files
    covid=pd.read_csv("WHO-COVID-19-global-data.csv")
    vaccination_data=pd.read_csv("vaccination-data.csv")

    #Highest death and vaccine rate in both files
    def highDeathAndVaccine():
    #scan through file and get country with the highets death/vaccine data
    
        death_rate = covid.iloc[covid['Cumulative_deaths'].argmax()]
        vaccine_rate = vaccineData.iloc[vaccineData['TOTAL_VACCINATIONS'].argmax()]

        print("The country with the highest death rate is:  ", death_rate.Country, death_rate.Cumulative_cases)
        print("The country with the highest vaccination rate is:  ", vaccine_rate.COUNTRY, vaccine_rate.TOTAL_VACCINATIONS, "\n")


    #Lowest death and vaccine rate in both files
    def lowDeathAndVaccine():

        death_rate = covid.iloc[covid['Cumulative_deaths'].argmin()]
        vaccine_rate = vaccineData.iloc[vaccination_data['TOTAL_VACCINATIONS'].argmin()]

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
def vaccineType():

#import modules 
    import csv
    import matplotlib.pyplot as plt
    AZtotal = 0
    PFtotal = 0
    Jtotal = 0
    BJtotal = 0
    Stotal = 0
    BHtotal = 0
    GMtotal = 0
    MDtotal = 0
    #read from file of vaccine data 
    inputfile = csv.reader(open('vaccination-data.csv','r'))
    with open('vaccination-data.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)

        C = []
        for row in csv_reader:
            data = row[11]
            C.append(data)
        
    #search for the number of times each vaccine has been used
    for item in C:
        if "AstraZeneca" in item:
            AZtotal = AZtotal+ 1
        if "Moderna" in item:
            MDtotal = MDtotal+ 1
        if "Pfizer" in item:
            PFtotal = PFtotal+ 1
        if "Janssen" in item:
            Jtotal = Jtotal+ 1
        if "Beijing" in item:
            BJtotal = BJtotal+ 1
        if "SII" in item:
            Stotal = Stotal+ 1
        if "Bharat" in item:
            BHtotal = BHtotal+ 1
        if "Gamaleya" in item:
            GMtotal = GMtotal+ 1

    #set up the data ready for the bar graph 
    VaccinesNames = ["Astrazeneca", "Moderna", "Pfizer", "Janssen", "Beijing", "SII", "Bharat", "Gamaleya"]
    VaccineDataPlot = [AZtotal, MDtotal, PFtotal, Jtotal, BJtotal, Stotal, BHtotal, GMtotal]

    #plot the data 
    fig, ax = plt.subplots()
    ax.set_xlabel("Vaccine Names")
    ax.set_ylabel("Number of countries using each vaccine")
    ax.set_title("Vaccine Bar Graph")
    ax.bar(VaccinesNames, VaccineDataPlot)

    #show the graph to the user
    plt.show()



#Vince 
def popularVaccinePerCountry():

    #introduuction
    print("\nWelcome!\n")

    #while loop so program repeats for user to select multiple options
    while(True):
        firstInput = str(input(print("\nENTER.. \n\n"+"D for Dataset\n"+"P for Pie Chart\n"+"B for Bar Chart\n"+"L for Line Graph\n"+"Q for quit")))

        #quit option for user to exit the program
        if firstInput == 'Q' :
            print("\nThank you for using the service!\n")
            break
  
        if firstInput == 'D' :
            print("\nHere is the data set of popular vaccines from 224 countries\n")
            countries = []
            count = []
            with open('C:\\Users\\User\\OneDrive\\Desktop\\teamproject\\mydata.txt','r') as file:
                data = file.readlines()
            for i in data:
                broken = i.split('\t')
                print(broken)

        #Pie chart construction
        elif firstInput == 'P' :
            plt.figure(figsize=(15,15))
            plt.title("Pie Chart of Most Popular Vaccines from a Group of Countries",fontsize = 20)
            countries = []
            count = []
            explode = (0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            with open('C:\\Users\\User\\OneDrive\\Desktop\\teamproject\\mydata.txt','r') as file:
                data = file.readlines()
            for i in data:
                broken = i.split('\t')
                countries.append(broken[0])
                count.append(int(broken[1]))
            plt.pie(count, explode=explode, labels=countries, autopct='%1.1f%%', startangle = 75, radius= 1,wedgeprops = {"edgecolor" : "black",'linewidth': 1,'antialiased': True})
            labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(countries, count)]
            plt.axis('equal')
            plt.show()

        #Bar chart construction
        elif firstInput == 'B' :
            plt.figure(figsize=(15,15))
            plt.title("Bar Chart of Distribution of Vaccines",fontsize = 20)
            Countries = []
            count = []
            with open('C:\\Users\\User\\OneDrive\\Desktop\\teamproject\\mydata.txt','r') as file:
                data = file.readlines()
            for i in data:
                broken = i.split('\t')
                Countries.append(broken[0])
                count.append(int(broken[1]))
                plt.bar(Countries,count)
                plt.xlabel('Vaccines')
                plt.ylabel('Number of Countries')
            plt.show()

        #Line Chart construction
        else:
            plt.figure(figsize=(15,15))
            Countries = []
            count = []
            with open('C:\\Users\\User\\OneDrive\\Desktop\\teamproject\\mydata.txt','r') as file:
                data = file.readlines()
                for i in data:
                    broken = i.split('\t')
                Countries.append(broken[0])
                count.append(int(broken[1]))
                plt.plot(Countries,count)
                plt.title("Line Graph of Vaccine Popularity Amongst a Group Of Countries",fontsize = 20)
                plt.xlabel('Vaccines')
                plt.ylabel('Total')
            plt.show()


#Charlie
def totalCasesPerSelectedCountry():
    print ("What Country would you like data for?")
    country = input()
    #Asking user for country to base data around

    countryData = casesAndDeathData[casesAndDeathData.Country == country]
    print(countryData)
    #Finding and printing data for users choice

    fig, ax = plt.subplots(figsize=(24, 12))
    fig.suptitle(country + " total cases and deaths", fontsize=18)
    ax.set_title("From 03/01/2020 to 23/12/21", fontsize=18)
    #Setting the size of the graph and titling it

    plt.plot(countryData.why[0::60], countryData.Cumulative_cases[0::60], 'g*--')
    plt.plot(countryData.why[0::60], countryData.Cumulative_deaths[0::60], 'rD--')
    plt.legend(['Cases', 'Deaths'])
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Cases/Deaths', fontsize=18)
    #Plotting the graph and its axis

    ax.set_facecolor('xkcd:light cyan')
    fig.patch.set_facecolor('xkcd:silver')
    #Changing colour of the graph and the background

    plt.grid(color='black', linestyle='-.', linewidth=0.7)
    #Adding a grid to the graph

    plt.show()
    #Displaying the graph

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
    print("1 - Top 5 vaccines\n2 - Find data by country\n3 - Deaths and Vaccines information\n4 - Type of vaccines used\n5 - Popular vaccine per\
        country\n6 - Comparing total deaths and cases of specific countries\n7\
        - Quit\nPlease enter the number   below:")

    #user enter's the choosen option
    
    menuOption=input()

    #Runs a function depending on the user's input
    if menuOption=="1":
        vaccineComparisonData()
    elif menuOption=="2":
        countryDataSelection()
    elif menuOption=="3":
        deathAndVaccine()
    elif menuOption=="4":
        vaccineType()
    elif menuOption=="5":
        popularVaccinePerCountry()

    elif menuOption=="6":
        totalCasesPerSelectedCountry()
    elif menuOption=="7":
        break 
    else:
        print("Invalid Input.Please enter a number from the menu.")

         
           
    






    

 
         
           
    







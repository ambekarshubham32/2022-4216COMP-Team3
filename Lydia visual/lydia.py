#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
from tkinter.font import BOLD

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

    
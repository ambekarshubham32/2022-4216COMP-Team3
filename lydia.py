#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt


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
def deathAndVaccineGraph():
    print("please input a country")
    country_selected = input()

    #linking files to country selected
    country_data = covid[covid.Country==country_selected]
    vaccines = vaccination_data[vaccination_data.COUNTRY==country_selected]

    #creating 2 graphs
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle("Number of Deaths and Vaccinations from " + country_selected, fontsize=18)

    #plotting and labeling country death graph
    ax1.plot(country_data.why[0::96], country_data.Cumulative_deaths[0::96], "mD--")
    ax1.set_xlabel("Dates")
    ax1.set_ylabel("Deaths Reported")

    #plotting and labeling country and vaccinations graph
    ax2.plot(vaccines.DATE_UPDATED, vaccines.TOTAL_VACCINATIONS, "mD--")
    ax2.set_xlabel("Dates")
    ax2.set_ylabel("Vaccinations Reported")

    plt.legend("deaths")
    plt.show()


#Menu options
def menu():
    strs =("1.Highest Death and Vaccine rate per Country\n"
                "2.Lowest Death and Vaccine rate per Country\n"
                "3.Death and Vaccines rates graph\n"
                "4. Return to previous menu :\n ")
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
        deathAndVaccineGraph()
    elif choice >3:
        print("Incorrect input, please try again \n")
    else:
        break

    
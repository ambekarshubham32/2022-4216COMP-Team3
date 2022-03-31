
import pandas as pd
from matplotlib import pyplot as plt

#reading from the files
covid= pd.read_csv("WHO-COVID-19-global-data.csv")
vaccination_data= pd.read_csv("vaccination-data.csv")

#user input for the country of choice
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


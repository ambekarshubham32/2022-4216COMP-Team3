
from tkinter.font import BOLD
import pandas as pd
from matplotlib import pyplot as plt
from sympy import rotations

#reading from the files
covid= pd.read_csv("WHO-COVID-19-global-data.csv")
vaccination_data= pd.read_csv("vaccination-data.csv")

#user input for the country of choice
print("please input a country")
country_selected = input()

#linking files to country selected
country_data = covid[covid.Country==country_selected]
vaccines = vaccination_data[vaccination_data.COUNTRY==country_selected]

#creating death cases graph
fig,ax = plt.subplots()
fig.suptitle("Number of Deathsfrom " + country_selected, fontsize=18, weight=BOLD)

#plotting and labeling country death graph
ax.plot(country_data.why[0::70], country_data.Cumulative_deaths[0::70], "r--",linewidth=3)
ax.set_xlabel("Dates", fontsize=12, weight=BOLD)
ax.set_ylabel("Deaths Reported", fontsize=12, weight=BOLD)

#adding colour to the graph
#ax.set_facecolor("xkcd: silver")

#additions to add context to the graph
plt.tight_layout()
ax.grid(True)
plt.legend("deaths")

plt.show()


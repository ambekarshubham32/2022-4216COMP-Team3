import matplotlib.pyplot as plt
import pandas as pd
#Importing the essential libraries

data = pd.read_csv('WHO-COVID-19-global-data.csv')
#Reading the data from the excel file

print ("What Country would you like data for?")
country = input()
#Asking user for country to base data around

countryData = data[data.Country == country]
print(countryData)
#Finding and printing data for users choice

fig, ax = plt.subplots(figsize=(24, 12))
fig.suptitle(country + " total cases and deaths", fontsize=18)
ax.set_title("From 03/01/2020 to 11/12/21", fontsize=18)
#Setting the size of the graph and titling it

plt.plot(countryData.Date_reported[0::59], countryData.Cumulative_cases[0::59], 'g*--')
plt.plot(countryData.Date_reported[0::59], countryData.Cumulative_deaths[0::59], 'rD--')
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
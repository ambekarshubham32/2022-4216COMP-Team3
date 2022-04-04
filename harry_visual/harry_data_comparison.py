
import matplotlib.pyplot as plt
import pandas as pd
#imports the necessary libraries

vaccination_data = pd.read_csv("/Users/harry/Desktop/vaccination-data.csv")
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



    


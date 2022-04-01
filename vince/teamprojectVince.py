import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(15,15))
plt.title("Pie Chart of Most Popular Vaccines from a Group of Countries",fontsize = 20)

countries = []
count = []
explode = (0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0)
with open('C:\\Users\\User\\OneDrive\\Desktop\\teamproject\\piechart.txt','r') as file:
    data = file.readlines()
for i in data:
    broken = i.split('\t')
    print(broken)
    countries.append(broken[0])
    count.append(int(broken[1]))
    
plt.pie(count, explode=explode, labels=countries, autopct='%1.1f%%', startangle = 75, radius= 1,wedgeprops = {"edgecolor" : "black",'linewidth': 1,'antialiased': True})
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(countries, count)]
plt.axis('equal')


plt.show()


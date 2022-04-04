import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("\nWelcome!\n")
firstInput = input(print("\nENTER.. \n\n"+"D for Dataset\n"+"P for Pie Chart\n"+"B for Bar Chart\n"+"L for Line Graph\n"))

if firstInput == 'D' :
  print("\nHere is the data set of popular vaccines from 224 countries\n")
  countries = []
  count = []
  with open('C:\\Users\\User\\OneDrive\\Desktop\\teamproject\\mydata.txt','r') as file:
      data = file.readlines()
  for i in data:
      broken = i.split('\t')
      print(broken)


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
      plt.xlabel('Countries')
      plt.ylabel('Number of Countries')
  plt.show()

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

  







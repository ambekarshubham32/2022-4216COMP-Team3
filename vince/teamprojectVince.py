import matplotlib.pyplot as plt

countries = []
count = []
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

with open('C:\\Users\\User\\OneDrive\\Desktop\\teamproject\\piechart.txt','r') as file:
    data = file.readlines()
for i in data:
    broken = i.split('\t')
    print(broken)
    countries.append(broken[0])
    count.append(int(broken[1]))
plt.pie(amount, explode=explode, labels=countries, autopct='%1.1f%%', shadow=True, startangle = 75)
plt.show()
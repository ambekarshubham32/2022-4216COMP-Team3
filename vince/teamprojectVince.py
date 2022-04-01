import matplotlib.pyplot as plt

countries = []
count = []
with open('C:\\Users\\User\\OneDrive\\Desktop\\teamproject\\piechart.txt','r') as file:
    data = file.readlines()
for i in data:
    broken = i.split('\t')
    print(broken)
    countries.append(broken[0])
    count.append(int(broken[1]))
plt.pie(countries)
plt.show()
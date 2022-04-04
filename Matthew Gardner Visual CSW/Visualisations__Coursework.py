import csv
import matplotlib.pyplot as plt

AZtotal = 0
PFtotal = 0
Jtotal = 0
BJtotal = 0
Stotal = 0
BHtotal = 0
GMtotal = 0
MDtotal = 0


inputfile = csv.reader(open('M:\python\coursework\VaccineData.csv','r'))
with open('M:\python\coursework\VaccineData.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)

    C = []
    for row in csv_reader:
        data = row[11]
        C.append(data)
        

for item in C:
    if "AstraZeneca" in item:
        AZtotal = AZtotal+ 1
    if "Moderna" in item:
        MDtotal = MDtotal+ 1
    if "Pfizer" in item:
        PFtotal = PFtotal+ 1
    if "Janssen" in item:
        Jtotal = Jtotal+ 1
    if "Beijing" in item:
        BJtotal = BJtotal+ 1
    if "SII" in item:
        Stotal = Stotal+ 1
    if "Bharat" in item:
        BHtotal = BHtotal+ 1
    if "Gamaleya" in item:
        GMtotal = GMtotal+ 1


VaccinesNames = ["Astrazeneca", "Moderna", "Pfizer", "Janssen", "Beijing", "SII", "Bharat", "Gamaleya"]
VaccineDataPlot = [AZtotal, MDtotal, PFtotal, Jtotal, BJtotal, Stotal, BHtotal, GMtotal]

fig, ax = plt.subplots()
ax.set_title("Vaccine Bar Graph")
ax.bar(VaccinesNames, VaccineDataPlot)

plt.show()




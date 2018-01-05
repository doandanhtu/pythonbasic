import csv
days = []
temps = []
with open('nhietdo.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        days.append(int(row[0]))
        temps.append(float(row[1]))

print(days)
print(temps)
from pylab import plot, show
plot(days, temps, 'o')
show()
#! python3
# CrimeGraphs.py - takes crime data from CSV file and plots number of crimes
# that occur per day

import matplotlib.pyplot as plt
import csv

# Opens CSV file in read mode
file = open('sample_data.csv', 'r')
csv = csv.reader(file)

# Initialises crime dictionary
crimeDict = {}

# Iterates through each line of data extracting crimes per date
for line in csv:
    date = str(line[2])
    if date == 'Date Occurred' or date == '':
        continue
    elif date in crimeDict.keys():
        crimeDict[date] += 1
    else:
        crimeDict[date] = 1

# Declares x and y values for plotting
x = [k for k in crimeDict]
y = [k for k in crimeDict.values()]

# Plots data
plt.plot(x, y)
plt.show()

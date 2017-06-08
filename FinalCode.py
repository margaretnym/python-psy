import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from collections import OrderedDict #for sorting dictionary

# Reading in csvs and turning all csvs to dictionaries
import csv
with open("ListRegions.csv", 'r') as csvfile1:
    data_ListRegions = csv.reader(csvfile1, delimiter=',')
    dict_ListRegions = {}
    for row in data_ListRegions:
        dict_ListRegions[row[0]] = row[1:]
        
with open("LandAreaByState.csv", 'r') as csvfile2:
    data_LandAreaByState = csv.reader(csvfile2, delimiter=',')
    dict_LandAreaByState = {}
    for row in data_LandAreaByState:
        dict_LandAreaByState[row[0]] = row[1:]
        
with open("Census2010byState.csv", 'r') as csvfile3:
    data_Census2010byState = csv.reader(csvfile3, delimiter=',')
    dict_Census2010byState = {}
    for row in data_Census2010byState:
        dict_Census2010byState[row[0]] = row[1:]

#initialization
pop = {}
area = {}
density = {}

for regions in dict_ListRegions:
    pop[regions] = []
    area[regions] = []
    density[regions] = []
    
for regions in dict_ListRegions:
    for i in range(0,len(dict_ListRegions[regions])):
        pop[regions] = pop[regions] + dict_Census2010byState[dict_ListRegions[regions][i]]
        area[regions] = area[regions] + dict_LandAreaByState[dict_ListRegions[regions][i]]

    density[regions] = sum(list(map(int, pop[regions])))/sum(list(map(int, area[regions])))

# Ordering a dictionary in ascending order    
ordered_density = OrderedDict(sorted(density.items(), key=lambda t: t[1]))    

# Plotting the bar chart
plt.figure(figsize=(16,8))    
bar_width = 0.5
x = np.arange(len(dict_ListRegions))

plt.bar(left=x+bar_width/2, height=ordered_density.values() , width = bar_width, color='r')

plt.xlabel('Geographical Divisions')
plt.ylabel('Population Density (people per sq. mi.) ')
plt.title('Population Density by Geographical Divisions')

plt.xticks(x+bar_width, ordered_density.keys())

plt.savefig('Density.png', dpi= 300)
plt.show()
    
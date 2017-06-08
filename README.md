# python-psy
UT Psychology Python Class


Problem: Population Density by Geog Divisions

Details: If you are interested in reading the code, here are some details about how the program proceeds: 
1.	Read in all those three csv files.
2.	For ListRegions.csv, create a dictionary with the first items in each row in the csv as keys and 
    the rest in the same row as values.
3.	For Census2010byState.csv and LandAreaByState.csv, create two dictionaries: dict_Census2010byState 
    and dict_LandAreaByState -- with the state names as the keys and the population and area as the 
    values respectively. 
4.	To calculate the population density in each division, divide the sum of population by the sum of 
    the land area of each divisions to calculate the population density (people per sq. mi.) in these 
    9 divisions (i.e., total population over total land area). Return as a dictionary with the name 
    of the divisions as keys and the number density as values.
5.	Sort the density dictionary in ascending order.
6.	Produce a bar graph comparing these 9 divisions. In the bar graph, the x- and y-axis are labeled
    as “Division” and “Density” respectively, with each division shown as a tick mark on the x-axis.

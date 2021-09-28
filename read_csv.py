# Pull the path into the file so it can be used later
PATH = r'C:\Users\mattr\OneDrive\Desktop\AFIT\Tab 1 - Current Semester\EENG_032_Python\read_data_pandas'
# Notice the 'r' before the main string. That creates a "raw" string...neccesary for the read_csv to work

#File name that will serve as the target data
DATA = 'd.csv'

import pandas as pd #Pandas is a data processing tool
import os #os tools used to acces system specific stuff
import matplotlib.pyplot as plt #Load the plotting tools for python

file_nm = os.path.join(PATH, DATA) #Write full path

d = pd.read_csv(file_nm) # Pull the data in using pandas

print('=================================================\n')
print(d.columns + '\n') # Pulls the header column names
print('=================================================\n \n')
print(d.describe()) #Delivers on some very interesting data in the csv
print('=================================================\n \n')
print(d) #Prints the full csv file
print('=================================================\n \n')

d.plot(x='Report Month/Year', y='Fuel Quantity (In Gallons)')
plt.show()

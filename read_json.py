# Pull the path into the file so it can be used later
PATH = r'C:\Users\mattr\OneDrive\Desktop\AFIT\Tab 1 - Current Semester\EENG_032_Python\read_data_pandas'
# Notice the 'r' before the main string. That creates a "raw" string...neccesary for the read_csv to work

#File name that will serve as the target data
DATA = 'd.json'

import pandas as pd #Pandas is a data processing tool
import os #os tools used to acces system specific stuff
import matplotlib.pyplot as plt #Load the plotting tools for python
import json #package used to manage json data objects

file_nm = os.path.join(PATH, DATA) #Write full path

# Pull in the json data using with and open
with open(file_nm) as json_data:
    d = json.load(json_data)

# Json data is pegged to 'keys'
print(d.keys()) # retuns dict_keys(['meta', 'data'])

# Analyze the type set of the values attached to the keys
print(type(d['data'])) # returns <class 'list'>

# Begin accessing the data from the json
print(d['data'][0]) # Returns what I think is the first row, BUT WITHOUT HEADERS!

#We can begin using the pandas toolbox to make accessing this information much easier
d_json = pd.DataFrame(d['data'])
#print(d_json) #Prints everything out without headers

#Notably, we are getting some weird data in the first few columns. Lets strip that out
A = d_json.iloc[:, -3:] #Pull all rows and the coumns beginning three from the end to the end
print(A)

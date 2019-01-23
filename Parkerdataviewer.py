# Import requisit libraries 

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shapely


# Read in data
# Set working directory
local_path= 'C:\Users\Greg\Documents\Repositories\19thAD'
loc="test.csv"

# This should read in the data
#df = pd.read_csv(loc)
#df = open(loc, 'w')


#print type(df)
print 'test'

#data = np.loadtxt('test.csv', delimiter=',', dtype=str)
#data

#csv = np.genfromtxt ('test.csv', delimiter=",")

infile = open('test.csv', 'r')

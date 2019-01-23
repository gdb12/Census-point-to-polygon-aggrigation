# Important Notes:

# 1) There are five records with the county ID of 733. There is no county listed under that ID, though the 700 range is for Texas.
#    I added 733 to the csv I created, with the lable 'Unknown Texas County'
#    242 Unknown Georgia County: 10 counties


# LOAD PYTHON PACKAGES
import numpy as np 
import pandas as pd
import pyper as pr
import matplotlib.pyplot as plt
import string

# READ DATA
counties = pd.read_csv("C:\Users\Greg\Documents\Parker py code\counties.csv", header = 0)
parker = pd.read_csv("C:\Users\Greg\Documents\Documents\PypeR\Parker1860.txt", header = 0)
counties.rename(columns = {list(counties)[1]: 'County'}, inplace = True)

# Create County ID: County dictionary 
counties_dic= counties.set_index('COUNTYID').to_dict()

# Data Processing
#parker.columns = ['COUNTYID', 'SOILID', 'COUNTYSAMPLE']
parker.rename(columns={'V1':'COUNTYID'}, inplace=True)
parker.rename(columns={'V2':'SOILID'}, inplace=True)
parker.rename(columns={'V3':'COUNTYSAMPLE'}, inplace=True)
parker.rename(columns={'V4':'AGY007A'}, inplace=True)
parker.rename(columns={'V5':'CENSUSID'}, inplace=True)

# Data Processing 
parker['State'] = 'placeholder'
parker['County'] = 'placeholder'
length=  len(parker['COUNTYID'])
parser= np.arange(0, length)
a= 0
for i in parker['COUNTYID']:
    parker['County'][i] = counties_dic['County'][parker['COUNTYID'][i]]

# Add State names to each record
for i in parser:
    if parker['COUNTYID'][i] == 0:
        parker['State'][i] =  'Unknown1'
    elif parker['COUNTYID'][i] <51:
        parker['State'][i] =  'ALABAMA'
    elif parker['COUNTYID'][i] <129:
        parker['State'][i] =  'FLORIDA'
    elif parker['COUNTYID'][i] <285:
        parker['State'][i] =  'GEORGIA'
    elif parker['COUNTYID'][i] <332:
        parker['State'][i] =  'LOUISIANA'    
    elif parker['COUNTYID'][i] <403:
        parker['State'][i] =  'MISSISSIPPI'
    elif parker['COUNTYID'][i] <446:
        parker['State'][i] =  'NORTHCAROLINA'
    elif parker['COUNTYID'][i] <536:
        parker['State'][i] =  'SOUTHCAROLINA'
    elif parker['COUNTYID'][i] <619:
        parker['State'][i] =  'TENNESSEE'
    elif parker['COUNTYID'][i] <762:
        parker['State'][i] =  'TEXAS'
    elif parker['COUNTYID'][i] <805:
        parker['State'][i] =  'VIRGINIA'
    else:
        parker['State'][i] = 'Unknown2'
print parker['State'].unique()
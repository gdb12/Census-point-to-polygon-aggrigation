# 19thAD
This repository is for working on projects focusing on the 19th century.
--------
In the 1970's and 80's, William N. Parker and Robert E. Gallman collected a random samples of 1860 census returns from farm housholds from the slave ownng South. While the county level data is available, this is the only unaggrigated subset. This makes the data unique in agricultural, economic, and southern history. Unfortunately, data anlaysis has evelved significantly sense then, and it does not intereact well with modern systems. This is largely due to the laborious process of transcribing historical documents into a database. Due to the way the data was hand coded, it could not be intigrated with the Historical GIS' shape files or used in any spatial analysis of the data. 

This python code wrangles the raw data and adds the state name from the published code book. This allows the data to be related to hsitorical county shapefiles. It also makes it possible to subset the data by state and county. This enables summary statistics to be produced from the data.

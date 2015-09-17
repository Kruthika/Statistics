# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 01:55:04 2015

@author: Kruthika
"""

import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()
data = [i.split(', ') for i in data]
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
print data_rows
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)
alcohol = df['Alcohol']
tobacco = df['Tobacco']

#COncatenation of alcohol and tobacco datasets
verticalStack = pd.concat([alcohol, tobacco], axis=0)
print verticalStack

mean=verticalStack.mean() 
print("The mean of alcohol and tobacco dataset is {}".format(mean))

median=verticalStack.median()
print("The median of alcohol and tobacco dataset is {}".format(median))

# If all numbers occur equally often, stats.mode() will return the smallest number
mode=stats.mode(verticalStack) 
print("The mode of alcohol and tobacco dataset is {}".format(mode))

range1= max(verticalStack) - min(verticalStack)
print("The range of alcohol and tobacco dataset is {}".format(range1))

std_dev = (verticalStack).std() 
print("The standard deviation of alcohol and tobacco dataset is {}".format(std_dev))

variance = (verticalStack).var() 
print("The variance of alcohol and tobacco dataset is {}".format(variance))



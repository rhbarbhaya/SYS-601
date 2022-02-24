# -*- coding: utf-8 -*-
"""
This is an example Python script to perform basic plotting functions.

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# import the pandas package to handle data structures, refer to it as pd
import pandas as pd
# import the numpy package to handle numerical data, refer to it as np
import numpy as np
# import the matplotlib.pyplot package for plotting, refer to it as plt
import matplotlib.pyplot as plt
# import the ListedColormap file from matplotlib to customize colors
from matplotlib.colors import ListedColormap

# read the csv file to a data frame
df = pd.read_csv('wx_nyc_2015.csv')
# define the number of days stored in the file
numDays = len(df)
# define the first day of the week in the file (4 = thursday)
initDay = 4

# parse the weather conditions on each day into an array
conditions = np.array([
    0 if events is np.nan       # store a 0 if events is not a number (nan)
    else 2 if 'Snow' in events  # store a 2 if events contains 'Snow'
    else 1 if 'Rain' in events  # store a 1 if events contains 'Rain'
    else 0                      # otherwise store a 0 (should not happen)
    for events in df[' Events'].values  # loop over all rows of 'Events' column
])
# copy the max temperature on each day to an array
maxTemp = df['Max TemperatureF'].values
# copy the min temperature on each day to an array
minTemp = df['Min TemperatureF'].values

# set the default plot font size to 12
plt.rcParams['font.size'] = 12
# set the default plot font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

#%% This section creates a plot to visualize the conditions on each day

# initialize the data to an array of 53 weeks x 7 days = 371 elements of -1
data = -1*np.ones(53*7)
# overwrite the data for the conditions recorded from the csv file
data[initDay:numDays+initDay] = conditions
# resize from a 371x1 array to a 53x7 matrix
data.resize(53,7)
# create a new figure
plt.figure()
# use the matshow function to plot the data with a custom color map
plt.matshow(np.transpose(data), cmap=ListedColormap(['#000000','#3399ff','#b3b3b3','#ffffff']))
# set the y-axis label and ticks to show the days of the week
plt.ylabel('Day')
plt.yticks(range(0,7),['Su','Mo','Tu','We','Th','Fr','Sa'])
# set the x-axis label and ticks to show the months (calculate which column!)
plt.xlabel('Week')
month_cols = np.cumsum([initDay,31,28+(1 if numDays>365 else 0),31,30,31,30,31,31,30,31,30])/7
plt.xticks(month_cols, ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
# add a colorbar to the plot and set the labels for various conditions
cbar = plt.colorbar(ticks=[-1, 0, 1, 2])
cbar.ax.set_yticklabels(['N/A', 'Clear', 'Rain', 'Snow'])

#%% This section creates a plot to visualize the max temperature on each day

# initialize the data to an array of 53 weeks x 7 days = 371 elements of -1
data = -1*np.ones(53*7)
# overwrite the data for the max temperature recorded from the csv file
data[initDay:numDays+initDay] = maxTemp
# resize from a 371x1 array to a 53x7 matrix
data.resize(53,7)
# create a new figure
plt.figure()
# use the matshow function to plot the data
plt.matshow(np.transpose(data))
# set the y-axis label and ticks to show the days of the week
plt.ylabel('Day')
plt.yticks(range(0,7),['Su','Mo','Tu','We','Th','Fr','Sa'])
# set the x-axis label and ticks to show the months (calculate which column!)
plt.xlabel('Week')
month_cols = np.cumsum([initDay,31,28+(1 if numDays>365 else 0),31,30,31,30,31,31,30,31,30])/7
plt.xticks(month_cols, ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
# add a colorbar
plt.colorbar()

#%% This section creates a histogram of the condition frequencies

# create a new figure
plt.figure()
# define the categories as a list of integers 0, 1, 2
categories = range(3)
# count the frequency of each condition equal to the category values
frequencies = [sum(conditions==i) for i in categories]
# use the bar function to create a histogram with the associated tick labels
plt.bar(categories, frequencies, align='center')
# set the x-axis label and ticks to show the conditions
plt.xlabel('Condition')
plt.xticks(categories, ['Clear', 'Rain', 'Snow'])
# set the y-axis label
plt.ylabel('Frequency')

#%% This section creates a pie chart of the condition frequencies

# create a new figure
plt.figure()
# define the categories as a list of integers 0, 1, 2
categories = range(3)
# count the frequency of each condition equal to the category values
frequencies = [sum(conditions==i) for i in categories]
plt.pie(frequencies, colors=['#3399ff','#b3b3b3','#ffffff'], 
         labels=['Clear', 'Rain', 'Snow'], autopct='%1.1f%%')
# set the axis to have equal scales (makes it a circle)
plt.axis('equal')

#%% This section creates a histogram of the max temperature frequencies

# create a new figure
plt.figure()
# define the bin width
bin_width = 5
# define the bins to be integers from 0 to 100 (by 5)
bins = range(0,100,bin_width)
# count the frequencies in each bin by summing values >= lower bound and < upper bound
frequencies = [sum(np.logical_and(maxTemp>=i,maxTemp<i+bin_width)) for i in bins]
# use the bar function to create the histogram with associated tick labels
plt.bar(bins, frequencies, width=bin_width, align='edge')
# set the x-axis and y-axis labels
plt.xlabel('Max Temp')
plt.ylabel('Frequency')

#%% This section creates a histogram of the max temperature frequencies

# create a new figure
plt.figure()
# define the bin width using freedman-diaconis rule
bin_width = 2*(np.percentile(maxTemp, 75) - np.percentile(maxTemp, 25))/np.power(len(maxTemp), 1./3)
# define the bins to be between min and max temp with specified bin widths
bins = np.arange(min(maxTemp),max(maxTemp),bin_width)
# count the frequencies in each bin by summing values >= lower bound and < upper bound
frequencies = [sum(np.logical_and(maxTemp>=i, maxTemp<i+bin_width)) for i in bins]
# use the bar function to create the histogram with associated tick labels
plt.bar(bins, frequencies, width=bin_width, align='edge')
# set the x-axis and y-axis labels
plt.xlabel('Max Temp')
plt.ylabel('Frequency')

#%% This section creates a histogram using the automatic features of matplotlib.

# create a new figure
plt.figure()
# use the hist function to draw the histogram
frequencies, bins, patches = plt.hist(maxTemp)
# set the x-axis and y-axis labels
plt.xlabel('Max Temp')
plt.ylabel('Frequency')

#%% This section creates an ojive of the max temperature

# create a new figure
plt.figure()
# define the bin width
bin_width = 10
# define the bins to be integers from 0 to 100 (by 5)
bins = range(0,100+bin_width,bin_width)
# count the frequencies in each bin by summing values >= lower bound and < upper bound
frequencies = [sum(np.logical_and(maxTemp>=i, maxTemp<i+bin_width)) for i in bins]
# use the plot function to plot the cumulative frequencies
plt.plot(bins, np.cumsum(frequencies), 'o-')
# set the x-axis and y-axis labels
plt.xlabel('Max Temp')
plt.ylabel('Cumulative Frequency')
# set the x-axis and y-axis limits to 0 and 100 and 0 and 400, respectively
plt.xlim([0,100])
plt.ylim([0,400])
# create a second axis, sharing the original x-axis
ax2 = plt.twinx()
# set the second axis y-axis label
ax2.set_ylabel('Cumulative Relative Frequency')
# set the second axis y-axis limits to 0 and 400/365
ax2.set_ylim([0,400/365.])

#%% This section creates a Pareto chart for the conditions

# create a new figure
plt.figure()
# define the categories as a list of integers 0, 1, 2
categories = range(3)
# count the frequency of each condition equal to the category values
frequencies = [sum(conditions==i) for i in categories]
# use the bar function to plot the histogram of condition frequencies
plt.bar(categories, frequencies, align='center')
# set the x-axis label and ticks to show the conditions
plt.xlabel('Condition')
plt.xticks(categories, ['Clear', 'Rain', 'Snow'])
# set the y-axis label
plt.ylabel('Frequency')
# set the y-axis limits to 0 and 400
plt.ylim([0,400])
# create a second axis, sharing the original x-axis
ax2 = plt.twinx()
# use the plot function to plot the cumulative relative frequencies as a line
# note: cast number of days to a float to avoid integer round-off
ax2.plot(categories, np.cumsum(frequencies)/float(numDays), 'o-')
# set the y-axis label and limits to 0 and 400/365
ax2.set_ylabel('Fraction')
ax2.set_ylim([0,400/365.])

#%% This section creates a scatter plot of the max and min temperature

# create a new figure
plt.figure()
# use the plot function to plot the max and min temps with marks (no lines)
plt.plot(maxTemp, minTemp, 'o')
# set the x-axis and y-axis labels
plt.xlabel('Max Temp')
plt.ylabel('Min Temp')
# set the x-axis and y-axis limits to 0 and 100
plt.xlim([0,100])
plt.ylim([0,100])
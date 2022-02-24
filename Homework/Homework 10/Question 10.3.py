'''
Rushabh Barbhaya
CWID 10427219
Date: 4/19/2018

ASSIGNMENT 10
'''

import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt 

Value_Labels = np.array(['0','1','2','3','4','5','6','7','8'])
Count_Values = np.array([2,4,4,9,6,6,3,1,1])

Labels = np.array(['0-1','2','3','4','5','6-8'])
Values = np.array([6,4,9,6,6,5])

pmf = np.array([6./36,4./36,9./36,6./36,6./36,5./36])

expected = pmf * np.sum(Values)

chi2, p = stats.chisquare(Values, expected, ddof=1)

print 'chi2 = {:.2f}, p = {:.2f}'.format(chi2, p)
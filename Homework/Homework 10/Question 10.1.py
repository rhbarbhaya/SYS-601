'''
Rushabh Barbhaya
CWID 10427219
Date: 4/19/2018

ASSIGNMENT 10
'''

import numpy as np 
import scipy.stats as stats

#Question 10.1(a)
Ins_Eval = np.array(['Good','Excellent','Good','Good','Excellent','Excellent','Good','Good','Good','Excellent','Excellent','Excellent','Excellent','Excellent','Excellent','Good','Good','Excellent','Good','Good','Excellent','Excellent','Excellent','Excellent','Excellent','Excellent','Fair','Excellent','Excellent','Excellent','Excellent','Excellent','Excellent','Excellent','Excellent','Excellent','Poor','Excellent','Excellent','Excellent',])
Ins_Num = np.array([2,3,2,2,3,3,2,2,2,3,3,3,3,3,3,2,2,3,2,2,3,3,3,3,3,3,1,3,3,3,3,3,3,3,3,3,0,3,3,3])

Ins_Ranks = stats.rankdata(Ins_Num)

Cou_Eval = np.array(['Good','Fair','Fair','Poor','Good','Good','Poor','Good','Poor','Good','Good','Good','Good','Good','Poor','Good','Good','Good','Good','Good','Good','Good','Good','Excellent','Good','Excellent','Poor','Good','Excellent','Good','Excellent','Excellent','Good','Excellent','Good','Good','Poor','Good','Good','Good'])
Cou_Num = np.array([2,1,1,0,2,2,0,2,0,2,2,2,2,2,0,2,2,2,2,2,2,2,2,3,2,3,0,2,3,2,3,3,2,3,2,2,0,2,2,2])

Ins_Ranks = stats.rankdata(Ins_Num)
Cou_Ranks = stats.rankdata(Cou_Num)

r, p1 = stats.spearmanr(Ins_Num, Cou_Num)
print 'Solution 10.1(a)'
print 'r = {:.4f},p1 = {:.4f}'.format(r, p1)
print

#-------------------------------------------------------------------------------


#Question 10.1(b)
Calcu = ([2,3,2,2,3,3,2,2,2,3,3,3,3,3,3,2,2,3,2,2])
Thermo = ([3,3,3,3,3,3,1,3,3,3,3,3,3,3,3,3,0,3,3,3])
U, p2 = stats.mannwhitneyu(Calcu, Thermo)
print 'Solution 10.1(b)'
print 'U = {:.4f}, p2 = {:.4f}'.format(U, p2)
print

#-------------------------------------------------------------------------------


#Question 10.1(c)
T, p3 = stats.wilcoxon(Calcu, Thermo)
print 'Solution 10.1(c)'
print 'T = {:.2f}, p3 = {:.4f}'.format(T, p3)
print

#-------------------------------------------------------------------------------
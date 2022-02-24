'''
Rushabh Barbhaya
CWID 10427219
Date: 4/19/2018

ASSIGNMENT 10
'''

import numpy as np 
import scipy.stats as stats

P1 = np.array([
	[512, 89],
	[313, 19]
	])
chi2, p1, dof, expected = stats.chi2_contingency(P1)
print 'P1-->	chi2 = {:.2f}, p = {:.6f}'.format(chi2, p1)

P2 = np.array([
	[313, 17],
	[207,  8]
	])
chi2, p2, dof, expected = stats.chi2_contingency(P2)
print 'P2-->	chi2 = {:.2f}, p = {:.2f}'.format(chi2, p2)

P3 = np.array([
	[120,202],
	[205,391]
	])
chi2, p3, dof, expected = stats.chi2_contingency(P3)
print 'P3-->	chi2 = {:.2f}, p = {:.2f}'.format(chi2, p3)

P4 = np.array([
	[138,131],
	[279,244]
	])
chi2, p4, dof, expected = stats.chi2_contingency(P4)
print 'P4-->	chi2 = {:.2f}, p = {:.2f}'.format(chi2, p4)

P5 = np.array([
	[ 53, 94],
	[138,299]
	])
chi2, p5, dof, expected = stats.chi2_contingency(P5)
print 'P5-->	chi2 = {:.2f}, p = {:.2f}'.format(chi2, p5)

P6 = np.array([
	[ 22, 24],
	[351,317]
	])
chi2, p6, dof, expected = stats.chi2_contingency(P6)
print 'P6-->	chi2 = {:.2f}, p = {:.2f}'.format(chi2, p6)
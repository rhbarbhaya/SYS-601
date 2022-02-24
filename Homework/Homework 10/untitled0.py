# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:13:27 2018

@author: rhbar
"""

import numpy as np 
import scipy.stats as stats

#labels = np.array(['Male_Accepted','Male_Denied','Female_Accepted','Female_Denied'])

P1 = np.array([[512,89],
[313,19]])
#P1_pmf = np.array([512./933,89./933])
#P1_exp = P1_pmf * np.sum(P1)
chi2, p1, dof, expected = stats.chi2_contingency(P1)
print 'P1-->	chi2 = {:.2f}, p = {:.2f}'.format(chi2, p1)
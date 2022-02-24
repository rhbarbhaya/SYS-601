# -*- coding: utf-8 -*-
"""

@author: sukit
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

observed = np.array( [3, 6, 4, 6, 2, 3, 1, 5, 1, 0, 3, 3,
                    1, 2, 4, 0, 2, 6, 5, 4, 2, 5, 3, 4,
                    5, 3, 5, 3, 5, 4, 7, 3, 4, 8, 1, 3])
plt.figure()
plt.hist(observed, range(0,10,2), color='r')
plt.xlabel('Number of customers arriving')
plt.ylabel('Frequency')

labels = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
ob_frequency = np.array( [2, 4, 4, 9, 6, 6, 3, 1, 1] )

lamb = np.sum( labels * ob_frequency)/np.sum(ob_frequency)

pmf = stats.poisson.pmf(labels, lamb)
expected_value = np.sum(ob_frequency) * pmf

chi2, p = stats.chisquare(ob_frequency, expected_value, ddof=1)

print 'chi2 = {:.3f}, p = {:.3f}'.format(chi2,p)


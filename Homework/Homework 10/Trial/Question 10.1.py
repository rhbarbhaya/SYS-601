import numpy as np 
import scipy.stats as stats

#Ins_Eval = np.array(['Good','Excellent','Good','Good','Excellent','Excellent','Good','Good','Good','Excellent','Excellent','Excellent','Excellent','Excellent','Excellent','Good','Good','Excellent','Good','Good','Excellent','Excellent','Excellent','Excellent','Excellent','Excellent','Fair','Excellent','Excellent','Excellent','Excellent','Excellent','Excellent','Excellent','Excellent','Excellent','Poor','Excellent','Excellent','Excellent',])
Ins_Num = np.array([2,3,2,2,3,3,2,2,2,3,3,3,3,3,3,2,2,3,2,2,3,3,3,3,3,3,1,3,3,3,3,3,3,3,3,0,3,3,3])

Ins_Ranks = stats.rankdata(Ins_Num)

#Cou_Eval = np.array(['Good','Fair','Fair','Poor','Good','Good','Poor','Good','Poor','Good','Good','Good','Good','Good','Poor','Good','Good','Good','Good','Good','Good','Good','Good','Excellent','Good','Excellent','Poor','Good','Excellent','Good','Excellent','Excellent','Good','Excellent','Good','Good','Poor','Good','Good','Good'])
Cou_Num = np.array([2,1,1,0,2,2,0,2,0,2,2,2,2,2,0,2,2,2,2,2,2,2,2,3,2,3,0,2,3,2,3,3,2,3,2,2,0,2,2])

r_s, p = stats.spearmanr(Ins_Num, Cou_Num)

print ('r_s = {:.3f}'.format(r_s))
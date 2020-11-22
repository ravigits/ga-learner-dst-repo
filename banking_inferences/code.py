# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here

# Sample creation
data_sample = data.sample(n=sample_size, random_state=0)

# confidence_interval

mean = data_sample.installment.mean()
std = data_sample.installment.std()
margin_of_error = std/np.sqrt(sample_size)

true_mean = data.installment.mean()

confidence_interval = [round(mean - z_critical * margin_of_error, 2), round(mean + z_critical * margin_of_error, 2)]

print('confidence_interval is ', confidence_interval)

# central limit theorem

sizes = [20, 50, 100]

# small business interests

x1 = data[data.purpose == 'small_business']['int.rate'].str.replace('%','').astype(float)
values1 = data['int.rate'].str.replace('%','').astype(float).mean()

z_statistic_1, p_value_1 = ztest(x1, value=values1, alternative='larger')

print ('z_statistic1 is ', z_statistic_1)
print('p_value1 is ', p_value_1)

# Installment vs Loan Defaulting

x2 = data[data['paid.back.loan'] == 'No']['installment']
x1 = data[data['paid.back.loan'] == 'Yes']['installment']

z_statistic_2, p_value_2  = ztest(x2, x1)

print ('z_statistic2 is ', z_statistic_2)
print('p_value2 is ', p_value_2)

# purpose vs loan defaulting

not_paid = data_sample[data_sample['paid.back.loan'] == 'No']['purpose'].value_counts()
paid = data_sample[data_sample['paid.back.loan'] == 'Yes']['purpose'].value_counts()

observed = pd.crosstab(paid, not_paid)

chi2, p, dof, ex = stats.chi2_contingency(observed)

print("Chi-square statistic = ",chi2)
print("p-value = ",p)

if chi2 > p:
    print('Two distributions are not same. Null hypothesis is rejected')
else:
    print('Two distributions are same')





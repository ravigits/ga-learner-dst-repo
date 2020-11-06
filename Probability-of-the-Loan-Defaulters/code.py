# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here

# Task 1
p_a = len(df[df.fico> 700])/len(df)

p_b = len(df[df.purpose == 'debt_consolidation'])/len(df)

df1 = df[df.purpose == 'debt_consolidation']

p_a_inv_b = len(df[(df.purpose == 'debt_consolidation') & (df.fico> 700)])/len(df)

p_a_b = p_a_inv_b/p_a
result = (p_a_b == p_a)
print('Is P(B|A) == P(A) equal ', result)

# Task 2

prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/len(df)

prob_cs = len(df[df['credit.policy'] == 'Yes'])/len(df)

new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df)

bayes = round((prob_pd_cs * prob_lp)/prob_cs, 4)

print('Bayes theorem value ', bayes)

# Task 3

plt.figure(figsize=(10,7))

plt.subplot(1,2,1)

df.purpose.value_counts().plot.barh()

df1 = df[df['paid.back.loan'] == 'No']

print(df1.shape)

plt.subplot(1,2,2)

df1.purpose.value_counts().plot.barh()

plt.show()

# Task 4

inst_median = df.installment.median()

inst_mean = df.installment.mean()

plt.figure(figsize=(10,7))

plt.subplot(1,2,1)

df.installment.plot.hist()

plt.subplot(1,2,2)

df['log.annual.inc'].plot.hist()

plt.show()



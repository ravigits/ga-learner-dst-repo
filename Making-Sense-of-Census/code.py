# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate((data, new_record))

# Step 2

age = census[:,0]

max_age = age.max()
min_age = age.min()
age_mean = np.mean(age)
age_std = np.std(age)

# Step 3

race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
min_len = min(len_0, len_1, len_2, len_3, len_4)
if  min_len== len_0:
    minority_race = 0
elif min_len== len_1:
    minority_race = 1
elif min_len== len_2:
    minority_race = 2
elif min_len== len_3:
    minority_race = 3
else:
    minority_race = 4

print('Minority race number is ', minority_race)

# Step 4
senior_citizens = census[census[:,0]>60]
working_hours_sum = senior_citizens[:,6].sum()
senior_citizens_len = len(senior_citizens)
avg_working_hours = round(working_hours_sum / senior_citizens_len, 2)
print('Working hours sum for senior citizens is ',working_hours_sum)
print('Average working hours for senior citizens is ',avg_working_hours)

# Step 5
high = census[census[:,1]>10]
low = census[census[:,1]<=10]

avg_pay_high = round(np.mean(high[:,7]),2)
avg_pay_low = round(np.mean(low[:,7]), 2)

if avg_pay_high > avg_pay_low:
    print('Average pay is higher for people with higher education. Mean is ', avg_pay_high)
else:
    print('Average pay is higher for people with lower education. Mean is ', avg_pay_low)



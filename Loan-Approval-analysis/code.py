# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
categorical_var = bank_data.select_dtypes(include='object')
print(categorical_var.shape)


numerical_var = bank_data.select_dtypes(include='number')
print(numerical_var.shape)
numerical_var.head()
categorical_var.head()

banks = bank_data.drop('Loan_ID', axis=1)


bank_mode = banks.mode()
print(bank_mode['Gender'][0])
for col in banks.columns:
    banks[col] = banks[col].fillna(bank_mode[col][0])
print(banks.isnull().sum())

avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount', aggfunc='mean')

print(avg_loan_amount)

loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].count()

loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].count()

percentage_se = loan_approved_se/banks['Loan_Status'].count()*100
percentage_nse = loan_approved_nse/banks['Loan_Status'].count()*100

print(percentage_nse)
print(percentage_se)

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)

big_loan_term = loan_term[loan_term >= 25.0].count()
print(big_loan_term)

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]
mean_values = round(loan_groupby.mean(),2)
print(mean_values.iloc[1,0])



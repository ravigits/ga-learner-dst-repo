# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here
data['Gender'] = data['Gender'].replace('-','')

data['Alignment'].value_counts().plot.pie()

qtl = data['Total'].quantile(0.99)

super_best_names  = list(data[data['Total'] > qtl]['Name'])
print(super_best_names )



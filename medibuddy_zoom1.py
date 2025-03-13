# -*- coding: utf-8 -*-
"""medibuddy_zoom1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lnsTekentKWFYl5Vw0VQ3avB8bZcnuXD

Import libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""Import dataset"""

df1 = pd.read_csv('/content/Price.csv')
df2= pd.read_csv('/content/personal.csv')

df1.keys()

df2.keys()

"""merge dataset"""

data = pd.merge(df1,df2,on='Policy no.')

data.keys()

data.rename(columns={'Policy no.':'Policy_no','sex':'gender','charges in INR':'Charges'},inplace=True)

data.dtypes

"""check for null and duplicates"""

data.duplicated().sum()

data.isna().sum()

"""
# Does the gender of the person matter for the company as a constraint for
# extending policies?
"""

gender_charges = data.groupby('gender')['Charges'].mean()
gender_charges

"""Plot the graph"""

plt.figure(figsize=(10,6))
sns.barplot(x=gender_charges.index,y=gender_charges.values)
plt.show()

"""# What is the average amount of money the company spent over each policycover?

"""

avg_amount = data['Charges'].mean()
avg_amount

"""plot histogram"""

plt.figure(figsize=(8,5))
sns.histplot(data=data,x=data['Charges'])

"""
# Could you advice if the company needs to offer separate policies based upon the geographic location of the person?
"""

location_charges = data.groupby('region')['Charges'].mean().sort_values(ascending=False)
location_charges

data.keys()

"""plot the bar"""

plt.figure(figsize=(10,6))
sns.barplot(x=location_charges.index,y=location_charges.values)

"""# Does the no. of dependents make a difference in the amount claimed?

"""

children_charges= data.groupby('children')['Charges'].mean().sort_values(ascending=False)
children_charges

data.keys()

"""Plot the graph"""

plt.figure(figsize=(10,6))
sns.barplot(x=children_charges.index,y=children_charges.values)
plt.show()

"""# Does a study of persons BMI get the company any idea for the insurance claim  that it would extend?"""

bmi_charges = data.groupby('bmi_group')['Charges'].mean().sort_values(ascending=False)
bmi_charges

data['bmi_group']=pd.cut(data['bmi'],bins=[15,18,24,30,36,42,48,54,float('inf')],labels=['minimum','very low','low','normal','medium','high','above high','maximum'])

"""plot scatterplot with hue"""

plt.figure(figsize=(10,6))
sns.scatterplot(data=data,x='bmi_group',y='Charges',hue='smoker')



"""# Is it needed for the company to understand whether the person covered is a smoker or a non-smoker?

"""

smoker_charges = data.groupby('smoker')['Charges'].mean().sort_values(ascending=False)
smoker_charges

"""Plot graph"""

plt.figure(figsize=(10,6))
sns.barplot(x=smoker_charges.index,y=smoker_charges.values)
plt.show()

"""# Is it needed for the company to understand whether the person covered is a smoker or a non-smoker?"""

bmi_charges1 = data.groupby('bmi')['Charges'].mean().sort_values(ascending=False)
bmi_charges1

"""Plot graph"""

plt.figure(figsize=(10,6))
sns.scatterplot(x='bmi',y='Charges',hue='smoker',data=data)

"""#Does age have any barrier on the insurance claimed?"""

data['age'].unique()

data['age_group']=pd.cut(data['age'],bins=[18,25,30,35,40,50,62,float('inf')],labels=['teen','very young','young','adult','middle','old','very-old'])

age_charges = data.groupby('age_group')['Charges'].mean().sort_values(ascending=False)
age_charges

"""Plot graph"""

plt.figure(figsize=(10,6))
sns.scatterplot(data=data, x='age_group',y='Charges',hue='smoker')

"""#Can the company extend certain discounts after checking the health status (BMI) in this case?"""



data.keys()

"""plot graph"""


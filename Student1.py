import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("C:/Users/ASUS/Downloads/StudentsPerformance.csv")
print(data.head(5))
print(data.tail(5))
print(data.shape)
print(data.size)
print(data.ndim)
print(data.describe())
print(data.columns)
print(data.nunique())
print(data.isnull().sum())
d=data.drop(['parental level of education','lunch'],axis=1)
print(d.head(5))
corelation=d.corr()
sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns, annot=True)
sns.pairplot(d)
sns.relplot(x='reading score', y='writing score', hue='gender', data=d)
sns.distplot(d['reading score'])






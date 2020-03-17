import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

data=pd.read_csv(R'C:\Users\jayesh\PycharmProjects\untitled3\bigmart.csv')
# print(data.head())
print(data.isnull().sum())
print(data.shape)
print(data.nunique())
corrmat=data.corr()
f,ax=plt.subplot(figsize=(12,11)
sns.heatmap(corrmat,ax=ax,cmap="YlGnBu",linewidths=0.1)


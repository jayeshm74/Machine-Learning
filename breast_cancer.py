import pandas as pd
import numpy as np
data=pd.read_csv('breast cancer.csv')
print(data.head())
X=data.drop('diagnosis',axis=1)
Y=data['diagnosis']
print(Y)
print(X)
print(data.count())
print(data.isnull().sum())
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
Y=encoder.fit_transform(Y)
print(Y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y, test_size=0.25)
print(x_test)
from sklearn.preprocessing import StandardScaler
sd=StandardScaler()
x_train=sd.fit_transform(x_train)
x_test=sd.transform(x_test)
print(data.isnull().sum())
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix
lm=LinearRegression()
lm.fit(x_train,y_train)
prediction=lm.predict(x_test)
print(prediction)




import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data=pd.read_csv('BostonHousing.csv')
print(data.head())
target=data['medv']
features=data.drop('medv',axis=1)
print(target.head())
print(features.head())
print(target.mean)
x_train,x_test,y_train,y_test=train_test_split(target,features,test_size=0.3 )
print(x_test,x_train)
#  Linear_regression
# lin=LinearRegression()
# lin.fit(x_train,y_train)
# prediction=lin.predict(x_test)
# print(prediction)

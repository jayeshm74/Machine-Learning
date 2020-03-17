import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
data=pd.read_csv('iris.csv')
print(data.head())
print(data.info())
data['class']=data['species'].map({'setosa':0,'versicolor':1,'virginica':2}).astype(int)
print(data.shape)
print(data.ndim)
print(data.head())
X=data.iloc[:,0:4]
Y=data['class']
print(X.head())
print(Y.head())
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3)

# decission tree
dt=DecisionTreeClassifier()
dt.fit(x_train,y_train)
prediction=dt.predict(x_test)
print(prediction)

3

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
data=pd.read_csv(r'Loan_data.csv')
# print(data.head())
# print(data.shape)
# print(data.ndim)
data.dropna(inplace=True)
# print(data.shape)
# print(data.columns)
data.drop(['Loan_ID'],axis=1,inplace=True)
print(data.head())
print(data['Loan_Status'].value_counts())
print(data.nunique())
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data['Loan_Status']=le.fit_transform(data['Loan_Status'])
# print(data.head())
le=LabelEncoder()
data['Gender']=le.fit_transform(data['Gender'])
le=LabelEncoder()
data['Married']=le.fit_transform(data['Married'])
le=LabelEncoder()
data['Education']=le.fit_transform(data['Education'])
le=LabelEncoder()
data['Self_Employed']=le.fit_transform(data['Self_Employed'])
le=LabelEncoder()
data['Credit_History']=le.fit_transform(data['Credit_History'])
le=LabelEncoder()
data['Property_Area']=le.fit_transform(data['Property_Area'])
le=LabelEncoder()
data['Dependents']=le.fit_transform(data['Dependents'])
print(data.head())
x=data.drop(['Loan_Status'],axis=1)
y=data['Loan_Status']
sns.countplot(data['Loan_Status'],label='count')
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
# print(x_train)
from sklearn.linear_model import LogisticRegression
le=LogisticRegression()
le.fit(x_train,y_train)
prediction=le.predict(x_test)
print(prediction)
print(accuracy_score(y_test,prediction))
# print(y_train.head())
from sklearn.tree import DecisionTreeClassifier
dc=DecisionTreeClassifier()
dc.fit(x_train,y_train)
prediction=dc.predict(x_test)
print(prediction)
print(accuracy_score(y_test,prediction))

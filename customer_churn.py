import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import rcParams
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
data=pd.read_csv('customer_churn.csv')
# print(data.head())
# print(data.shape)
# print(data.isnull())
print(data.groupby('Churn').size())
data.drop(['customerID','gender'],axis=1,inplace=True)
# print(data.shape)
print(data.nunique())
print(data.dtypes)
print(data.columns)
# x=data.drop(['Churn'],axis=1)
# y=data['Churn']
# print(data.info())
# print(data.columns)
le=LabelEncoder()
data['Churn']=le.fit_transform(data['Churn'])
le=LabelEncoder()
data['SeniorCitizen']=le.fit_transform(data['SeniorCitizen'])
le=LabelEncoder()
data['MultipleLines',]=le.fit_transform(data['MultipleLines'])
le=LabelEncoder()
data['Partner']=le.fit_transform(data['Partner'])
le=LabelEncoder()
data['Dependents']=le.fit_transform(data['Dependents'])
le=LabelEncoder()
data['PhoneService']=le.fit_transform(data['PhoneService'])
le=LabelEncoder()
data['PaperlessBilling']=le.fit_transform(data['PaperlessBilling'])
le=LabelEncoder()
data['InternetService']=le.fit_transform(data['InternetService'])
le=LabelEncoder()
data['OnlineSecurity']=le.fit_transform(data['OnlineSecurity'])
le=LabelEncoder()
data['OnlineBackup']=le.fit_transform(data['OnlineBackup'])
le=LabelEncoder()
data['DeviceProtection']=le.fit_transform(data['DeviceProtection'])
le=LabelEncoder()
data['TechSupport']=le.fit_transform(data['TechSupport'])
le=LabelEncoder()
data['StreamingTV']=le.fit_transform(data['StreamingTV'])
le=LabelEncoder()
data['StreamingMovies']=le.fit_transform(data['StreamingMovies'])
le=LabelEncoder()
data['Contract']=le.fit_transform(data['Contract'])
le=LabelEncoder()
data['PaymentMethod']=le.fit_transform(data['PaymentMethod'])
print(data.head())
x=data.drop(['Churn'],axis=1)
y=data['Churn']
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.3)
print(x_train.head(),x_test.head(),y_train.head(),y_test.head())
lr=LogisticRegression()
lr.fit(x_train,y_train)
prediction=lr.predict(x_test)
print(prediction)

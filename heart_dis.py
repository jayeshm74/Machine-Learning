import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
data=pd.read_csv('framingham.csv')
print(data.head())
data.drop(['education'],axis=1,inplace=True)
print(data.head())
print(data.shape)
data.rename(columns={'male':'sex_male'},inplace=True)
print(data.tail())
print(data.isnull().sum().head())
count=0
# doubt
for i in data.isnull().sum(axis=1):
    if i>0:
        count=count+1
    print(count)
data.dropna(axis=0,inplace=True)
print(data)
X=data.drop('TenYearCHD',axis=1)
Y=data.iloc[:,14]
print(Y)
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)
print(x_train.shape,y_train.shape)
print(x_test.shape,y_test.shape)
# fit model
lm=LogisticRegression()
lm.fit(x_train,y_train)
prediction=lm.predict(x_test)

print(prediction)

# lr=LogisticRegression()

# pred=lr.predict('X')
# print(pred)


from sklearn.metrics import accuracy_score
acc  = accuracy_score(y_test, prediction)
print('Accuracy for Logistic Regression: ', acc)



import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,prediction)
conf_matrix=pd.DataFrame(data=cm,columns=['Predicted:0','Predicted:1'],index=['Actual:0','Actual:1'])
plt.figure(figsize = (8,5))
sn.heatmap(conf_matrix, annot=True,fmt='d',cmap="YlGnBu")


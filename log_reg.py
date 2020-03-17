import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
data=pd.read_csv('log_regression.csv')
data.head()
Y=data['Y']
X=data.drop('X1',axis=1)
print(Y)

logisticRegr = LogisticRegression()
logisticRegr.fit(X, Y)
a=[[85]]
pred=logisticRegr.predict(a)
print(pred)


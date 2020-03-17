import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
data=pd.read_csv('regression.csv')
Y=data['Y']
X=data.drop('Y',axis=1)
lr=LinearRegression()
lr.fit(X,Y)
pred=lr.predict([[95]])
print(pred)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('regression.csv')
print(data)
x=data.iloc[:,0]
y=data.iloc[:,1]
mx=data['X1'].mean()
my=data['Y'].mean()
print(mx,my)

num, den = 0,0
for i in range(len(x)):
    num += (x[i] - mx)*(y[i]-my)
    den += (x[i]-mx)**2
beta1 = num/den
beta0 =my-(beta1*mx)
print(beta1,beta0)
Y_predict=beta1*x + beta0
plt.scatter(x,y)

plt.plot([min(x),max(x)],[min(Y_predict),max(Y_predict)], color='red')
plt.show()

ycap = []
for i in range(len(x)):
    xdata =( beta1*x[i])+ beta0
    ycap.append(xdata)
print(ycap)
residue=[]
for i in range(len(y)):
    l = y[i] - ycap[i]
    residue.append(l)
print(residue)
residualsum=sum(residue)
print(residualsum)




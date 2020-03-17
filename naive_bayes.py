import pandas as pd
predict=pd.read_csv('weathers.csv')
print(predict)
target=pd.read_csv(r'C:\Users\jayesh\PycharmProjects\untitled3\freq_table1.csv')
print(target)
sdata=target[target["weather"]=='S']
print(sdata)
totalsunny= sdata['Y']+sdata['N']
print(totalsunny)
ydata=target["Y"]
print(ydata)
sum=(sum(ydata))
print(sum)
tdata=predict['play'].count()
print(tdata)
pdata=sum/tdata
print(pdata)
print(totalsunny)
print(tdata)
mdata=totalsunny/tdata
print(mdata)
ysunny=sdata['Y']
print(ysunny)
fdata=ysunny/sum
print(fdata)
playdata=fdata*pdata/mdata
print(playdata)

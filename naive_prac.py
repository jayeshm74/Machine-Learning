import pandas as pd
target=pd.read_csv('weathers.csv')
print(target)
freq=pd.read_csv(r'C:\Users\jayesh\PycharmProjects\untitled3\freq_table1.csv')
print(freq)
tdata=freq['Y']
print(tdata)

# adata=freq[freq['weather']=='S']
# print(adata)
# total_sunny=adata['Y']+adata['N']
# print(total_sunny)
# bdata=freq['Y']
# print(bdata)
# cdata=sum(bdata)
# print(cdata)
# ddata=target['play'].count()
# print(ddata)
# edata=cdata/ddata
# print(edata)
# fdata=total_sunny/ddata
# print(fdata)
# gdata=adata['Y']
# print(gdata)
# hdata=gdata/cdata
# print(hdata)
# jdata=hdata*edata/fdata
# print(jdata)

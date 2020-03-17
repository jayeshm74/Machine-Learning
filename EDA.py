import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('telecom_churn.csv')
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
df['Churn']=df['Churn'].astype('int64')
print(df.head())
print(df.describe())
df.describe(include=['object','bool'])
print(df.head())
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=False))
print(df['Churn'].value_counts())
print(df.sort_values(by='Total day charge', ascending=False).head())
print(df.sort_values(by=['Churn', 'Total day charge'],
        ascending=[True, False]).head())
print(df['Churn'].mean())
print(df[df['Churn']==1].mean())
print(df[df['Churn'] == 1]['Total day minutes'].mean())
print(df[(df['Churn'] == 0) & (df['International plan'] == 'No')]['Total intl minutes'].max())
print(df.loc[0:5, 'State':'Area code'])
print(df.iloc[0:5, 0:3])
print(df[-1:])
print(df.apply(np.max))
print(df[df['State'].apply(lambda state: state[0] == 'W')].head())
d = {'No' : False, 'Yes' : True}
df['International plan'] = df['International plan'].map(d)
print(df.head())
df = df.replace({'Voice mail plan': d})
print(df.head())
columns_to_show = ['Total day minutes', 'Total eve minutes',
                   'Total night minutes']

print(df.groupby(['Churn'])[columns_to_show].describe(percentiles=[]))
print(pd.crosstab(df['Churn'], df['International plan']))
print(pd.crosstab(df['Churn'], df['Voice mail plan'], normalize=True))
print(df.pivot_table(['Total day calls', 'Total eve calls', 'Total night calls'],
               ['Area code'], aggfunc='mean'))
total_calls = df['Total day calls'] + df['Total eve calls'] + \
              df['Total night calls'] + df['Total intl calls']
df.insert(loc=len(df.columns), column='Total calls', value=total_calls)
# loc parameter is the number of columns after which to insert the Series object
# we set it to len(df.columns) to paste it at the very end of the dataframe
print(df.head())
df['Total charge'] = df['Total day charge'] + df['Total eve charge'] + df['Total night charge'] + df['Total intl charge']
print(df.head())
# get rid of just created columns
df.drop(['Total charge', 'Total calls'], axis=1, inplace=True)
# and here’s how you can delete rows
print(df.drop([1, 2]).head())
sns.countplot(x='International plan', hue='Churn', data=df);









import pandas as pd
review=pd.read_csv('ign.csv')
print(review.head())
print(review.tail())
print(review.shape)
print(review.iloc[0:5,:])
review=review.iloc[:,1:]
print(review.head())
review=review.iloc[:,1:]
print(review.head())
review.loc[0:5,:]
print(review.head())
review.index
print(review.head())
some_review=review.iloc[10:20,]
print(some_review.head())
review=review.loc[:5,'score']
print(review)



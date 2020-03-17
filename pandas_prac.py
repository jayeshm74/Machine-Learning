import pandas as pd
import numpy as np
import matplotlib as mp
review=pd.read_csv('ign.csv')
print(review)
print(review.head())
print(review.tail())
print(review.shape)
print(review.iloc[0:6,:])
print(review.iloc[9,:])
print(review.iloc[0:,2:])
print(review.loc[0:5,:])
review.index
print(review)
some_review=review.iloc[10:20,:]
print(some_review.head())
print(some_review.loc[9:21,:])
print(review.loc[0:,'score'])
print(review.loc[0:10,['score','release_year']])
print(review['score'])
print(review[['score','release_year','release_month']])
# print(type(review['score']))
# s1=pd.series(["Boris Yeltsin", "Mikhail Gorbachev"])
# print(s1)
# print(pd.DataFrame([s1,s2]))
# tilt=review['title'].head()
# print(tilt)
print(review["title"].head())
print(review['score'].mean())
print(review.mean())
print(review.mean(axis=1))
print(review.corr())
print(review.median)
print(review['score']/2)
# print(review['score']<7)
score_filter=review['score']<7
print(score_filter)
filtered_reviews = review[score_filter]
print(filtered_reviews.head())
xbox_review=(review['score']<7)&(review['platform']=="xbox one")
print(xbox_review.head())
print(review[review['platform']=='xbox one']['score'].plot(kind='hist'))













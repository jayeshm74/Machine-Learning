import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
diabetes=pd.read_csv('diabetes.csv')
print(diabetes.head())
print(diabetes.shape)
print(diabetes.dtypes)
print(diabetes.isnull())
print(diabetes.nunique())
print(diabetes.columns)
print(diabetes.info())
print(diabetes.groupby('Outcome').size())
import seaborn as sns
# sns.countplot(diabetes['Outcome'],label='count')

x=diabetes.drop(['Outcome'],axis=1)
y=diabetes['Outcome']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
training_accuracy=[]
test_accuracy=[]
for i in range(1,11):

    knn=KNeighborsClassifier(n_neighbors=i)

    print(len(x_train))

    knn.fit(x_train,y_train)
    training_accuracy.append(knn.score(x_train,y_train))
    test_accuracy.append(knn.score(x_test,y_test))






print(training_accuracy,len(training_accuracy))
print(test_accuracy,len(test_accuracy))


l=[1,2,3,4,5,6,7,8,9,10]

plt.plot(l, training_accuracy, label="training accuracy")
plt.plot(l, test_accuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.show()
plt.savefig('knn_compare_model')
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression().fit(x_train, y_train)
print("Training set accuracy: {:.3f}".format(logreg.score(x_train, y_train)))
print("Test set accuracy: {:.3f}".format(logreg.score(x_test, y_test)))




import pandas
student={'Name':['jayesh','hitesh','atul','rakesh'],
         'class':['python','java','c','c++'],
          'city':['mumbai','delhi','chennai','kolkata'],
           'age':[1,2,3,4]}
data=pandas.DataFrame(student)
print(type(data))
print(data.columns.values)
print(data.ndim)
# to print the shape of data
print(data.shape)
print(data.describe())
print(data.count())
print(data[data['Name']=='jayesh'])
print(data[data['age']>2])




import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

cols = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']


dataset = pandas.read_csv(url, names=cols)

print(dataset)

# top 5 rows
print(dataset.head())

print(dataset.head(10))

#last
print(dataset.tail())
print(dataset.tail(6))

#show cols
print(dataset.columns)

#dimenssion
print(dataset.shape)


#read one column
print(dataset['class'])

data = dataset.values #convert dataframe to list
print(data[:,1])
print(data[:,1:3])


print(data[10:20,1:3])

#show stats
print(dataset.describe())

#classification : group by  : distribuation
print(dataset.groupby('class').size())
print(dataset.groupby('class').max())
print(dataset.groupby('class').min())
print(dataset.groupby('class').sum())

#search data / filter
out = dataset.loc[dataset['petal-width'] > 1.0 ]
print(out)

out = out.loc[dataset['sepal-length']<4.3]
print(out)


#visualiation / graph

#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
#dataset.plot(kind='line', subplots=True, layout=(2,2), sharex=False, sharey=False)
#dataset.plot(kind='line')
#plt.show()

#dataset.hist()
#plt.show()

#scatter_matrix(dataset)
#plt.show()


# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]

validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation =model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

print(X_train)
print(X_validation)
print(Y_train)
print(Y_validation)









































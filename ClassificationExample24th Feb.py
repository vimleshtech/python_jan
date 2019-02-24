import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


fruits = pd.read_table(r'C:\Users\vkumar15\Desktop\Desktop - Raman\fruits_data.txt')
print(fruits.head())  #show from top , default 5 rows

print(fruits.shape)

#get unique list
print(fruits.groupby('fruit_name').size())


#sns.countplot(fruits['fruit_name'],label="Count")
#plt.show()

# 1 2 3 4 ..10

feature_names = ['mass', 'width', 'height', 'color_score']
X = fruits[feature_names]
Y = fruits['fruit_label']


print(X)
print(Y)


x_train,x_test,y_train,y_test= train_test_split(X, Y, random_state=2)

print(x_train)
print(x_test)
print(y_train)
print(y_test)



logreg = LogisticRegression()
out = logreg.fit(x_train, y_train)

print(logreg.score(x_train, y_train))

#print(out.summary())
#print(logreg.score(x_test, y_test))






















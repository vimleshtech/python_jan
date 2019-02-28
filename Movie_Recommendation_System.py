#library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

#load data
movie = pd.read_table(r'C:\Users\Tech Vision\Desktop\Python\python_project-master\python_project-master\Data\movies.dat',sep = "::", names = ['MovieID','Movie','Genre'])
rating = pd.read_table(r'C:\Users\Tech Vision\Desktop\Python\python_project-master\python_project-master\Data\ratings.dat',sep = "::", names = ['UserID', 'MovieID', 'Rating', 'TimeStamp'])
user = pd.read_table(r'C:\Users\Tech Vision\Desktop\Python\python_project-master\python_project-master\Data\users.dat',sep = "::", names = ['UserID', 'Gender', 'Age', 'Occupation', 'ZipCode'])


#check data 
print(user.head())
print(movie.head())
print(rating.head())

# JOIN THE 3 DATASETS
rm = rating.join(movie.set_index('MovieID'), on='MovieID', how='left', lsuffix='l').drop('TimeStamp', axis=1)
rum = rm.join(user.set_index('UserID'), on='UserID', how='left')
print(rum.head())


rum.isna().sum()     # NO NULL VALUES FOUND


print(user['UserID'].count())     #6040 UNIQUE USERS
print(movie['MovieID'].count())   #3883 UNIQUE MOVIES


# ADD "OCCUPATION TYPE" AND "ACTUAL AGE" COLUMNS (BY CREATING DICTIONARY)

dict = {'Occupation':[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 'OccupationType':['Other or not specified', 'Academic/Educator', 'Artist', 'Clerical/Admin', 'College/grad student', 'Customer service', 'Doctor/Health care', 'Executive/Managerial', 'Farmer', 'Homemaker', 'K-12 Student', 'Lawyer', 'Programmer', 'Retired', 'Sales/Marketing', 'Scientist', 'Self-Employed', 'Technician/Engineer', 'Tradesman/Craftsman', 'Unemployed', 'Writer']}
occ = pd.DataFrame(dict)
rum1 = rum.join(occ.set_index('Occupation'), on = 'Occupation', how = 'left')

dict = {'Age':[1, 18, 25, 35, 45, 50, 56], 'AgeGroup':['Under 18', '18-24', '25-34', '35-44', '45-49', '50-55', '56+']}
age = pd.DataFrame(dict)
rum2 = rum1.join(age.set_index('Age'), on = 'Age', how = 'left')
print(rum2.head(2))


a = rum2.groupby('Movie')['MovieID'].count().sort_values(ascending=False)

print(rum2.groupby('Gender')['Rating'].count())


print(rum2.groupby('Gender')['Rating'].mean())

#by age group 
#sns.barplot(x=rum2['AgeGroup'], y=rum2['Rating'])
#plt.show()


#by gender
sns.barplot(x=rum2['Gender'], y=rum2['Rating'])
plt.show()













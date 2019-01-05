import pandas as p

o = p.read_csv(r'C:\Users\vkumar15\Documents\Sandbox\UHG\bmi.csv')
print(o)


#show list of columns
print(o.columns)

#show particular column
print(o['height'])

#show top given no of rows
print(o.head(n=2))

#show buttom  given no of rows
print(o.tail(n=2))

#group / distibuation
print(o.groupby('gender').size())
print(o.groupby('gender').sum())
print(o.groupby('gender').max())
print(o.groupby('gender').min())

##describe : show basic stats
print(o.describe())


print(o.shape)










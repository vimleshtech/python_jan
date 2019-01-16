data = [1111,222,333344]

print('len  =',max(data))
print('min  = ',min(data))
print('max = ',sum(data))

data.sort()
print('sorted data  = ',data)

data.append(100) #add after last index
print(data)

data.pop() #remove from last
print(data)

data.insert(1,2223334)  # add new value at given position 
print(data) 

data.remove(222) # remove by value
print(data)

#remove by index
data.remove(data[1])
print(data)

##slicer
##dynamic list
dd = []

for x in range(1,5):
     d = input('enter data :')
     dd.append(d)


print(dd)

#traverse the list
for x in dd:
     print(x)

#or
for i in range(0,len(dd)):
     print(dd[i])






     



     







#


     
     









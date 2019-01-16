#while loop
i =1  # init 
while i<10: # condition
     
     #print(i) # print and change the line
     print(i,end='\t')  #pritn and don't change line 
     i = i+1 # incrementer
     

print('----for loop  ---- ')
for x in range(1,10):#   from 1 to <10 , default incrementer is 1
     print(x)


#print in reverse
for x in range(10,0,-1):
     print(x)
     

#WAP to print sum and avg of all numberes between 1 to 100
s = 0

for x in range(1,101):
     s +=x

print('sum of all numbers :',s)
print('avg of all numbers :',s/100)
     

f = open(r'C:\Users\vkumar15\Desktop\Java - Session 16th Jan.txt','r')
#print(f)

#print(f.read())

#read by line
#print(f.readline())
#print(f.readline())

#read all lines and store on list
data = f.readlines()
#print(data)
print('row count ', len(data))

#word count
wc = 0
#count of particular word
pwc =0
for r in data:
     print(r)
     c = r.split(' ')
     wc = wc+ len(c)
     for w in c:
          if w =='is':
               pwc +=1
               
               


print(wc)
print(pwc)





     
     
     











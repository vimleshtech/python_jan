sales = int(input('enter sale amount :'))
#if condition
tax =0

if sales>1000:
     tax = sales*.18     
total = sales+tax
print(total)


#if else condition
tax =0
if sales>1000:
     tax = sales*.18
else:
     tax = sales*.05
     
total = sales+tax
print(total)

##if elif ...
tax =0
if sales>100000:
     tax = sales*.18
elif sales>10000:
     tax = sales*.12
elif sales>1000:
     tax = sales*.05
else:
     tax = 0
     
     
total = sales+tax
print(total)

##show greater number from three inputs
a = int(input('enter data :'))
b = int(input('enter data :'))
c = int(input('enter data :'))

if a>b and a>c:
     print('a is gt')
elif b>a and b>c:
     print('b is gt')
else:
     print('c is gt')

#nested condition
if a>b:
     if a>c:
          print('a is gt')
     else:
          print('c is gt')
else:
     if b>c:
          print('b is gt')
     else:
          print('c is gt')
          





                

          
          




          






     















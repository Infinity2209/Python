import math
b=0
b=int(b)
count=0
count=int(count)
a=input("Enter your number: ")
a=int(a)
c=a
c=int(c)
while c>0:
    count=count+1
    c=c//10
c=a
print(c)
while c>0:
    p=(c%10)
    b=b+math.pow(p,count) 
    c=c//10  
    
if (b==a):
  print("Your number is an amstrong number")
else:
  print("Your number is not an amstrong number")
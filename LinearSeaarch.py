def linersearch(A,n,x):
  for i in range(0,n):
    if(A[i]==x):
      return i+1
  return -1
A=[23,25,14,75,62,42,41]
n=len(A)
s=input("Enter your searching element \n")
s=int(s)
r= linersearch(A,n,s)
if (r==-1):
  print("NO element exist")
else:
  print("Element found at",r+1)

import math
print("Enter all the coefficient in the manner ax^2+bx+c=0\n")
a=input()
a=int(a)
b=input()
b=int(b)
c=input()
c=int(c)
D=(pow(b, 2)-(4*a*c))
if D>0:
  x1=(-b+math.pow(D, 1/2))/(2*a)
  x2=(-b-math.pow(D, 1/2))/(2*a)
  print("Your values of x are\n",x1,x2)
elif D==0:
  x=-b/(2*a)
  print("Your values for x are equal since your D=0 so x=",x)
else:
  x1=(-b+math.pow(D, 1/2))/(2*a)
  x2=(-b-math.pow(D, 1/2))/(2*a)
  print("Your values for x is complex in nature, values are\n",x1,x2)
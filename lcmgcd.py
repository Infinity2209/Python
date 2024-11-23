a=input("Enter your first number\n")
a=int(a)
b=input("Enter your second number\n")
b=int(b)
lcm=1
gcd=1
for item in range(max(a,b),1+(a*b)):
    if item%a==item%b==0:
      lcm=item
      break
print("LCM = ",lcm)
if a%b==0 or b%a==0:
  gcd=min(a,b)
else:
    for i in range(1,min(a,b)):
        if a%i==b%i==0:
            gcd=i
print("GCD = ",gcd)
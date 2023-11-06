from array import*
dict_sample={"CSE":1,"CE":2,"EE":3,"ME":4}
print(dict_sample)
print(dict_sample['CE'])
l=[1,2,'a','b',3,4]
print(l[-1],l[-2],l[0],l[1])
str='Learning'
print(str.index('i'),str.index('L'),str.index('ing'),str[-8])
L1=[1,2,3,'a','sam',2]
print(L1.index("sam"))
array_sample= array('i',[1,2,3,4])
for x in array_sample:
    print(x)
print(str[slice(0,7,1)])
S="GEEKSFORGEEKS"
print(str[0:7:1])
print(str[0:7:2])
list=[50,70,30,20,90,10,50]
print(list[-7::1])
print(list[-7:5:1])
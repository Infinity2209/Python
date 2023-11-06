def binarysearch(a,x,l,h):
    while l<=h:
        mid=(l+h)//2
        if a[mid]==x:
            return mid
        elif a[mid]<x:
            l=mid+1
            binarysearch(a,x,l,h)
        else:
            h=mid-1
            binarysearch(a, x, l, h)
    return -1
a=[10,20,30,40,50,60]
s=input("Enter your Searching element\n")
s= int(s)
l=0
h=len(a)
r=binarysearch(a, s, l, h)
if r==-1:
    print("Element not found")
else:
    print("Element found at ",r+1)

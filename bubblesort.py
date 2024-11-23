def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print("Sorted Array is :\n")
    for item in range(n):
        print(arr[item])

data=[2,9,5,7,3,5,4,3,10]
bubblesort(data)

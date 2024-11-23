print("The prime numbers in between 10 to 1000 are\n")
for i in range(11,1000):
    for j in range(2,10):
        if i%j==0:
            break
    else:
        print(i)
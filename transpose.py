A=[[1,2,3],[4,5,6],[7,8,9]]
T=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        T[i][j]=A[j][i]
print(T)
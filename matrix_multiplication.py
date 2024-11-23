A=[[1,2,3],[2,3,4],[3,4,5]]
B=[[4,2,3],[5,3,4],[6,4,5]]
M=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        mul=0
        for k in range(0,3):
            mul=mul+(A[i][k]*B[k][j])
        M[i][j]=mul
print(M)
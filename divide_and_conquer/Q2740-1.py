n,m=map(int,input().split())
arr1=[list(map(int,input().split())) for _ in range(n)]
m,k=map(int,input().split())
arr2=[list(map(int,input().split())) for _ in range(m)]
result = [[0 for _ in range(k)]for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            result[i][j]+=arr1[i][l]*arr2[l][j]

for i in range(n):
    for j in range(k):
        print(result[i][j],end=" ")
    print()
                
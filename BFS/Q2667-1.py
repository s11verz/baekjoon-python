n=int(input())
arr=[list(map(int,input())) for _ in range(n)]
result=[]


def dfs(x,y):
    global count
    count+=1
    arr[x][y]=0
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for k in range(4):
        a=x+dx[k]
        b=y+dy[k]
        if 0<=a<n and 0<=b<n and arr[a][b]==1:
            dfs(a,b)
    



for i in range(n):
    for j in range(n):
        count=0
        if arr[i][j]==1:
            dfs(i,j)
        if count!=0:
            result.append(count)

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])
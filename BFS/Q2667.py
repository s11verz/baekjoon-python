
n=int(input())
arr = [list(map(int, input())) for _ in range(n)]
result=[]
count=0
def dfs(x,y):
    global count
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    arr[x][y]=0
    count+=1
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(nx<0 or nx>=n or ny<0 or ny>=n):
            continue
        if(arr[nx][ny]== 1):
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if (arr[i][j]==1):
            count=0
            dfs(i,j)
            result.append(count)

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])




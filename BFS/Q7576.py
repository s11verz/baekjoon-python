from typing import Deque


m,n=map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q=Deque()
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs():
    while q:
        a,b=q.popleft()
        
        for i in range(4):
            x=a+dx[i]
            y=b+dy[i]
            if 0<=x<n and 0<=y<m and arr[x][y]==0:
                arr[x][y]=arr[a][b]+1
                q.append([x,y])
                

for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            q.append([i,j])
bfs()
answer=0
for i in arr:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    answer=max(answer,max(i))
print(answer-1)
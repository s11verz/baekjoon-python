from typing import Deque


t=int(input())
dx=[-1,0,0,1]
dy=[0,1,-1,0]

def bfs(sx,sy):
    q=Deque()
    q.append([sx,sy])
    while q:
        a,b=q.popleft()
        for i in range(4):
            x=a+dx[i]
            y=b+dy[i]
            if 0<=x<n and 0<=y<m and arr[x][y]==1:
                q.append([x,y])
                arr[x][y]=0



for _ in range(t):
    count=0
    m,n,k=map(int,input().split())
    arr = [[0]*(m) for i in range(n)]
    for _ in range(k):
        a,b=map(int,input().split())
        arr[b][a]=1
    for x in range(n):
        for y in range(m):
            if arr[x][y]==1:
                bfs(x,y)
                arr[x][y]=0
                count+=1
    print(count)

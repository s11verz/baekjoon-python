from typing import Deque


n,m=map(int,input().split())
arr = [list(map(int, input())) for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(bx,by,ax,ay):
    q=Deque()
    q.append([bx,by])
    while q:
        a,b=q.popleft()
        if a==ax and b==ay:
            print(arr[ax][ay])
            return
        for i in range(4):
            x=a+dx[i]
            y=b+dy[i]
            if (0<=x<n and 0<=y<m and arr[x][y]==1):
                q.append([x,y])
                arr[x][y]=arr[a][b]+1


bfs(0,0,n-1,m-1)

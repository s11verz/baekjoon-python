from typing import Deque


n=int(input())

dx=[-2,-1,1,2,-2,-1,1,2]
dy=[-1,-2,-2,-1,1,2,2,1]

def func(ax,ay,sx,sy):
    q=Deque()
    q.append([ax,ay])
    matrix[ax][ay]=1
    while q:
        a,b=q.popleft()
        if a==sx and b==sy:
            print(matrix[a][b]-1)
            return
        for i in range(8):
            rx=a+dx[i]
            ry=b+dy[i]
            if 0<=rx<l and 0<=ry<l and matrix[rx][ry]==0:
                q.append([rx,ry])
                matrix[rx][ry]=matrix[a][b]+1
                

    

for i in range(n):
    l=int(input())
    matrix=[[0]*l for _ in range(l)]
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    func(x,y,a,b)


from collections import deque
n, m = map(int, input().split())
#arr = [list(map(int, input().split())) for _ in range(n)]
arr=[]
for _ in range(n):
  arr.append(list(map(int, input())))


def bfs(x,y):
    #   상,하,좌,우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    check=deque()
    check.append((x,y))
    while check:
        x,y=check.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if(nx<0 or nx>=n or ny<0 or ny>=m):
                continue
            if(arr[nx][ny]== 0):
                continue
            if(arr[nx][ny]== 1):
                arr[nx][ny]=arr[x][y]+1
                check.append((nx,ny))
    return arr[n-1][m-1]


print(bfs(0,0))
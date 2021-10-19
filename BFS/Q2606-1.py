n=int(input())
m=int(input())
matrix=[[0]*(n+1) for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    matrix[a][b]=matrix[b][a]=1
visit=[0]*(n+1)


def dfs(target):
    visit[target]=1
    for i in range(n+1):
        if ((visit[i]==0 and matrix[target][i]==1)or(visit[i]==0 and matrix[i][target]==1)) :
            dfs(i)
       
        

dfs(1)
count=0
for i in range(n+1):
    if visit[i]==1:
        count+=1
print(count-1)

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
neg=0
neut=0
pos=0

def divide(x,y,n):
    global neg,neut,pos
    check=arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j]!=check:
                for k in range(3):
                    for l in range(3):
                        divide(x+k*n//3,y+l*n//3,n//3)
                return
    if check==-1:
        neg+=1
    elif check==0:
        neut+=1
    else:
        pos+=1

divide(0,0,n)
print(neg)
print(neut)
print(pos)

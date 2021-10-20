n=int(input())
arr=[list(map(int,input())) for i in range(n)]

def divide(x,y,n):
    check=arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j] != check:
                check=-1
                break
    
    if check==-1:
        n//=2
        print("(",end="")
        divide(x,y,n)
        divide(x,y+n,n)
        divide(x+n,y,n)
        divide(x+n,y+n,n)
        print(")",end="")

    elif check==1:
        print(1,end="")
    else:
        print(0,end="")

divide(0,0,n)

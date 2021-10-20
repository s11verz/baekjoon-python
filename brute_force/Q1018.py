n,m=map(int,input().split())
arr=[input() for _ in range(n)]
result=[]


for i in range(n-7):
    for j in range(m-7):
        first_W=0
        first_B=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if arr[a][b]!='W':
                        first_W+=1
                    if arr[a][b]!='B':
                        first_B+=1
                else:
                    if arr[a][b]!='B':
                        first_W+=1
                    if arr[a][b]!='W':
                        first_B+=1
        result.append(first_W)
        result.append(first_B)

print(min(result))           
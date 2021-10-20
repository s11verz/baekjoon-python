n,m=map(int,input().split())
arr=[int(i) for i in input().split()]
result=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            answer=arr[i]+arr[j]+arr[k]
            if answer<=m:
                result.append(answer)
                
print(max(result))

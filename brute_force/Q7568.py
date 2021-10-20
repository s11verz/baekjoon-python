n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]

for i in arr:
    count=1
    for j in arr:
        if i[0]<j[0] and i[1]<j[1]:
            count+=1
    print(count,end=" ")
    



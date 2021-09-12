n=int(input())
m=int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
result=[]

def find(x):
    for i in range(m):
        if(arr[i][0]==x):
            if(arr[i][1] not in result):
                result.append(arr[i][1])
                find(arr[i][1])
        if(arr[i][1]==x):
            if(arr[i][0] not in result):
                result.append(arr[i][0])
                find(arr[i][0])
    return



find(1)
if(1 in result):
    result.remove(1)
print(len(result))





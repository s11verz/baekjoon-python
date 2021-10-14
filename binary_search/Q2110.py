n, c = map(int, input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))

arr.sort()

def binary():
    start=1
    end=arr[-1]-arr[0]
    while start<=end:
        mid=(start+end)//2
        count=1
        gap=min(arr)+mid

        for i in range(1,n):
            if gap<=arr[i]:
                count+=1
                gap=arr[i]+mid
        
        if count>=c:
            start=mid+1
        elif count<c:
            end=mid-1
    return end

print(binary())
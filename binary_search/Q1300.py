n=int(input())
k=int(input())

def binary(target,start,end):
    while(start<=end):
        mid=(start+end)//2
        count=0
        for i in range(1,n+1):
            count+=min(mid//i,n)
        if count<target:
            start=mid+1
        else:
            end=mid-1
    return start

print(binary(k,1,n*n))

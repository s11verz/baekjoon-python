# 가장 긴 증가하는 부분 수열 2

n=int(input())
A=[int(i) for i in input().split()]
result=[0]


for i in range(n):  
    low=0
    high=len(result)-1
    while low<=high:
        mid=(low+high)//2
        if(result[mid]<A[i]):
            low=mid+1
        else:
            high=mid-1
    if (low>=len(result)):
        result.append(A[i])
    else:
        result[low]=A[i]

print(len(result)-1)
        
n=int(input())
arr1=[int(i) for i in input().split()]
arr1.sort()
m=int(input())
arr2=[int(i) for i in input().split()]

for i in arr2:
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if arr1[mid]==i:
            break
        if arr1[mid]>i:
            end=mid-1
        else:
            start=mid+1
    if arr1[mid]==i:
        print(arr1.count(i),end=" ")
    else:
        print(0,end=" ")

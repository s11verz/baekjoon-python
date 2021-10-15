n=int(input())
arr1=[int(i) for i in input().split()]
m=int(input())
arr2=[int(i) for i in input().split()]


for i in range(m):
    if arr2[i] in arr1:
        print(1)
    else:
        print(0)

# def binary(target):
#     left=0
#     right=arr1[-1]-arr1[1]
#     while left<=right:
#         mid=(left+right)//2
#         if arr1[mid]==target:
#             return True
#         if target<arr1[mid]:
#             right=mid-1
#         elif target>arr1[mid]:
#             left=mid+1

# for i in range(m):
#     if binary(arr2[i]):
#         print(1)
#     else:
#         print(0)
    

n=int(input())
arr=[int(i) for i in input().split()]
result=[0 for i in range(n)]
resultSum=0

arr.sort()

for i in range(n):
    resultSum+=arr[i]
    result[i]=resultSum

print(sum(result))


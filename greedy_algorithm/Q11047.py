n, k = map(int, input().split())
arr = []
sum = 0
count=0
for i in range(n):
    arr.append(int(input()))

for i in reversed(arr):
    if(k==0):
        break
    if(i<=k):
        count+=k//i
        k%=i
    
print(count)
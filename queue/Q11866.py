from collections import deque

n, k = map(int, input().split())
result=[]
queue=deque([])
for i in range(n):
    queue.append(i+1)

while queue:
    for i in range(k-1):
        queue.append(queue[0])
        queue.popleft()
    result.append(queue.popleft())
print('<',end='')
print(*result, sep=', ',end='')
print('>')

    


    

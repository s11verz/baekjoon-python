n=int(input())

def solution(x):
    answer=0
    while x>0:
        answer+=x%10
        x//=10
    return answer

for i in range(1,n+1):
    if i+solution(i)==n:
        print(i)
        break
    if i==n:
        print(0)

        
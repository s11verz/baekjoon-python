t=int(input())
result=[]

for i in range(t):
    put=input()
    arr=list(put)
    sum=0
    for j in arr:
        if(j=='('):
           sum+=1
        elif(j==')'):
           sum-=1
        if(sum<0):
           result.append('NO')
           break
    if(sum==0):
        result.append('YES')
    elif(sum>0):
        result.append('NO')

for i in range(t):
    print(result[i])




        


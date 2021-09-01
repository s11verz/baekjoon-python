#링

def gcd(a,b):
    while(a%b!=0):
        mod=a%b
        b=mod
    return b

n=int(input())
arr=[int(i) for i in input().split()]

for i in range (n-1):
    g=gcd(arr[0],arr[i+1])
    print('{}/{}'.format(arr[0]//g,arr[i+1]//g))
   



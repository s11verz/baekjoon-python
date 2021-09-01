from collections import deque
import sys
n=int(input())
queue=deque([])
input = sys.stdin.readline

def push_front(x):
    queue.appendleft(x)

def push_back(x):
    queue.append(x)

def pop_front():
    if(len(queue)==0): return(-1)
    else: return(queue.popleft())

def pop_back():
    if(len(queue)==0): return(-1)
    else: return(queue.pop())

def size():
    return len(queue)

def empty():
    if(len(queue)==0): return(1)
    else: return(0)

def front():
    if(len(queue)==0): return(-1)
    else: return(queue[0])
def back():
    if(len(queue)==0): return(-1)
    else: return(queue[-1])



for i in range(n):
    ask = input().split()
    if 'push_front' in ask:
        push_front(ask[1])
    elif 'push_back' in ask:
        push_back(ask[1])
    elif 'pop_front' in ask:
        print(pop_front())
    elif 'pop_back' in ask:
        print(pop_back())
    elif 'size' in ask:
        print(size())
    elif 'empty' in ask:
        print(empty())
    elif 'front' in ask:
        print(front())
    elif 'back' in ask:
        print(back())
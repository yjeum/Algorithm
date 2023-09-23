import sys
from collections import deque

q = deque([i for i in range(1, int(sys.stdin.readline())+1)])

new_q = []


while len(q) != 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])
            

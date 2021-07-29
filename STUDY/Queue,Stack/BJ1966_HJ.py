from collections import deque
import sys
input= sys.stdin.readline
t = int(input()) 
for _ in range(t):
    n , m = map(int,input().split())
    que = deque(list(map(int,input().split())))
    idx = deque(list(range(n)))
    cnt = 0
    while que:
        if que[0] == max(que):
            cnt += 1
            que.popleft()
            if idx.popleft() == m :
                print(cnt) 
        else:
            que.append(que.popleft())
            idx.append(idx.popleft())

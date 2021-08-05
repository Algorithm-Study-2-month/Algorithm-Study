from collections import deque


que=deque()
dy = [1,-1,0,0]
dx = [0,0,1,-1]
def bfs(x,y):
    que.append((x,y))
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x +dx[i], y+dy[i]
            if 0<=nx<n and 0<= ny< m:
                if graph[ny][nx] ==1:
                    que.append((nx,ny))
                    graph[ny][nx] = 2                   
T = int(input())
for _ in range(T):
    n,m,k = map(int,input().split())
    graph = [[0]*n for _ in range(m)]
    cnt = 0
    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1
    for i in range(n):
        for j in range(m):
            if graph[j][i] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)

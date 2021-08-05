from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
n,m = map(int, input().split())
a = [list(map(int,input())) for _ in range(n)]

check=[[False]*m for _ in range(n)]

que = deque()

que.append((0,0))
check[0][0]=True
while que:
    x,y = que.popleft()
    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]
        if 0<= nx < n and  0<= ny < m :
            if check[nx][ny] == False and a[nx][ny] == 1:
                que.append((nx,ny))
                a[nx][ny] = a[x][y] + 1
                check[nx][ny] = True

print(a[n-1][m-1])

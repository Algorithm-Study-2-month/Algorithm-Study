from collections import deque

n,m,k = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    m1,m2 = map(int,input().split())
    graph[m1][m2]=graph[m2][m1]=1



def dfs(start,check=[]):
    check.append(start)
    print(start,end=" ")
    for i in range(len(graph[start])):
        if graph[start][i] ==1 and (i not in check):
            dfs(i)

            
def bfs(start):
    check=[start]
    que=deque()
    que.append(start)
    
    while que:
        ans = que.popleft()
        print(ans, end=" ")
        for i in range(len(graph[start])):
            if graph[ans][i] ==1 and (i not in check):
                check.append(i)
                que.append(i)
    
    
dfs(k)
print()
bfs(k)

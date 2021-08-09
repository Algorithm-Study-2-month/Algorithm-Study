import heapq
r=[]
n = int(input())
cnt = 1
queue=[]
room = [list(map(int,input().split())) for _ in range(n)]
room.sort(key= lambda x : x[0])
heapq.heappush(queue,room[0][1])
for i in range(1,n):
    if queue[0] > room[i][0]:
        heapq.heappush(queue,room[0][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue,room[0][1])
 
print(len(queue))
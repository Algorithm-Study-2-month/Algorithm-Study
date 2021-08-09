import sys
input = sys.stdin.readline
n,k = map(int,input().split())
b=[]

for _ in range(n):
    a = int(input())
    b.append(a)
    b.sort(reverse=True)
cnt =0
for i in range(n):
    s= k//b[i]
    k = k%b[i]
    cnt += s

print(cnt)

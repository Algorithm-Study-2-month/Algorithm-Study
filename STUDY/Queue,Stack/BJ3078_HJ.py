import sys
input=sys.stdin.readline

n, k = map(int,input().strip().split())
students = [0] * n
data = [0] * 21
count = 0

for rank in range(n):
    name = len(input().strip())
    students[rank] = name
    if rank > k:
        data[students[rank - k - 1]] -= 1
    count += data[name]
    data[name] += 1

print(count)

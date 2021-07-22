a = int(input())
ans =[]
for i in range(a):
    b = int(input())
    for k in range(a):
        ans.append(list(map(int,input().split())))
    ans[0][1] += ans[1][0]
    ans[1][1] += ans[0][0]
    for j in range(2, b):
        ans[0][j] += max(ans[1][j - 1], ans[1][j - 2])
        ans[1][j] += max(ans[0][j - 1], ans[0][j - 2])
    print(max(ans[0][b - 1], ans[1][b - 1]))

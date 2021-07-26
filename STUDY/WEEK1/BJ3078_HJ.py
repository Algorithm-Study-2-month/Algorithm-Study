from itertools import combinations
n,k = map(int,input().split(" "))
b=[]
cnt = 0
cnt1=0
for _ in range(n):
    a =input()
    b.append(a)
result = list(combinations(b,2))
for i in range(len(result)):
    if len(result[i][0]) != len(result[i][1]):
        cnt += 1
    elif (b.index(result[i][1])-b.index(result[i][0])) > k:
        cnt1 +=1

        
        
    
ans = len(result)-cnt-cnt1
print(ans)

n, k = map(int, input().split())
coin = []
ans=[0 for i in range(k+1)]
for _ in range(n):
    coin.append(int(input()))
for i in range(k+1):
    if i==0:
        ans[0]=0
    elif  coin[0]<=i <coin[1]:
        ans[i] = ans[i-coin[0]]+1
    elif coin[1]<= i <coin[2]:
        ans[i] = ans[i-coin[1]]+1
    elif i%coin[1] != 0 and i%coin[2] != 0 and coin[2]<=i:
        ans[i] = ans[i-coin[2]]+1
    elif i%coin[1]==0:
        ans[i]= int(i/coin[1])
    elif i%coin[2]==0:
        ans[i]= int(i/coin[2])
        
    
print(ans)

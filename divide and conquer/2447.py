def mkstars(star):
    arr = []
    for i in range(3 * len(star)):
        if i // len(star) == 1:
            arr.append(star[i % len(star)] + " " * len(star) + star[i%len(star)])
        else:
            arr.append(star[i%len(star)]*3)
    return (list(arr))   

n=int(input())

star = ["***","* *","***"]
k=0
#3일때는 k =0 9일때는 k=1 27일때는 k=2
while n != 3:
    n=int(n/3)
    k +=1

for i in range(k):
    star = mkstars(star)
for i in star:
    print(i)
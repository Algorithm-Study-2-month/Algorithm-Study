def QuadTree(x,y,n):
    check = tree[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != tree[i][j]:
                print('(', end='')
                QuadTree(x,y,n//2) 
                QuadTree(x,y+n//2,n//2) 
                QuadTree(x+n//2,y,n//2) 
                QuadTree(x+n//2,y+n//2,n//2) 
                print(")",end="")
                return

    if check == 0:
        print('0',end="")
        return
    else:
        print('1',end="")
        return
n = int(input())
tree = [list(map(int,input())) for _ in range(n)]

QuadTree(0,0,n)
import sys
que = []
n= int(sys.stdin.readline())
for _ in range(n):
    m=sys.stdin.readline().split()
    if m[0] == "push":
        que.append(m[1])
    elif m[0] == "pop":
        if len(que)==0:
            print(-1)
        else:
            print(que.pop(0))
    elif m[0] == "size":
        print(len(que))
    elif m[0] == "empty":
        if len(que)==0:
            print(1)
        else:
            print(0)
    elif m[0] == "front":
        if len(que)==0:
            print(-1)
        else:
            print(que[0])
    elif m[0] == "back":
        if len(que)==0:
            print(-1)
        else:
            print(que[-1])

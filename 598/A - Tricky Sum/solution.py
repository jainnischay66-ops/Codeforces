t= int(input())
for _ in range(t):
    n = int(input())
    f = []
    for i in range(64):
        if 2**i<=n:
            f.append(2**i)
    print((n*(n+1)//2)-(2*(sum(f))))
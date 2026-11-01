t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = sorted(map(int,input().split()),reverse=True)
    total = 0
    for i in range(min(n,m)):
        total += a[i]*(m-i)
    print(total)
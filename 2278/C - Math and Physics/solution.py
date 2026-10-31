t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    d = set(a)
    if len(d)==1 and 1 in a:
        print(-1)
    elif n==2 or max(a[1:n-1])>=2:
        print(sum(a)-1)
    else:
        print(sum(a)-(n-1))
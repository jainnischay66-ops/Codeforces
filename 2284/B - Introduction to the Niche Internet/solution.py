t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    maximum = a[-1]
    if a.count(maximum)>k:
        print("NO")
    else:
        print("YES")
        s = a[n-k:]+a[:n-k][::-1]
        print(*s)
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    f = set(a)
    print(len(f))
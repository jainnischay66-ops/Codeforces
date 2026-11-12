t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    if sum(a[::k+1])%2==1:
        print("Alice")
    else:
        print("Bob")
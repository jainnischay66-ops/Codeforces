n = int(input())
a = list(map(int,input().split()))
s = sum(a)
if s%2==0:
    print(s)
else:
    m = 10**9+1
    for i in a:
        if i%2 and i<m:
            m = i
    print(s-m)
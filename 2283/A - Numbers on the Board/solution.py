t = int(input())
for _ in range(t):
    l,r = map(int,input().split())
    if l>0 or r<0:
        print(abs(r-l))
    else:
        print(max(0,abs(l+r)-1))
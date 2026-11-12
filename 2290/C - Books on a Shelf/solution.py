t=int(input())
for _ in range(t):
    n=int(input())
    f=list(map(int,input().split()))
    f.sort()
    a=[]
    b=[]
    for i in range(n):
        if i==0 or f[i]!=f[i-1]:
            a.append(f[i])
        else:
            b.append(f[i])
    b.reverse()
    print(len(a)+len(set(b)))
    print(*(a+b))
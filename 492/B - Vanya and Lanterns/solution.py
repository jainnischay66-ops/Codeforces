n,l = map(int,input().split())
a = list(map(int,input().split()))
f = []
a.sort()
if n == 1:
    print(max(a[0], l-a[0]))
else:
    if 0 not in a:
        f.append(a[0])
    else:
        a.pop(0)
        f.append(a[0]/2)
    for i in range(len(a)-1):
        f.append(abs(a[i]-a[i+1])/2)
    f.append(l-a[-1])
    print(max(f))
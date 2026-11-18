n = int(input())
a = list(map(int,input().split()))
f = []
for i in range(n):
    if a[i]%2==0:
        f.append(0)
    else:
        f.append(1)
if f.count(0)==1:
    print(f.index(0)+1)
else:
    print(f.index(1)+1)
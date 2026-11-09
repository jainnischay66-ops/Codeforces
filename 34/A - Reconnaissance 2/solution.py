n = int(input())
a = list(map(int,input().split()))
f = []
for i in range(n-1):
    f.append(abs(a[i]-a[i+1]))
f.append(abs(a[0]-a[-1]))
if f.index(min(f))==len(f)-1:
    print(1,n)
else:
    print(f.index(min(f))+1,f.index(min(f))+2)
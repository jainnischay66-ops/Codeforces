n = int(input())
a = list(map(int,input().split()))
a.sort()
print(a[-1]-a[0],end=" ")
if a[0]==a[-1]:
    print(n*(n-1)//2)
else:
    print(a.count(a[0])*a.count(a[-1]))
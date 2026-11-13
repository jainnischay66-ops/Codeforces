n = int(input())
a = list(map(int,input().split()))
if ((a.count(200))%2==0 or (a.count(100))>=2) and (a.count(100))%2==0:
    print("YES")
else:
    print("NO")
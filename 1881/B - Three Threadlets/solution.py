import math
t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    d = math.lcm(a,b,c)//math.gcd(a,b,c)
    f = []
    f.append(a//math.gcd(a,b,c))
    f.append(b//math.gcd(a,b,c))
    f.append(c//math.gcd(a,b,c))
    f.sort()
    if f==[1,2,3] or f==[1,1,4]:
        print("YES")
    elif f==[1,3,3]:
        print("NO")
    elif d<=3:
        print("YES")
    else:
        print("NO")
a,b,s = map(int,input().split())
d = abs(a)+abs(b)
print("Yes" if s>=d and (s-d)%2==0 else "No")
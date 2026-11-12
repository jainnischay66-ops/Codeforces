t = int(input())
a = list(map(int,input().split()))
m = 10**6+1
p = [1]*m
p[0] = p[1] = 0
for i in range(2,1001):
    if p[i]:
        for j in range(i*i,m,i):
            p[j] = 0
print("
".join("YES" if int(x**0.5)**2==x and p[int(x**0.5)] else "NO" for x in a))
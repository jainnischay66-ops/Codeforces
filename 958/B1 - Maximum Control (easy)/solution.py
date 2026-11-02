t = int(input())
l = [0]*(t+1)
for _ in range(t-1):
    a,b = map(int,input().split())
    l[a]+=1
    l[b]+=1
print(l.count(1))
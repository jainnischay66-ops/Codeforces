t = int(input())
f = []
c = True
for _ in range(t):
    a,b = map(int,input().split())
    f.append((a,b))
count = 0
f.sort()
for i in range(len(f)-1):
    if f[i][1]>f[i+1][1]:
        count += 1
    if count>=1:
        c = False
        break
if c:
    print("Poor Alex")
else:
    print("Happy Alex")
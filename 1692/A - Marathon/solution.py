t = int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    count = 0
    if a<b:
        count = count+1
    if a<c:
        count = count + 1
    if a<d:
        count = count+1
    print(count)
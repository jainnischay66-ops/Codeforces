t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    count = 0
    i = n-1
    f = []
    while i>=0:
        if a[i]>=x:
            count+=1
        elif a[i]*(len(f)+1)>=x:
            count += 1
            f = []
        else:
            f.append(a[i])
        i -= 1
    print(count)
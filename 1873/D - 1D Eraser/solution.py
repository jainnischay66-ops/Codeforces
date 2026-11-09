t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    n = input().strip()
    count = 0
    i = 0
    while i < a:
        if n[i] == "B":
            count += 1
            i += b
        else:
            i += 1
    print(count)
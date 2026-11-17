t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    odd = 0
    for i in a:
        if i%2:
            odd+=1
    if n==1 or odd==0:
        print("Moggity")
    elif (n==2 and odd==1) or(odd==3==n):
        print("Larpity")
    else:
        print("Moggity")
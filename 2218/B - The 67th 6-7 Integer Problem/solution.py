t = int(input())
for i in range (t):
    n = list(map(int,input().split()))
    n.sort()
    maximum = sum(n)- 2*(int(n[-1]))
    print(maximum*(-1))
import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    c = b//2
    if a%2==b%2:
        if b%2==0:
            print(a*(c)+b//(c))
        else:
            print(a*b+1)
    elif b%2==1 and a%2==0:
        print(-1)
    elif not(c<1) and (a*(c)+b//(c))%2==0:
        print(a*(c)+b//(c))
    else:
        print(-1)
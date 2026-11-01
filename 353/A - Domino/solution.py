t = int(input())
upper_odd = 0
lower_odd = 0
parity = False
for _ in range(t):
    a,b = map(int,input().split())
    upper_odd += a%2
    lower_odd += b%2
    if (a+b)%2==1:
        parity = True
if upper_odd%2==0 and lower_odd%2==0:
    print(0)
elif upper_odd%2==1 and lower_odd%2==1 and parity:
    print(1)
else:
    print(-1)
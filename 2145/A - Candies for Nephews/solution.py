t = int(input())
for i in range(t):
    n = int(input())
    if n%3==0:
        print(0)
    elif (n+1)%3==0:
        print(1)
    elif (n+2)%3==0:
        print(2)
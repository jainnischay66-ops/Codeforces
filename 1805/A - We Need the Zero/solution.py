from functools import reduce
import operator
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = (reduce(operator.xor,a))
    if n%2==1:
        print(b)
    elif b==0:
        print(0)
    else:
        print(-1)
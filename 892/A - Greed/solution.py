n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
b.sort()
f = b.pop(-1)
g = b.pop(-1)
if sum(a)<=f+g:
    print("YES")
else:
    print("NO")
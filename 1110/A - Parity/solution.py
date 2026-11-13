b,k = map(int,input().split())
arr = list(map(int,input().split()))
if b%2==0:
    s = arr[-1]
else:
    s = sum(arr)
if s%2==0:
    print("even")
else:
    print("odd")
n = int(input())
arr = list(map(int,input().split()))
count = 0 
for i in range(n):
    if arr[i] == 1:
        count = +1
if count !=0:
    print("HARD")
else:
    print("EASY")
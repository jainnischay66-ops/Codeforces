k = int(input())
arr = list(map(int,input().split()))
arr.sort()
arr.reverse()
total = 0
count = 0
i = 0
while total<k and i<12:
    total += arr[i]
    count += 1
    i+=1
if total<k:
    print(-1)
else:
    print(count)
n = int(input())
count = 0
for i in range(1,2**10):
    if int(bin(i)[2:])<=n:
        count += 1
print(count)
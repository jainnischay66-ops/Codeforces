n = input().strip()
count = 0
while len(n) > 1:
    n = str(sum(int(ch) for ch in n))
    count += 1
print(count)
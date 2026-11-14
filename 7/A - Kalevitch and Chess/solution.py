count = 0
column = 0
for i in range(8):
    s = input().strip()
    if "W" not in s:
        count += 1
    else:
        column = s.count("B")
print(count+column)
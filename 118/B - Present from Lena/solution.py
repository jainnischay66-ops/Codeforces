n = int(input())
 
for i in range(2*n + 1):
    row = ""
    for j in range(2*n + 1):
        d = n - abs(n-i)-abs(n-j)
        if d >= 0:
            row += str(d) + " "
        else:
            row += "  "
    print(row.rstrip())
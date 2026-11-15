n = int(input())
for i in range(n**2//2):
    if i%(n//2)==0:
        print("")
    print(1+i,n**2-i, end=" ")
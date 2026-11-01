t = int(input())
for _ in range(t):
    n= int(input())
    numCow= n//4
    numChicken = n%4//2
    print(numChicken+numCow)
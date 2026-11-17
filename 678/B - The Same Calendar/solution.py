def is_leap(x):
    if ((x)%4==0 and (x)%100!=0) or (x)%400==0:
        return True
    else:
        return False
    
n = int(input())
total = 0
i = 0
c = n
    
while (total%7!=0 or is_leap(n)!=is_leap(c)) or i == 0 :
    if ((c)%4==0 and (c)%100!=0) or (c)%400==0:
        total += 366
    else:
        total += 365 
    c += 1
    i += 1
    
print(n+i)
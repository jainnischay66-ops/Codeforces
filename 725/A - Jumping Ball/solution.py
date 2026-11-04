n = int(input())
s = input().strip()
i = 0
count = 0
while i<n and s[i]=="<":
    count+=1
    i+=1
i=-1
while abs(i)<=n and s[i]==">":
    count+=1
    i-=1
print(count)
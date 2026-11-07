s = input().strip()
one = 0
zero = 0
c = True
for i in range(len(s)):
    if s[i]=="0":
        zero += 1
        one = 0
    elif s[i]=="1":
        one += 1
        zero = 0
    if zero==7 or one==7:
        print("YES")
        c = False
        break
if c:
    print("NO")
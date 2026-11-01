t = int(input())
for i in range(t):
    s = input()
    f = len(s)
    n = len(s)-2
    if f<=10:
        print(s)
    else:
        print(s[0],n,s[f-1], sep = "")
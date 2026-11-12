t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    # f = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    # f = "abcdefghijklmnopqrstuvwxyz"
    a = set()
    if s==s[::-1]:
        print(0)
    else:
        for i in range(n//2):
            x = ord(s[i])
            y = ord(s[n-1-i])
            for j in range(min(x,y)+1,max(x,y)+1):
                a.add(j)
        print(len(a))
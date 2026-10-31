n = input().strip()
t = n.lower()
s = ["a","o","e","i","u","y"]
f = ""
for i in range(len(n)):
    if t[i] in s:
        pass
    else:
        f += "." + t[i]
print(f)
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
pos = {}
for i in range(n):
    pos[a[i]] = i+1
vasya = 0
petya = 0
for x in b:
    vasya += pos[x]
    petya += n-pos[x]+1
print(vasya,petya)
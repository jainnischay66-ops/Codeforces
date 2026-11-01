from math import perm,comb
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    print(comb(10-n,2)*6)
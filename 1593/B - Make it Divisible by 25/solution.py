def solve(s):
    n = len(s)
    ans = n
    for i in range(n):
        for j in range(i+1,n):
            num = int(s[i])*10+int(s[j])
            if num%25==0:
                ans = min(ans,(j-i-1)+(n-1-j))
    return ans
 
t = int(input())
for _ in range(t):
    s = input().strip()
    print(solve(s))
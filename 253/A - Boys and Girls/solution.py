with open("input.txt") as f:
    n,m = map(int,f.read().split())
if n>m:
    ans = "BG"*m+"B"*(n-m)
else:
    ans = "GB"*n+"G"*(m-n)
with open("output.txt","w") as f:
    f.write(ans + "
")
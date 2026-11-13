a,b,c = map(int,input().split())
d,e,f = map(int,input().split())
g,h,i = map(int,input().split())
if (a+b+d)%2==0:
    j = 1
else:
    j = 0
if (a+b+e+c)%2==0:
    k = 1
else:
    k = 0
if (f+b+c)%2==0:
    l = 1
else:
    l = 0
if (a+e+d+g)%2==0:
    m = 1
else:
    m = 0
if (d+b+e+h+f)%2==0:
    n = 1
else:
    n = 0
if (f+e+c+i)%2==0:
    o = 1
else:
    o = 0
if (g+h+d)%2==0:
    p = 1
else:
    p = 0
if (g+h+e+i)%2==0:
    q = 1
else:
    q = 0
if (h+i+f)%2==0:
    r = 1
else:
    r = 0
print(j,k,l,sep="")
print(m,n,o,sep="")
print(p,q,r,sep="")
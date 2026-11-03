k,a,b = map(int,input().split())
if b<0:
    print(abs(a)//k-(abs(b)-1)//k)
elif a<0:
    print((abs(a)//k)+(b//k)+1)
else:
    print(b//k-((a-1)//k))
    
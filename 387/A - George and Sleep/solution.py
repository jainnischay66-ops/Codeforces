h1,m1 = map(int,input().split(":"))
h2,m2 = map(int,input().split(":"))
h,m = 0,0
if m1-m2<0:
    m = 60+m1-m2
    h -= 1
else:
    m = m1-m2
h = h1-h2+h
if h<0:
    h += 24
# if h1-h2<0:
#     h = 24+h+h1-h2
# else:
#     h = h1-h2+h
if h<10:
    h = "0"+str(h)
if m<10:
    m = "0"+str(m)
print(str(h)+":"+str(m))
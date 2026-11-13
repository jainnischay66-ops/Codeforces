n = int(input())
a = list(map(int,input().split()))
one = a.count(1)
two = a.count(2)
three = a.count(3)
four = a.count(4)
six = a.count(6)
x = four        
y = three        
z = six-three   
 
if one+two+three+four+six!=n or z<0 or two!=x+z or one!=x+y+z:
    print(-1)
else:
    for i in range(min(one,two,four)):
        print(1,2,4)
    one -= min(one,two,four)
    two -= min(one,two,four)
    for j in range(min(one,six,three)):
        print(1,3,6)
    one -= min(one,three,six)
    six -= min(one,three,six)
    for k in range(min(one,two,six)):
        print(1,2,6)
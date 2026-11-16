n = int(input())
shell = int(input())
if shell==0:
    if n%6==1:
        print(1)
    elif n%6==2:
        print(1)
    elif n%6==3:
        print(2)
    elif n%6==4:
        print(2)
    elif n%6==5:
        print(0)
    else:
        print(0)
elif shell==1:
    if n%3==1:
        print(0)
    elif n%3==2:
        print(2)
    else:
        print(1)
else:
    if n%6==1:
        print(2)
    elif n%6==2:
        print(0)
    elif n%6==3:
        print(0)
    elif n%6==4:
        print(1)
    elif n%6==5:
        print(1)
    elif n%6==0:
        print(2)